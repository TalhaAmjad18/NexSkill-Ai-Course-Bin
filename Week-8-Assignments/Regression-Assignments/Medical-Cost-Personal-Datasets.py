import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr, chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import sqrt

df = pd.read_csv(r'Week-8-Assignments/Regression-Assignments/Medical-Cost-Personal-Datasets.csv')

print(df.head())
print('***************************************************************')
print(df.shape)
print('***************************************************************')
print(df.columns)
print('***************************************************************')
print(df.dtypes)
print('***************************************************************')
print(df.describe())
print('***************************************************************')
print(df.info())
print('***************************************************************')
print(df.isnull().sum())
print('***************************************************************')
print(df.duplicated().sum())
print('***************************************************************')

# for col in df.columns:
#     print(f'{col}: {df[col].nunique()}')
#     print()
#     print(f'{df[col].value_counts()}')
#     print()
#     print('*****************************************************')
#     print()

numerical_columns = ['age', 'bmi', 'children']
categorical_columns = ['sex', 'smoker', 'region']

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
#     sns.regplot(data=df, x=col, y='charges')
#     plt.show()

df.drop_duplicates(inplace=True)

df['sex'] = df['sex'].map({
    'female': 0,
    'male': 1,
})

df['smoker'] = df['smoker'].map({
    'no': 0,
    'yes': 1,
})

df = pd.get_dummies(df, columns=['region'], drop_first=True, dtype=int)

df['bmi_category'] = pd.cut(df['bmi'],
                            bins=[0,18.5,24.9,29.9,49.9],
                            labels=['underweight','healthy weight','overweight','obese'])

df = pd.get_dummies(df, columns=['bmi_category'], drop_first=True, dtype=int)

print(df.head())

updated_categorical_columns = list()
for col in df.columns:
    if col not in numerical_columns:
        updated_categorical_columns.append(col)

pearsonr_list = list()
for col in numerical_columns:
    pearsonr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['charges'])
    pearsonr_dict['name'] = col
    pearsonr_dict['corr coef'] = corr_coef
    pearsonr_dict['p val'] = p_val
    pearsonr_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
    pearsonr_list.append(pearsonr_dict)

pearsonr_df = pd.DataFrame(pearsonr_list)
print(pearsonr_df) # keep all values

# df['charges'] = pd.qcut(df['charges'], q=4, labels=False)
# chi2_list = list()
# for col in updated_categorical_columns:
#     chi2_dict = dict()
#     contingency_table = pd.crosstab(df[col], df['charges'])
#     chi2_val, p_val, a, b = chi2_contingency(contingency_table)
#     chi2_dict['name'] = col
#     chi2_dict['chi2 val'] = chi2_val
#     chi2_dict['p val'] = p_val
#     chi2_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
#     chi2_list.append(chi2_dict)

# chi2_df = pd.DataFrame(chi2_list)
# print(chi2_df)
df.drop(columns=['region_northwest', 'region_southwest', 'bmi_category_healthy weight', 'bmi_category_overweight'], inplace=True)
print(df.head())

X = df.drop(columns='charges')
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

models = {
    'random forest': RandomForestRegressor(random_state=42),
    'ada boost': AdaBoostRegressor(),
    'gradient boost': GradientBoostingRegressor(),
    'xgb': XGBRegressor()
}

for key, val in models.items():
    model = val
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print('model name: ', key)
    print('r2 score: ', r2_score(y_test, y_pred))
    print('mean absolute error: ', mean_absolute_error(y_test, y_pred))
    print('mean squared error: ', mean_squared_error(y_test, y_pred))
    print('root mean squared error: ', sqrt(mean_squared_error(y_test, y_pred)))