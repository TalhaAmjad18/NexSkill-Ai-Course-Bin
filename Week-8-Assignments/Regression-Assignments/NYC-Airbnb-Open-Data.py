import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr, chi2_contingency
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from math import sqrt
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb

df = pd.read_csv(r'Week-8-Assignments/Regression-Assignments/NYC-Airbnb-Open-Data.csv', parse_dates=['last_review'])
print(df.head())
print('**************************************************************')
print(df.shape)
print('**************************************************************')
print(df.columns)
print('**************************************************************')
print(df.dtypes)
print('**************************************************************')
print(df.info())
print('**************************************************************')
print(df.describe())
print('**************************************************************')
print(df.isnull().sum())
print('**************************************************************')
print(df.duplicated().sum())
print('**************************************************************')

columns = df.columns
for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print()
    print(f'{df[col].value_counts()}')
    print()
    print('*********************************************')
    print()

# drop id, name, host_id, host_name, last_review

categorical_columns = ['neighbourhood_group', 'neighbourhood', 'room_type']
numerical_columns = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']

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
#     sns.regplot(data=df, x=col, y='price')
#     plt.show()

df.drop(columns=['id', 'name', 'host_id', 'host_name', 'last_review'], inplace=True)

df['reviews_per_month'] = df['reviews_per_month'].fillna(
    df['reviews_per_month'].median()
)

print(df.isnull().sum())

median_price = df.loc[df['price'] != 0, 'price'].median()

df['price'] = df['price'].replace(0, median_price)

df = pd.get_dummies(df, columns=['neighbourhood_group', 'neighbourhood', 'room_type'], drop_first=True, dtype=int)

Q1 = np.percentile(df['price'], 25)
Q3 = np.percentile(df['price'], 75)
IQR = Q3 - Q1
UF = Q3 + 1.5 * IQR
LF = Q1 - 1.5 * IQR
df.loc[(df['price'] < LF) | (df['price'] > UF), 'price'] = df.loc[~(df['price'] < LF) | (df['price'] > UF), 'price'].median()

updated_categorical_columns = list()

for col in df.columns:
    if col not in numerical_columns:
        updated_categorical_columns.append(col)

pearsonr_list = list()
for col in numerical_columns:
    pearsonr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['price'])
    pearsonr_dict['name'] = col
    pearsonr_dict['correlation coefficient'] = corr_coef
    pearsonr_dict['p values'] = p_val
    pearsonr_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
    pearsonr_list.append(pearsonr_dict)

pearsonr_df = pd.DataFrame(pearsonr_list)
print(pearsonr_df)

# we will keep all the features

# df['price'] = pd.qcut(df['price'], q=4, labels=False)
# chi2_list = list()
# for col in updated_categorical_columns:
#     chi2_dict = dict()
#     contingency_table = pd.crosstab(df[col], df['price'])
#     chi2_val, p_val, a, b = chi2_contingency(contingency_table)
#     chi2_dict['name'] = col
#     chi2_dict['correlation coefficient'] = chi2_val
#     chi2_dict['p values'] = p_val
#     chi2_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
#     chi2_list.append(chi2_dict)

# chi2_df = pd.DataFrame(chi2_list)
# print(chi2_df.to_string())

dropped_columns = [
'neighbourhood_Arden Heights','neighbourhood_Arverne','neighbourhood_Bay Terrace','neighbourhood_Bay Terrace, Staten Island','neighbourhood_Baychester','neighbourhood_Bayswater','neighbourhood_Belle Harbor',  'neighbourhood_Bellerose', 'neighbourhood_Bergen Beach','neighbourhood_Castleton Corners',  'neighbourhood_City Island','neighbourhood_Clason Point',  'neighbourhood_Clifton','neighbourhood_Co-op City',  'neighbourhood_Coney Island',   'neighbourhood_Dongan Hills', 'neighbourhood_Douglaston', 'neighbourhood_Dyker Heights','neighbourhood_East Morrisania','neighbourhood_Eastchester','neighbourhood_Edgemere','neighbourhood_Eltingville','neighbourhood_Emerson Hill','neighbourhood_Fieldston','neighbourhood_Fort Wadsworth','neighbourhood_Graniteville','neighbourhood_Grant City','neighbourhood_Great Kills','neighbourhood_Grymes Hill','neighbourhood_Hollis','neighbourhood_Holliswood','neighbourhood_Howard Beach','neighbourhood_Howland Hook','neighbourhood_Huguenot','neighbourhood_Jamaica Estates','neighbourhood_Jamaica Hills']

df.drop(columns=dropped_columns, inplace=True)

X = df.drop(columns = 'price')
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

# bagging

# random_forest_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
# random_forest_regressor.fit(X_train, y_train)
# y_pred = random_forest_regressor.predict(X_test)
# print('r2 score: ', r2_score(y_test, y_pred))
# print('mean absolute error: ', mean_absolute_error(y_test, y_pred))
# print('mean squared error: ', mean_squared_error(y_test, y_pred))
# print('root mean squared error: ', sqrt(mean_squared_error(y_test, y_pred)))

# stacking

# base_learners = [
#     ('linear_regressor', LinearRegression()),
#     ('decision_tree_regressor', DecisionTreeRegressor(random_state=42)),
#     ('svm_regressor', SVR(kernel='rbf'))
# ]

# meta_learner = KNeighborsRegressor(n_neighbors=5)

# stacking_clf = StackingRegressor(
#     estimators=base_learners,
#     final_estimator=meta_learner,
#     cv=5
# )

# stacking_clf.fit(X_train, y_train)
# stacking_clf_y_pred = stacking_clf.predict(X_test)
# print('r2 score: ', r2_score(y_test, stacking_clf_y_pred))
# print('mean absolute error: ', mean_absolute_error(y_test, stacking_clf_y_pred))
# print('mean squared error: ', mean_squared_error(y_test, stacking_clf_y_pred))
# print('root mean squared error: ', sqrt(mean_squared_error(y_test, stacking_clf_y_pred)))

# boosting

# ada_boost_regressor = AdaBoostRegressor()
# ada_boost_regressor.fit(X_train,y_train)
# ada_boost_regressor_y_pred = ada_boost_regressor.predict(X_test)
# print('r2 score: ', r2_score(y_test, ada_boost_regressor_y_pred))
# print('mean absolute error: ', mean_absolute_error(y_test, ada_boost_regressor_y_pred))
# print('mean squared error: ', mean_squared_error(y_test, ada_boost_regressor_y_pred))
# print('root mean squared error: ', sqrt(mean_squared_error(y_test, ada_boost_regressor_y_pred)))
# ada_boost_regressor = AdaBoostRegressor()

# gradient_boosting_regressor = GradientBoostingRegressor()
# gradient_boosting_regressor.fit(X_train,y_train)
# gradient_boosting_regressor_y_pred = gradient_boosting_regressor.predict(X_test)
# print('r2 score: ', r2_score(y_test, gradient_boosting_regressor_y_pred))
# print('mean absolute error: ', mean_absolute_error(y_test, gradient_boosting_regressor_y_pred))
# print('mean squared error: ', mean_squared_error(y_test, gradient_boosting_regressor_y_pred))
# print('root mean squared error: ', sqrt(mean_squared_error(y_test, gradient_boosting_regressor_y_pred)))

xgb_regressor = xgb.XGBRegressor()
xgb_regressor.fit(X_train, y_train)
xgb_regressor_y_pred = xgb_regressor.predict(X_test)
print('r2 score: ', r2_score(y_test, xgb_regressor_y_pred))
print('mean absolute error: ', mean_absolute_error(y_test, xgb_regressor_y_pred))
print('mean squared error: ', mean_squared_error(y_test, xgb_regressor_y_pred))
print('root mean squared error: ', sqrt(mean_squared_error(y_test, xgb_regressor_y_pred)))