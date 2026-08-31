import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr, chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Adult-Census-Income.csv', delimiter=',')
print(df.head())
print('*************************************************************')
print(df.shape)
print('*************************************************************')
print(df.columns)
print('*************************************************************')
print(df.dtypes)
print('*************************************************************')
print(df.info())
print('*************************************************************')
print(df.describe())
print('*************************************************************')
print(df.isnull().sum())
print('*************************************************************')
print(df.duplicated().sum())
print('*************************************************************')

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education.num',
       'marital.status', 'occupation', 'relationship', 'race', 'sex',
       'capital.gain', 'capital.loss', 'hours.per.week', 'native.country',
       'income']

for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print()
    print(f'{df[col].value_counts()}')
    print()
    print('*****************************')

numerical_columns = ['age', 'fnlwgt', 'education.num', 'capital.gain', 'capital.loss', 'hours.per.week']
categorical_columns = ['workclass', 'education', 'marital.status', 'occupation', 'relationship', 'race', 'sex', 'native.country', 'income']

# workclass, occupation, native.country -> they include ?

# histplot for numerical columns

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, kde=True, bins=20)
#     plt.show()

# countplot for categorical columns

# for col in categorical_columns:
#     sns.countplot(data=df, x=col, hue='income')
#     plt.xticks(rotation=90)
#     plt.show()

# boxplot for numerical columns

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

df_cleaned = df.copy()

df_cleaned.rename(columns={
    'education.num': 'education_num',
    'marital.status': 'marital_status',
    'capital.gain': 'capital_gain',
    'capital.loss': 'capital_loss',
    'hours.per.week': 'hours_per_week',
    'native.country': 'native_country'
}, inplace=True)

df_cleaned.drop_duplicates(inplace=True)
work_class = df_cleaned.loc[df_cleaned['workclass'] != '?' , 'workclass'].mode()[0]
df_cleaned['workclass'].replace('?', work_class, inplace=True)
occupation = df_cleaned.loc[df_cleaned['occupation'] != '?' , 'occupation'].mode()[0]
df_cleaned['occupation'].replace('?', occupation, inplace=True)
native_country = df_cleaned.loc[df_cleaned['native_country'] != '?' , 'native_country'].mode()[0]
df_cleaned['native_country'].replace('?', native_country, inplace=True)

print(df_cleaned.head())

print(df_cleaned.columns)

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
       'marital_status', 'occupation', 'relationship', 'race', 'sex',
       'capital_gain', 'capital_loss', 'hours_per_week', 'native_country',
       'income']

numerical_columns = ['age', 'fnlwgt', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
categorical_columns = ['workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'income']

# for col in categorical_columns:
#     sns.countplot(data=df_cleaned, x=col, hue='income')
#     plt.xticks(rotation=90)
#     plt.show()

df_cleaned['sex'] = df_cleaned['sex'].map({
    'Male': 1,
    'Female': 0
})

df_cleaned['income'] = df_cleaned['income'].map({
    '<=50K': 0,
    '>50K': 1
})

df_cleaned = pd.get_dummies(df_cleaned, 
                            columns=  ['workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'native_country'],
                            drop_first=True)

X = df_cleaned.drop(columns='income')
y = df_cleaned['income']

updated_columns = list()
for col in X.columns.to_list():
    if col not in numerical_columns:
        updated_columns.append(col)

X[updated_columns] = X[updated_columns].astype(int)
print(X.head())

# for numerical column we are performing pearson correlation
pearsonr_list = list()
for col in numerical_columns:
    pearsonr_dict = dict()
    corr_coef, p_val = pearsonr(X[col], y)
    pearsonr_dict['name'] = col
    pearsonr_dict['corr coef'] = corr_coef
    pearsonr_dict['p val'] = p_val
    pearsonr_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
    pearsonr_list.append(pearsonr_dict)

pearsonr_df = pd.DataFrame(pearsonr_list)
print(pearsonr_df)

# for categorical column we are performing chi2 test
chi2_list = list()
for col in updated_columns:
    chi2_dict = dict()
    contingency_table = pd.crosstab(X[col],y)
    chi2_val, p_val, a, b = chi2_contingency(contingency_table)
    chi2_dict['name'] = col
    chi2_dict['chi2 val'] = chi2_val
    chi2_dict['p val'] = p_val
    chi2_dict['decision'] = 'keep' if 0.05 > p_val else 'drop'
    chi2_list.append(chi2_dict)

chi2_df = pd.DataFrame(chi2_list)
print(chi2_df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
scaler = StandardScaler()
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

models_dict = {
    'LogisticRegression': LogisticRegression(),
    'K Nearest Neighbour': KNeighborsClassifier(n_neighbors=5),
    'Naive Bayes': GaussianNB(),
    'Decision Tree': DecisionTreeClassifier(),
    'Support Vector Machine': SVC()
}

for key, val in models_dict.items():
    model = val
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print(key)
    print(accuracy_score(y_test,y_pred))
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    print('********************************************************************')

useful_columns = list()
useful_columns.extend(numerical_columns)
for row in chi2_list:
    if row['decision'] == 'keep':
        useful_columns.append(row['name'])

print(useful_columns)

new_input = df_cleaned[useful_columns]
new_output = df_cleaned['income']
X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(new_input, new_output, test_size=0.20, random_state=42, stratify=new_output)
scaler = StandardScaler()
X_train_new[numerical_columns] = scaler.fit_transform(X_train_new[numerical_columns])
X_test_new[numerical_columns] = scaler.transform(X_test_new[numerical_columns])

models_dict = {
    'LogisticRegression': LogisticRegression(),
    'K Nearest Neighbour': KNeighborsClassifier(n_neighbors=5),
    'Naive Bayes': GaussianNB(),
    'Decision Tree': DecisionTreeClassifier(),
    'Support Vector Machine': SVC()
}

for key, val in models_dict.items():
    model = val
    model.fit(X_train_new,y_train_new)
    y_pred = model.predict(X_test_new)
    print(key)
    print(accuracy_score(y_test_new,y_pred))
    print(confusion_matrix(y_test_new,y_pred))
    print(classification_report(y_test_new,y_pred))
    print('********************************************************************')
