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

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Bank-Marketing.csv')
print(df.head())
print('******************************************************************')
print(df.shape)
print('******************************************************************')
print(df.columns)
print('******************************************************************')
print(df.dtypes)
print('******************************************************************')
print(df.isnull().sum())
print('******************************************************************')
print(df.duplicated().sum())
print('******************************************************************')

columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
       'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
       'previous', 'poutcome', 'deposit']

for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print()
    print(f'{df[col].value_counts()}')
    print()
    print('*******************************')
    print()

numerical_columns = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'deposit']

# label encode -> default, housing, loan, deposit
# job, education, contact, poutcome contains unknown
# balance is in negative
# pdays contain -1

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

# for col in categorical_columns:
#     sns.countplot(data=df, x=col, hue='deposit')
#     plt.xticks(rotation=90)
#     plt.show()

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

# label encoding
df['default'] = df['default'].map({
    'yes': 1,
    'no': 0
})
df['housing'] = df['housing'].map({
    'yes': 1,
    'no': 0
})
df['loan'] = df['loan'].map({
    'yes': 1,
    'no': 0
})
df['deposit'] = df['deposit'].map({
    'yes': 1,
    'no': 0
})

# one hot encode

df = pd.get_dummies(df, 
                    columns= ['job', 'marital', 'education', 'contact', 'month', 'poutcome'],
                    drop_first=True)

updated_categorical_columns = ['default', 'housing', 'loan', 'deposit', 'job_blue-collar',
       'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
       'job_self-employed', 'job_services', 'job_student', 'job_technician',
       'job_unemployed', 'job_unknown', 'marital_married', 'marital_single',
       'education_secondary', 'education_tertiary', 'education_unknown',
       'contact_telephone', 'contact_unknown', 'month_aug', 'month_dec',
       'month_feb', 'month_jan', 'month_jul', 'month_jun', 'month_mar',
       'month_may', 'month_nov', 'month_oct', 'month_sep', 'poutcome_other',
       'poutcome_success', 'poutcome_unknown']

df[updated_categorical_columns] = df[updated_categorical_columns].astype(int)

print(df.head())


pearson_corr_list = list()
for col in numerical_columns:
    pearson_corr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['deposit'])
    pearson_corr_dict['Feature Name'] = col
    pearson_corr_dict['Correlation Coefficient'] = corr_coef
    pearson_corr_dict['P Value'] = p_val
    pearson_corr_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    pearson_corr_list.append(pearson_corr_dict)

pearson_corr_df = pd.DataFrame(pearson_corr_list)
print(pearson_corr_df)

chi2_list = list()
for col in updated_categorical_columns:
    chi2_dict = dict()
    contingency_table = pd.crosstab(df[col], df['deposit'])
    chi2_val, p_val, x, y = chi2_contingency(contingency_table)
    chi2_dict['Feature Name'] = col
    chi2_dict['Chi2 Value'] = chi2_val
    chi2_dict['P Value'] = p_val
    chi2_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    chi2_list.append(chi2_dict)

chi2_df = pd.DataFrame(chi2_list)
print(chi2_df)

df.drop(columns=['job_self-employed', 'job_technician', 'job_unknown', 'education_unknown', 'contact_telephone', 'month_aug'],
        axis=1, inplace=True)

print(df.head())

X = df.drop(columns='deposit')
y = df['deposit']
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