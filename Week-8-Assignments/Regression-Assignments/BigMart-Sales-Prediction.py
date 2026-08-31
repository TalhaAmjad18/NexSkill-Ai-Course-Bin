import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr, chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
from sklearn.ensemble import StackingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from math import sqrt

df = pd.read_csv(r'Week-8-Assignments/Regression-Assignments/BigMart-Sales-Prediction.csv')

print(df.head())
print('*******************************************************************')
print(df.shape)
print('*******************************************************************')
print(df.columns)
print('*******************************************************************')
print(df.dtypes)
print('*******************************************************************')
print(df.describe())
print('*******************************************************************')
print(df.info())
print('*******************************************************************')
print(df.isnull().sum())
print('*******************************************************************')
print(df.duplicated().sum())
print('*******************************************************************')

# for col in df.columns:
#     print(f'{col}: {df[col].nunique()}')
#     print()
#     print(f'{df[col].value_counts()}')
#     print()
#     print('****************************************')

categorical_columns = ['Item_Identifier', 'Item_Fat_Content', 'Item_Type', 'Outlet_Identifier', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']
numerical_columns = ['Item_Weight', 'Item_Visibility', 'Item_MRP']
date_column = 'Outlet_Establishment_Year'

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

# for col in categorical_columns:
#     sns.countplot(data=df, x=col)
#     plt.show()

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

# for col in numerical_columns:
#     sns.regplot(data=df, x=col, y='Item_Outlet_Sales')
#     plt.show()

# sns.lineplot(data=df, x=date_column, y='Item_Outlet_Sales')
# plt.show()

print(df.loc[df['Item_Visibility'] == 0, 'Item_Visibility'].count())    # contains 0 values
print(df.loc[df['Item_Outlet_Sales'] == 0, 'Item_Outlet_Sales'].count())

df['Item_Weight'] = df['Item_Weight'].fillna(
    df['Item_Weight'].mean()
) 

df['Outlet_Size'] = df['Outlet_Size'].fillna(
    df['Outlet_Size'].mode()[0]
)

print(df.isnull().sum())

median_item_visibility = df.loc[df['Item_Visibility'] != 0, 'Item_Visibility'].median()
df['Item_Visibility'] = df['Item_Visibility'].replace(
    0, median_item_visibility
)

for col in categorical_columns:
    print(f'{col}: {df[col].nunique()}')
    print()
    print(f'{df[col].value_counts()}')
    print()
    print('****************************************')

df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})

print(df['Item_Fat_Content'].unique())

df['Item_Fat_Content'] = df['Item_Fat_Content'].map({
    'Low Fat': 0,
    'Regular': 1
})

df['Outlet_Age'] = 2013 - df['Outlet_Establishment_Year']

numerical_columns.append('Outlet_Age')

df.drop(columns=['Item_Identifier', 'Outlet_Identifier', date_column], inplace=True)

df = pd.get_dummies(df, columns=['Item_Type','Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type'], drop_first=True, dtype=int)

print(df.head())

updated_categorical_columns = list()

for col in df.columns:
    if col not in numerical_columns:
        updated_categorical_columns.append(col)

pearson_list = list()
for col in numerical_columns:
    pearson_dict = dict()
    corr_coref, p_val = pearsonr(df[col], df['Item_Outlet_Sales'])
    pearson_dict['col'] = col
    pearson_dict['corr coef'] = corr_coref
    pearson_dict['p val'] = p_val
    pearson_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
    pearson_list.append(pearson_dict)

pearson_df = pd.DataFrame(pearson_list)
print(pearson_df)

# df['Item_Outlet_Sales'] = pd.qcut(df['Item_Outlet_Sales'], q=4, labels=False)
# chi2_list = list()
# for col in updated_categorical_columns:
#     chi2_dict = dict()
#     contingency_table = pd.crosstab(df[col], df['Item_Outlet_Sales'])
#     chi2_val, p_val, a, b = chi2_contingency(contingency_table)
#     chi2_dict['col'] = col
#     chi2_dict['corr coef'] = chi2_val
#     chi2_dict['p val'] = p_val
#     chi2_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
#     chi2_list.append(chi2_dict)

# chi2_df = pd.DataFrame(chi2_list)
# print(chi2_df)

X = df.drop(columns='Item_Outlet_Sales')
y = df['Item_Outlet_Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

models = {
    'random forest': GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid={
        'n_estimators': [10, 50, 100]
    }, cv=5),
    'ada boost': GridSearchCV(estimator=AdaBoostRegressor(random_state=42), param_grid={
        'n_estimators': [10, 50, 100],
        'learning_rate': [0.1, 1, 10]
    }, cv=5),
    'gradient boost': GridSearchCV(estimator=GradientBoostingRegressor(random_state=42), param_grid={
        'n_estimators': [10, 50, 100],
        'learning_rate': [0.1, 1, 10]
    }, cv=5),
    'xgb': GridSearchCV(estimator=xgb.XGBRegressor(random_state=42), param_grid={
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.05, 0.1, 1]
    }, cv=5)
} 

for key, val in models.items():
    model = val
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print('model name:', key)
    print('r2 score: ', r2_score(y_test, y_pred))
    print('mean absolute error: ', mean_absolute_error(y_test, y_pred))
    print('mean squared error: ', mean_squared_error(y_test, y_pred))
    print('root mean squared error: ', sqrt(mean_squared_error(y_test, y_pred)))

ada_boost_regressor = GridSearchCV(estimator=AdaBoostRegressor(random_state=42), param_grid={
            'n_estimators': [10, 50, 100],
            'learning_rate': [0.01, 0.05, 0.1]
},cv=5)
ada_boost_regressor.fit(X_train,y_train)
gradient_boost_regressor = GridSearchCV(estimator=GradientBoostingRegressor(random_state=42), param_grid={
            'n_estimators': [10, 50, 100],
            'learning_rate': [0.01, 0.05, 0.1]
}, cv=5)
gradient_boost_regressor.fit(X_train,y_train)
xgb_regressor = GridSearchCV(estimator=xgb.XGBRegressor(random_state=42), param_grid={
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.01, 0.05, 0.1]
}, cv=5)
xgb_regressor.fit(X_train,y_train)
rfr = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid={'n_estimators': [10, 50, 100]}, cv=5)
rfr.fit(X_train,y_train)
base_models = [
    ('ada',ada_boost_regressor.best_estimator_),
    ('gradient',gradient_boost_regressor.best_estimator_),
    ('xgb',xgb_regressor.best_estimator_)
]
meta_model = rfr.best_estimator_
stacking_regressor = StackingRegressor(estimators=base_models,
                                       final_estimator=meta_model,
                                       cv=5)

stacking_regressor.fit(X_train, y_train)
y_pred = stacking_regressor.predict(X_test)
print('r2 score: ', r2_score(y_test, y_pred))
print('mean absolute error: ', mean_absolute_error(y_test, y_pred))
print('mean squared error: ', mean_squared_error(y_test, y_pred))
print('root mean squared error: ', sqrt(mean_squared_error(y_test, y_pred)))