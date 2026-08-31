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

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Telco-Customer-Churn.csv')
print(df.head())
print('*****************************************************')
print(df.shape)
print('*****************************************************')
print(df.columns)
print('*****************************************************')
print(df.dtypes)
print('*****************************************************')
print(df.info())
print('*****************************************************')
print(df.describe())
print('*****************************************************')
print(df.isnull().sum())
print('*****************************************************')
print(df.duplicated().sum())
print('*****************************************************')

columns = df.columns
for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print()
    print(f'{df[col].value_counts()}')
    print()
    print('**************************************')
    print()

# dropping customer id as it is unique for each customer
df.drop(columns='customerID', axis=1, inplace=True)
categorical_columns = ['gender','SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'Churn']
numerical_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']

# coverting object column into numeric column and then remove null values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
mean = round(df['TotalCharges'].mean(),2)
df['TotalCharges'] = df['TotalCharges'].fillna(mean)

# histplot for numerical columns
# for col in numerical_columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

# countplot for categorical columns
# for col in categorical_columns:
#     sns.countplot(data=df, x=col, hue='Churn')
#     plt.xticks(rotation=90)
#     plt.show()

# boxplot for numerical columns
# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# heatmap for numerical columns
# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

# label encoding
df['gender'] = df['gender'].map({
    'Male': 1,
    'Female': 0
})

df['Partner'] = df['Partner'].map({
    'Yes': 1,
    'No': 0
})

df['Dependents'] = df['Dependents'].map({
    'Yes': 1,
    'No': 0
})

df['PhoneService'] = df['PhoneService'].map({
    'Yes': 1,
    'No': 0
})

df['PaperlessBilling'] = df['PaperlessBilling'].map({
    'Yes': 1,
    'No': 0
})

df['Churn'] = df['Churn'].map({
    'Yes': 1,
    'No': 0
})

# one hot encoding
df = pd.get_dummies(df, 
                    columns=['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod'],
                    drop_first=True)

updated_columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'PhoneService', 'PaperlessBilling',
       'Churn', 'MultipleLines_No phone service', 'MultipleLines_Yes',
       'InternetService_Fiber optic', 'InternetService_No',
       'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
       'OnlineBackup_No internet service', 'OnlineBackup_Yes',
       'DeviceProtection_No internet service', 'DeviceProtection_Yes',
       'TechSupport_No internet service', 'TechSupport_Yes',
       'StreamingTV_No internet service', 'StreamingTV_Yes',
       'StreamingMovies_No internet service', 'StreamingMovies_Yes',
       'Contract_One year', 'Contract_Two year',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']

df[updated_columns] = df[updated_columns].astype(int)

# pearson correlation for numerical columns

pearson_corr_list = list()
for col in numerical_columns:
    pearson_corr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['Churn'])
    pearson_corr_dict['Feature Name'] = col
    pearson_corr_dict['Correlation Coefficient'] = corr_coef
    pearson_corr_dict['P Value'] = p_val
    pearson_corr_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    pearson_corr_list.append(pearson_corr_dict)

pearson_corr_df = pd.DataFrame(pearson_corr_list)
print(pearson_corr_df)

# chi2 test for categorical columns

chi2_list = list()
for col in updated_columns:
    chi2_dict = dict()
    contingency_table = pd.crosstab(df[col], df['Churn'])
    chi2_val, p_val, x, y = chi2_contingency(contingency_table)
    chi2_dict['Feature Name'] = col
    chi2_dict['Chi2 Value'] = chi2_val
    chi2_dict['P Value'] = p_val
    chi2_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    chi2_list.append(chi2_dict)

chi2_df = pd.DataFrame(chi2_list)
print(chi2_df)

X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)
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