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

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Heart-Disease-UCI.csv')
print(df.head())
print('***************************************************************************')
print(df.shape)
print('***************************************************************************')
print(df.columns)
print('***************************************************************************')
print(df.dtypes)
print('***************************************************************************')
print(df.info())
print('***************************************************************************')
print(df.describe())
print('***************************************************************************')
print(df.isnull().sum())
print('***************************************************************************')
print(df.duplicated().sum())
print('***************************************************************************')

columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'condition']
for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print(df[col].value_counts())
    print('************************************************************************')

numerical_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, kde=True)
#     plt.show()

# for col in categorical_columns:
#     sns.countplot(data=df, x=col, hue='condition')
#     plt.show()

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df[numerical_columns].corr(), annot=True)
# plt.show()

pearsonr_list = list()
for col in numerical_columns:
    pearsonr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['condition'])
    pearsonr_dict['name'] = col
    pearsonr_dict['corr coef'] = corr_coef
    pearsonr_dict['p value'] = p_val
    pearsonr_dict['decision'] = 'keep feature' if 0.05 > p_val else 'drop feature'
    pearsonr_list.append(pearsonr_dict)

pearsonr_df = pd.DataFrame(pearsonr_list)
print(pearsonr_df)

chi2_list = list()
for col in categorical_columns:
    chi2_dict = dict()
    contingency_table = pd.crosstab(df[col], df['condition'])
    chi2_val, p_val, x, y = chi2_contingency(contingency_table)
    chi2_dict['name'] = col
    chi2_dict['corr coef'] = chi2_val
    chi2_dict['p value'] = p_val
    chi2_dict['decision'] = 'keep feature' if 0.05 > p_val else 'drop feature'
    chi2_list.append(chi2_dict)

chi2_df = pd.DataFrame(chi2_list)
print(chi2_df)

# nothing will drop
X = df.drop('condition', axis=1)
y = df['condition']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

columns = ['age', 'cp', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']
scaler = StandardScaler()
X_train[columns] = scaler.fit_transform(X_train[columns])
X_test[columns] = scaler.transform(X_test[columns])

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



















