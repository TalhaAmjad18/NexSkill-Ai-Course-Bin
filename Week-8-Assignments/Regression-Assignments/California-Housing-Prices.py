import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr, chi2_contingency
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from math import sqrt

df = pd.read_csv(r'Week-8-Assignments/Regression-Assignments/California-Housing-Prices.csv')
print(df.head())
print('*****************************************************************')
print(df.shape)
print('*****************************************************************')
print(df.columns)
print('*****************************************************************')
print(df.dtypes)
print('*****************************************************************')
print(df.describe())
print('*****************************************************************')
print(df.info())
print('*****************************************************************')
print(df.isnull().sum())
print('*****************************************************************')
print(df.duplicated().sum())
print('*****************************************************************')

columns = df.columns
# for col in columns:
#     print(f'{col}: {df[col].nunique()}')
#     print('')
#     print(f'{df[col].value_counts()}')
#     print('')
#     print('****************************************************')
#     print('')

numerical_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income']

# ocean_proximity is only categorical column

# histplot for numerical columns

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, kde=True, bins=20)
#     plt.show()

# countplot for categorical column

# sns.countplot(data=df, x='ocean_proximity')
# plt.show()

# boxplot for numerical columns

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# heatmap for numerical column

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

# regplot for confirming regression

# for col in numerical_columns:
#     sns.regplot(data=df, x=col, y='median_house_value')
#     plt.show()

# since total_bedrooms has many outliers, we will fill null values with median

df['total_bedrooms'].fillna(df['total_bedrooms'].median(), inplace=True)

print(df['total_bedrooms'].isnull().sum())

print(df['ocean_proximity'].value_counts()) # 5 categories so we will use one hot encoding

df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True)

print(df.columns)

categoical_columns = ['ocean_proximity_INLAND',
       'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY',
       'ocean_proximity_NEAR OCEAN']
df[categoical_columns] = df[categoical_columns].astype(int)

print(df.head()) 

# pearson correlation for numerical columns

pearsonr_list = list()
for col in numerical_columns:
    pearsonr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['median_house_value'])
    pearsonr_dict['name'] = col
    pearsonr_dict['correlation coefficient'] = corr_coef
    pearsonr_dict['p value'] = p_val
    pearsonr_dict['result'] = 'keep' if 0.05 > p_val else 'drop'
    pearsonr_list.append(pearsonr_dict)

pearsonr_df = pd.DataFrame(pearsonr_list)
print(pearsonr_df)

# we will keep all the features

# chi2 test for categorical columns

# first we will convert out target numerical column into a category
# df['median_house_value'] = pd.qcut(df['median_house_value'], q=4, labels=False)
# chi2_list = list()
# for col in categoical_columns:
#     chi2_dict = dict()
#     contingency_table = pd.crosstab(df[col], df['median_house_value'])
#     chi2_val, p_val, a, b = chi2_contingency(contingency_table)
#     chi2_dict['name'] = col
#     chi2_dict['chi2 value'] = chi2_val
#     chi2_dict['p value'] = p_val
#     chi2_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
#     chi2_list.append(chi2_dict)

# chi2_df = pd.DataFrame(chi2_list)
# print(chi2_df)

# we will keep all the features

X = df.drop(columns = 'median_house_value')
y = df['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

def function(model, regressor):
    print(f'Model name is: {model}')
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    print(f'R2 Score: {r2_score(y_test, y_pred)}')
    print(f'Mean squared error: {mean_squared_error(y_test, y_pred)}')
    print(f'Mean absolute error: {mean_absolute_error(y_test, y_pred)}')
    print(f'Root mean squared error: {sqrt(mean_squared_error(y_test, y_pred))}')
    print()
    print('***************************************************************')
    print()

linear_regressor = LinearRegression()
function('Linear regression', linear_regressor)

lasso_regressor = GridSearchCV(estimator=Lasso(), param_grid={
    'alpha': [0.01, 0.1, 1, 10, 100]
}, cv=5)
function('Lasso Regression', lasso_regressor)

ridge_regressor = GridSearchCV(estimator=Ridge(), param_grid={
    'alpha': [0.01, 0.1, 1, 10, 100]
}, cv=5)
function('Ridge Regression', ridge_regressor)

decision_tree_regressor = GridSearchCV(estimator=DecisionTreeRegressor(), param_grid={
    'criterion': ['squared_error', 'absolute_error'],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}, cv=5)
function('Decision Tree Regression', decision_tree_regressor)

random_forest_regressor = GridSearchCV(estimator=RandomForestRegressor(), param_grid={
    'n_estimators': [10,100,200],
    'criterion': ['squared_error', 'absolute_error']
}, cv=5)
function('Random Forest Regression', random_forest_regressor)