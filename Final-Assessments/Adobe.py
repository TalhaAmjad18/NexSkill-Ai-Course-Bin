import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split, TimeSeriesSplit, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_absolute_error, mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout

df = pd.read_csv(r'Adobe.csv')
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.date
df.set_index('Date', inplace=True)
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

print(df.loc[df['Open'] == 0, 'Open'].count()) # 145 '0' values which is not normal
print(df.loc[df['High'] == 0, 'High'].count())
print(df.loc[df['Low'] == 0, 'Low'].count())
print(df.loc[df['Close'] == 0, 'Close'].count())

df.loc[df['Open'] == 0, 'Open'] = (df.loc[df['Open'] == 0, 'High'] + df.loc[df['Open'] == 0, 'Low']) / 2

print(df.loc[df['Open'] == 0, 'Open'].count()) 

# now we will see trends
for col in df.columns:
    sns.lineplot(data=df, x=df.index, y=col)
    plt.show()

# feature engineering process

# first we will calculate log return
df['Log Return'] = np.log(df['Close'] / df['Close'].shift(1))
print(df['Log Return'])

# now we will calculate momentum for short trends
df['Mom5'] = df['Close'] / df['Close'].shift(5)
print(df['Mom5'])

# now we will calculate momentum for medium trends
df['Mom20'] = df['Close'] / df['Close'].shift(20)
print(df['Mom20'])

# now we will calculate avg of last 20 days close price
df['MA20'] = df['Close'].rolling(20).mean()
print(df['MA20'])

# now we will calculate avg of last 50 days close price
df['MA50'] = df['Close'].rolling(50).mean()
print(df['MA50'])

# now we will calculate avg of last 100 days close price
df['MA100'] = df['Close'].rolling(100).mean()
print(df['MA100'])

# now we will calculate volatility of last 5 days to see fluctuation in log return
df['Vol5'] = df['Log Return'].rolling(5).std()
print(df['Vol5'])

# now we will calculate volatility of last 10 days to see fluctuation in log return
df['Vol10'] = df['Log Return'].rolling(10).std()
print(df['Vol10'])

# now we will calculate volatility of last 20 days to see fluctuation in log return
df['Vol20'] = df['Log Return'].rolling(20).std()
print(df['Vol20'])

# now we will calculate volatility of last 60 days to see fluctuation in log return
df['Vol60'] = df['Log Return'].rolling(60).std()
print(df['Vol60'])

# now we will calculate HL-Range w.r.t Close
df['HL-Range'] = (df['High'] - df['Low']) / df['Close']
print(df['HL-Range'])

# now we will calculate overnight price movement (gap)
df['Gap'] = df['Open'] - df['Close'].shift(1)
print(df['Gap'])

# now we will calculate volume ratio to check unusal high and low activity
df['Volume Ratio'] = df['Volume'] / df['Volume'].rolling(20).mean()
print(df['Volume Ratio'])

# now we will calculate RSI to check whether stock is overbought or oversold
df['Change'] = df['Close'] - df['Close'].shift(1)
df['Gain'] = df['Change'].clip(lower=0)
df['Loss'] = np.absolute(df['Change'].clip(upper=0))
df['Avg Gain'] = df['Gain'].rolling(14).mean()
df['Avg Loss'] = df['Loss'].rolling(14).mean()
df['RS'] = df['Avg Gain'] / df['Avg Loss']
df['RSI'] = 100 - ( 100 / ( 1 + df['RS'] ))
df.drop(columns=['Change', 'Gain', 'Loss', 'Avg Gain', 'Avg Loss', 'RS'], inplace=True)
print(df['RSI'])

# now we wil calculate MACD to find out trend direction
df['EMA12'] = df['Close'].ewm(span=12).mean()
df['EMA26'] = df['Close'].ewm(span=26).mean()
df['MACD'] = df['EMA12'] - df['EMA26']
df.drop(columns=['EMA12', 'EMA26'], inplace=True)
print(df['MACD'])

# now we will calculate ATR to identify actual price moment
df['temp1'] = df['High'] - df['Low']
df['temp2'] = np.absolute(df['High'] - df['Close'].shift(1))
df['temp3'] = np.absolute(df['Low'] - df['Close'].shift(1))
df['TR'] = np.max(df[['temp1', 'temp2', 'temp3']], axis=1)
df['ATR'] = df['TR'].rolling(14).mean()
df.drop(columns=['TR', 'temp1', 'temp2', 'temp3'], inplace=True)
print(df['ATR'])

# now we will calculate Bollinger Band Width to check how spread or volatile , price of stock is
df['std20'] = df['Close'].rolling(20).std()
df['upper'] = df['MA20'] + ( 2 * df['std20'] )
df['lower'] = df['MA20'] - ( 2 * df['std20'] )
df['BB-Width'] = (df['upper'] - df['lower']) / df['MA20']
df.drop(columns=['std20', 'upper', 'lower'], inplace=True)
print(df['BB-Width'])

# now we will calculate Stochastic Oscillator to check where is today's close in last 14 days high-low range
df['Lowest Low'] = df['Low'].rolling(14).min()
df['Highest High'] = df['High'].rolling(14).max()
df['%K'] = ( ( df['Close'] - df['Lowest Low'] ) / ( df['Highest High'] - df['Lowest Low'] ) ) * 100
df.drop(columns=['Highest High', 'Lowest Low'], inplace=True)
print(df['%K'])

# now we will calculate OBV (on balance volumne)
df['Shifted Close'] = df['Close'].shift(1)
df['OBV'] = 0

for i in range(1, len(df)):

    if df['Close'].iloc[i] > df['Shifted Close'].iloc[i]:
        df['OBV'].iloc[i] = df['OBV'].iloc[i - 1]  + df['Volume'].iloc[i]
    
    elif df['Close'].iloc[i] < df['Shifted Close'].iloc[i]:
        df['OBV'].iloc[i] = df['OBV'].iloc[i - 1]  - df['Volume'].iloc[i]

    else: 
        df['OBV'].iloc[i] = df['OBV'].iloc[i - 1]    

df.drop(columns='Shifted Close', inplace=True)
print(df['OBV'])

# now we will make a column for day of week
df['Date'] = pd.to_datetime(df.index)
df['Day of week'] = df['Date'].dt.day_of_week
df.drop(columns='Date', inplace=True)
print(df['Day of week'])

print(df.isnull().sum())
df.dropna(subset=df.columns, inplace=True)
print(df.isnull().sum())

# Exploratory Data Analysis

# we will check log return distribution
sns.histplot(data=df, x='Log Return', bins=20, kde=True) 
plt.show()

# boxplot for outliers
sns.boxplot(data=df, x='Log Return') 
plt.show()

# heatmap for correlation
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.tight_layout()
plt.show()

# pairplot among different columns
sns.pairplot(df[['Close', 'Log Return', 'RSI', 'MACD']])
plt.show()

# day of week vs log return
sns.violinplot(data=df, x='Day of week', y='Log Return')
plt.show()

# # volatility along with time
sns.lineplot(data=df, x=df.index, y='Vol20')
plt.show()

# volume along with time
sns.lineplot(data=df, x=df.index, y='Volume')
plt.show()

# RSI along with time
sns.lineplot(data=df, x=df.index, y='RSI')
plt.show()

# Price Trend Analysis
plt.figure(figsize=(10,8))
plt.plot(df['Close'])
plt.plot(df['MA20'])
plt.plot(df['MA50'])
plt.plot(df['MA100'])
plt.show()

# Statistical Research

# Tomorrow Return
df['Tomorrow Return'] = (df['Close'].shift(-1) / df['Close']) - 1
print(df['Tomorrow Return'])

# Future 5-Day Return
df['Future 5-Day Return'] = (df['Close'].shift(-5) / df['Close']) - 1
print(df['Future 5-Day Return'])

# Future 20-Day Return
df['Future 20-Day Return'] = (df['Close'].shift(-20) / df['Close']) - 1
print(df['Future 20-Day Return'])

# checking correlation of features with Tommorrow Return

temp_df = df.dropna()
def check_corr(target):
    pearson_list = list()
    for col in temp_df.columns:
        pearson_dict = dict()
        corr_coef, p_val = pearsonr(temp_df[col], target)
        pearson_dict['name'] = col
        pearson_dict['correlation coefficient'] = corr_coef
        pearson_dict['p value'] = p_val
        pearson_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
        pearson_list.append(pearson_dict)
    pearson_df = pd.DataFrame(pearson_list)
    print(pearson_df)

check_corr(temp_df['Tomorrow Return'])
check_corr(temp_df['Future 5-Day Return'])
check_corr(temp_df['Future 20-Day Return'])

sns.scatterplot(data=df, x='OBV', y='Future 20-Day Return')
plt.show()

df.dropna(inplace=True)

# Classification target column

df['Up / Down'] = 0
for i in range(len(df)):
    if df['Tomorrow Return'].iloc[i] > 0:
        df['Up / Down'].iloc[i] = 1
    else:
        df['Up / Down'].iloc[i] = 0

# now we will make X and y
print(df.columns)

X_columns = [
    'Log Return','Mom5','Mom20','MA20','MA50','MA100','Vol5','Vol10','Vol20',
    'Vol60','HL-Range','Gap','Volume Ratio','RSI','MACD','ATR','BB-Width',
    '%K','OBV','Day of week'
]

X = df[X_columns]
y = df['Up / Down']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=False)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def train_evaluate_classification_model(name, model):
    print(name)
    model.fit(X_train, y_train)
    # print(model.best_estimator_)
    y_pred = model.predict(X_test)
    result = {
        'Accuracy score': accuracy_score(y_test, y_pred),
        'Confusion matrix': confusion_matrix(y_test, y_pred),
        'Classification report': classification_report(y_test, y_pred),
    }
    return result

# hyperparameter tunning using Grid Search CV
# logistic_regressor = GridSearchCV(estimator=LogisticRegression(max_iter=1000), param_grid = {
#                             'C': [0.01, 0.1, 1, 10, 100],
#                             'solver': ['liblinear', 'lbfgs'],
#                             'penalty': ['l2']
#                         },
#                         cv = TimeSeriesSplit(n_splits=5))
logistic_regressor = LogisticRegression(C=0.01, max_iter=1000, penalty='l2')
result = train_evaluate_classification_model('Logistic Regression', logistic_regressor)  
print('Accuracy score: ', result['Accuracy score']) 
print('Confusion matrix: ', result['Confusion matrix'])
print('Classification report: ', result['Classification report'])

# hyperparameter tunning using Grid Search CV
# dt_classifier = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42), param_grid = {
#                             'criterion': ['gini', 'entropy'],
#                             'max_depth': [3, 5, 10, 15, None],
#                             'min_samples_split': [2, 5, 10],
#                             'min_samples_leaf': [1, 2, 5]
#                         },
#                         cv = TimeSeriesSplit(n_splits=5), 
#                         n_jobs=-1)
dt_classifier = DecisionTreeClassifier(max_depth=15, min_samples_leaf=5, random_state=42) 
result = train_evaluate_classification_model('Decision Tree Classifier', dt_classifier)
print('Accuracy score: ', result['Accuracy score']) 
print('Confusion matrix: ', result['Confusion matrix'])
print('Classification report: ', result['Classification report'])
# now we will visualize confusion matrix of Decision Tree using heatmap
sns.heatmap(data=result['Confusion matrix'], annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Decision Tree Consfusion Matrix')
# plt.show()

# hyperparameter tunning using Grid Search CV
# rf_classifier = GridSearchCV(estimator=RandomForestClassifier(random_state=42),    param_grid={
#                             'n_estimators': [100, 200],
#                             'max_depth': [5, 10, None],
#                             'min_samples_split': [2, 10],
#                             'min_samples_leaf': [1, 5],
#                             'max_features': ['sqrt']
#                         },
#                         cv = TimeSeriesSplit(n_splits=5), 
#                         n_jobs=-1)
rf_classifier = RandomForestClassifier(min_samples_leaf=5, random_state=42) 
result = train_evaluate_classification_model('Random Forest Classifier', rf_classifier)
print('Accuracy score: ', result['Accuracy score']) 
print('Confusion matrix: ', result['Confusion matrix'])
print('Classification report: ', result['Classification report'])

# Since decision tree performed the best now we will check which features are important
feature_importance_dict = dict()
for i in range(len(X_columns)):
    item = {
        X_columns[i]: dt_classifier.feature_importances_[i]
    }
    feature_importance_dict.update(item)
feature_importance_df = pd.DataFrame([feature_importance_dict], index=['Feature Importance'])
print(feature_importance_df.T.sort_values(by='Feature Importance', ascending=False))

# Now we will do Regression

# Regression target column
y = df['Tomorrow Return']
# X columns will be same
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=False)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def train_evaluate_regression_model(name, model):
    print(name)
    model.fit(X_train, y_train)
    # print(model.best_estimator_)
    y_pred = model.predict(X_test)
    result = {
        'y pred': y_pred,
        'R2 score': r2_score(y_test, y_pred),
        'Mean Absolute Error': mean_absolute_error(y_test, y_pred),
        'Mean Squared Error': mean_squared_error(y_test, y_pred),
        'Root Mean Squared Error': np.sqrt(mean_squared_error(y_test, y_pred)),
    }
    return result

# linear_regressor = GridSearchCV(estimator=LinearRegression(),  param_grid={
#         'fit_intercept': [True, False],
#         'positive': [True, False]
#     },
#     cv=TimeSeriesSplit(n_splits=5),)
linear_regressor = LinearRegression(positive=True)
result = train_evaluate_regression_model('Linear Regression', linear_regressor)
print('R2 Score: ', result['R2 score'])
print('Mean Absolute Error: ', result['Mean Absolute Error'])
print('Mean Squared Error: ', result['Mean Squared Error'])
print('Root Mean Squared Error: ', result['Root Mean Squared Error'])

# dt_regressor = GridSearchCV(estimator=DecisionTreeRegressor(random_state=42),   param_grid={
#         'criterion': ['squared_error', 'absolute_error'],
#         'max_depth': [5, 10, 15, None],
#         'min_samples_split': [2, 5, 10],
#         'min_samples_leaf': [1, 2, 5]
#     },
#     cv=TimeSeriesSplit(n_splits=5),
#     n_jobs=-1)
dt_regressor = DecisionTreeRegressor(criterion='absolute_error', max_depth=5, min_samples_leaf=2, random_state=42)
result = train_evaluate_regression_model('Decision Tree Regressor', dt_regressor)
print('R2 Score: ', result['R2 score'])
print('Mean Absolute Error: ', result['Mean Absolute Error'])
print('Mean Squared Error: ', result['Mean Squared Error'])
print('Root Mean Squared Error: ', result['Root Mean Squared Error'])
plt.figure(figsize=(10,8))
plt.plot(result['y pred'], label='Predicted')
plt.plot(y_test.values, label='Actual')
# plt.show()

# rf_regressor = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid={
#         'n_estimators': [100, 200],
#         'max_depth': [5, 10, None],
#         'min_samples_split': [2, 10],
#         'min_samples_leaf': [1, 5],
#         'max_features': ['sqrt']
#     },
#     cv=TimeSeriesSplit(n_splits=5),
#     n_jobs=-1)
rf_regressor = RandomForestRegressor(max_depth=5, max_features='sqrt', min_samples_leaf=5, random_state=42)
result = train_evaluate_regression_model('Random Forest Regressor', rf_regressor)
print('R2 Score: ', result['R2 score'])
print('Mean Absolute Error: ', result['Mean Absolute Error'])
print('Mean Squared Error: ', result['Mean Squared Error'])
print('Root Mean Squared Error: ', result['Root Mean Squared Error'])

# Since decision tree performed the best now we will check which features are important
feature_importance_dict = dict()
for i in range(len(X_columns)):
    item = {
        X_columns[i]: dt_regressor.feature_importances_[i]
    }
    feature_importance_dict.update(item)
feature_importance_df = pd.DataFrame([feature_importance_dict], index=['Feature Importance'])
print(feature_importance_df.T.sort_values(by='Feature Importance', ascending=False))

# Classification:

# Logistic Regression accuracy ≈ 53.2%
# Decision Tree accuracy ≈ 53.3%
# Random Forest accuracy ≈ 48.7%
# Therefore, Decision Tree classifier performed slightly better.

# Regression:

# Linear Regression R² ≈ -0.009
# Decision Tree R² ≈ 0.023
# Random Forest R² ≈ -0.047
# Therefore, Decision Tree Regressor performed best among the three

# Now we will use deep learning to predict Tomorrow Return and for this purpose we will use LSTM
# first of all we will create X and y
window_size = 30
X = list()
y = list()
for i in range(window_size, len(df)):
    X.append(df[X_columns].iloc[i-window_size: i])
    y.append(df['Tomorrow Return'].iloc[i])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler_X = MinMaxScaler(feature_range=(0,1))
X_train = scaler_X.fit_transform(X_train.reshape(-1, X_train.shape[2]))
X_test = scaler_X.transform(X_test.reshape(-1, X_test.shape[2]))
X_train = X_train.reshape(-1, window_size, X_train.shape[1])
X_test = X_test.reshape(-1, window_size, X_test.shape[1])
scaler_y = MinMaxScaler(feature_range=(0,1))
y_train = scaler_y.fit_transform(y_train.reshape(-1,1))
y_test = scaler_y.transform(y_test.reshape(-1,1))

model = Sequential([
    LSTM(units=64, return_sequences=True, input_shape=(window_size, X_train.shape[2])),
    Dropout(0.3),
    LSTM(units=64),
    Dense(1, 'linear')
])
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])
history = model.fit(X_train, y_train, epochs=32, batch_size=32, validation_split=0.1, shuffle=False)
model.evaluate(X_test, y_test)
model.summary()

y_pred_scaled = model.predict(X_test)
y_pred = scaler_y.inverse_transform(y_pred_scaled)
y_test = scaler_y.inverse_transform(y_test)
print('R2 Score: ', r2_score(y_test, y_pred))
print('Mean Absolute Error: ', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error: ', mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred)))

# R2 Score:  -71.09289100413528
# Mean Absolute Error:  0.16521864846947593
# Mean Squared Error:  0.03588493264076096
# Root Mean Squared Error:  0.18943318780182358

plt.figure(figsize=(10,8))
plt.plot(y_test, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.show()

# Now we will use deep learning to predict Tomorrow Return and for this purpose we will use GRU
# first of all we will create X and y
window_size = 30
X = list()
y = list()
for i in range(window_size, len(df)):
    X.append(df[X_columns].iloc[i-window_size: i])
    y.append(df['Tomorrow Return'].iloc[i])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler_X = MinMaxScaler(feature_range=(0,1))
X_train = scaler_X.fit_transform(X_train.reshape(-1, X_train.shape[2]))
X_test = scaler_X.transform(X_test.reshape(-1, X_test.shape[2]))
X_train = X_train.reshape(-1, window_size, X_train.shape[1])
X_test = X_test.reshape(-1, window_size, X_test.shape[1])
scaler_y = MinMaxScaler(feature_range=(0,1))
y_train = scaler_y.fit_transform(y_train.reshape(-1,1))
y_test = scaler_y.transform(y_test.reshape(-1,1))

model = Sequential([
    GRU(units=64, return_sequences=True, input_shape=(window_size, X_train.shape[2])),
    Dropout(0.3),
    GRU(units=64),
    Dense(1, 'linear')
])
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])
history = model.fit(X_train, y_train, epochs=32, batch_size=32, validation_split=0.1, shuffle=False)
model.evaluate(X_test, y_test)
model.summary()

y_pred_scaled = model.predict(X_test)
y_pred = scaler_y.inverse_transform(y_pred_scaled)
y_test = scaler_y.inverse_transform(y_test)
print('R2 Score: ', r2_score(y_test, y_pred))
print('Mean Absolute Error: ', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error: ', mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error: ', np.sqrt(mean_squared_error(y_test, y_pred)))

# R2 Score:  -65.09289100413528
# Mean Absolute Error:  0.16521864846947593
# Mean Squared Error:  0.03588493264076096
# Root Mean Squared Error:  0.18943318780182358

plt.figure(figsize=(10,8))
plt.plot(y_test, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.show()

# # Now we will use deep learning to predict Up / Down and for this purpose we will use LSTM
X = list()
y = list()
for i in range(window_size, len(df)):
    X.append(df[X_columns].iloc[i-window_size: i])
    y.append(df['Up / Down'].iloc[i])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler_X = MinMaxScaler(feature_range=(0,1))
X_train = scaler_X.fit_transform(X_train.reshape(-1, X_train.shape[2]))
X_test = scaler_X.transform(X_test.reshape(-1, X_test.shape[2]))
X_train = X_train.reshape(-1, window_size, X_train.shape[1])
X_test = X_test.reshape(-1, window_size, X_test.shape[1])

model = Sequential([
    LSTM(units=64, return_sequences=True, input_shape=(window_size, X_train.shape[2])),
    Dropout(0.3),
    LSTM(units=64),
    Dense(1, 'sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=32, batch_size=32, validation_split=0.1, shuffle=False)
model.evaluate(X_test, y_test)
model.summary()
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob >= 0.5).astype(int).ravel()
print('Accuracy Score: ', accuracy_score(y_test, y_pred))
print('Confusion Matrix: ', confusion_matrix(y_test, y_pred))
print('Classification Report: ', classification_report(y_test, y_pred))

# Accuracy score: 47.02320

# # Now we will use deep learning to predict Up / Down and for this purpose we will use GRU
X = list()
y = list()
for i in range(window_size, len(df)):
    X.append(df[X_columns].iloc[i-window_size: i])
    y.append(df['Up / Down'].iloc[i])

X = np.array(X)
y = np.array(y)

split = int(len(X) * 0.8)
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

scaler_X = MinMaxScaler(feature_range=(0,1))
X_train = scaler_X.fit_transform(X_train.reshape(-1, X_train.shape[2]))
X_test = scaler_X.transform(X_test.reshape(-1, X_test.shape[2]))
X_train = X_train.reshape(-1, window_size, X_train.shape[1])
X_test = X_test.reshape(-1, window_size, X_test.shape[1])

model = Sequential([
    GRU(units=64, return_sequences=True, input_shape=(window_size, X_train.shape[2])),
    Dropout(0.3),
    GRU(units=64),
    Dense(1, 'sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=32, batch_size=32, validation_split=0.1, shuffle=False)
model.evaluate(X_test, y_test)
model.summary()
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob >= 0.5).astype(int).ravel()
print('Accuracy Score: ', accuracy_score(y_test, y_pred))
print('Confusion Matrix: ', confusion_matrix(y_test, y_pred))
print('Classification Report: ', classification_report(y_test, y_pred))

# Accuracy score: 49.02320

# Backtesting

X = df[X_columns]
y = df['Up / Down']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=False)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

dt_classifier = DecisionTreeClassifier(max_depth=15, min_samples_leaf=5, random_state=42)
dt_classifier.fit(X_train, y_train) 
y_pred = dt_classifier.predict(X_test)

backtesting_df = df.iloc[-len(X_test):,:]

backtesting_df['Prediction'] = 0

for i in range(len(backtesting_df)):
    backtesting_df['Prediction'].iloc[i] = y_pred[i]

# now we will calculate strategy return
backtesting_df['Strategy Return'] = 0
for i in range(len(backtesting_df)):
    if backtesting_df['Prediction'].iloc[i] == 1:
        backtesting_df['Strategy Return'].iloc[i] = backtesting_df['Tomorrow Return'].iloc[i]
    else:
        backtesting_df['Strategy Return'].iloc[i] = 0

print(backtesting_df['Strategy Return'])

# now we will calculate Cumulative Strategy Return
backtesting_df['Cumulative Strategy Return'] = np.cumprod(1 + backtesting_df['Strategy Return'])
print(backtesting_df['Cumulative Strategy Return'])

# now we will calculate Buy & Hold Return
backtesting_df['Cumulative Buy & Hold Return'] = np.cumprod(1 + backtesting_df['Tomorrow Return'])
print(backtesting_df['Cumulative Buy & Hold Return'])

# Decision Tree Strategy vs Buy & Hold
plt.figure(figsize=(10,6))
plt.plot(backtesting_df['Cumulative Strategy Return'])
plt.plot(backtesting_df['Cumulative Buy & Hold Return'])
plt.legend()
# plt.show()

# now we will calculate Sharpe Ratio
sharpe_ratio = ( backtesting_df['Strategy Return'].mean() / backtesting_df['Strategy Return'].std()) * np.sqrt(252) 
print(sharpe_ratio)

# now we will calculate Sortino Ratio
sortino_ratio = ( backtesting_df['Strategy Return'].mean() / backtesting_df['Strategy Return'].clip(upper=0).std()) * np.sqrt(252) 
print(sortino_ratio)

# now we will calculate Maximum Drawdown
running_max = backtesting_df['Cumulative Strategy Return'].cummax()
backtesting_df['Drawdown'] = (backtesting_df['Cumulative Strategy Return'] / running_max ) - 1
print(backtesting_df['Drawdown'].min())

# now we will calculate CAGR
total_trading_days = len(backtesting_df)
total_years = total_trading_days / 252
final_val =  backtesting_df['Cumulative Strategy Return'].iloc[-1]
cagr = (final_val ** (1/total_years)) - 1
print(cagr)

# Adobe

# Backtesting Results Explanation

# Strategy Return:

# The Decision Tree strategy increased the initial investment from 1 to approximately 4.54.
# This means that if we started with Rs. 100, it would become approximately Rs. 454
# during the backtesting period, assuming no transaction costs or other expenses.
# Therefore, the strategy generated a strong overall return.

# Buy & Hold Return:

# The Buy & Hold strategy increased the initial investment from 1 to approximately 3.72.
# This means that if we started with Rs. 100 and simply bought and held the stock,
# it would become approximately Rs. 372 during the same period.
# Since the Decision Tree strategy reached 4.54 while Buy & Hold reached 3.72,
# the Decision Tree strategy performed better in this backtest.

# Sharpe Ratio:

# Sharpe Ratio measures the return of the strategy compared with its overall risk.
# Our Sharpe Ratio is approximately 0.76.
# A positive Sharpe Ratio indicates that the strategy generated positive
# risk-adjusted performance.
# Higher Sharpe Ratio generally means better return for the amount of risk taken.

# Sortino Ratio:

# Sortino Ratio is similar to Sharpe Ratio, but it focuses mainly on downside risk.
# Our Sortino Ratio is approximately 1.19.
# This indicates that the strategy generated a positive return compared with
# the downside risk taken.
# Since the Sortino Ratio is higher than the Sharpe Ratio, the strategy's
# downside-risk-adjusted performance was relatively better.

# Maximum Drawdown:

# Maximum Drawdown measures the largest fall in the strategy value
# from a previous peak to a later lowest point.
# Our Maximum Drawdown is approximately -43.4%.
# This means that at its worst point, the strategy lost approximately 43.4%
# from its previous highest value.
# Therefore, although the strategy generated good returns, it also experienced
# a significant temporary decline and therefore involved considerable risk.

# CAGR:

# CAGR stands for Compound Annual Growth Rate.
# It shows the average yearly compounded growth of the strategy.
# Our CAGR is approximately 22.13%.
# This means that the strategy grew at an average componded annual rate
# of approximately 22.13% during the backtesting period.

# Overall Backtesting Conclusion:

# The Decision Tree strategy performed better than the Buy & Hold strategy
# based on the final cumulative return.
# The strategy achieved approximately 4.54 times the initial value,
# while Buy & Hold achieved approximately 3.72 times the initial value.
# The positive Sharpe Ratio of 0.76 and Sortino Ratio of 1.19
# indicate positive risk-adjusted performance.
# However, the Maximum Drawdown of approximately -43.4% shows that
# the strategy also experienced significant downside risk.
# Overall, the Decision Tree strategy showed better historical performance
# than Buy & Hold in this backtest, but the results also show that
# higher returns came with considerable risk.