import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Pima-Indians-Diabetes.csv')
print(df.head())
print('******************************************************************')
print(df.shape)
print('******************************************************************')
print(df.columns)
print('******************************************************************')
print(df.dtypes)
print('******************************************************************')
print(df.info())
print('******************************************************************')
print(df.describe())
print('******************************************************************')
print(df.isnull().sum())
print('******************************************************************')
print(df.duplicated().sum())
print('******************************************************************')

columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']

for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print()
    print()
    print('*****************************')
    print()
    print()

# All columns are numerical columns so we will make histplot

# for col in columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

print('Pregnancies',df[df['Pregnancies'] == 0]['Pregnancies'].count())
print('Glucose',df[df['Glucose'] == 0]['Glucose'].count())
print('BloodPressure',df[df['BloodPressure'] == 0]['BloodPressure'].count())
print('SkinThickness',df[df['SkinThickness'] == 0]['SkinThickness'].count())
print('Insulin',df[df['Insulin'] == 0]['Insulin'].count())
print('BMI',df[df['BMI'] == 0]['BMI'].count())
print('DiabetesPedigreeFunction',df[df['DiabetesPedigreeFunction'] == 0]['DiabetesPedigreeFunction'].count())
print('Age',df[df['Age'] == 0]['Age'].count())

glucose = df.loc[df['Glucose'] != 0,'Glucose'].median()
df['Glucose'] = df['Glucose'].replace(0, glucose)
bp = df.loc[df['BloodPressure'] != 0,'BloodPressure'].median()
df['BloodPressure'] = df['BloodPressure'].replace(0, bp)
st = df.loc[df['SkinThickness'] != 0,'SkinThickness'].median()
df['SkinThickness'] = df['SkinThickness'].replace(0, st)
insulin = df.loc[df['Insulin'] != 0,'Insulin'].median()
df['Insulin'] = df['Insulin'].replace(0, insulin)
bmi = df.loc[df['BMI'] != 0,'BMI'].median()
df['BMI'] = df['BMI'].replace(0, bmi)

# for col in columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

# for col in columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

# sns.countplot(data=df, x='Outcome', hue='Outcome')
# plt.show()

pearsonr_list = list()
for col in columns:
    pearsonr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['Outcome'])
    pearsonr_dict['name'] = col
    pearsonr_dict['corr_coef'] = corr_coef
    pearsonr_dict['p value'] = p_val
    pearsonr_dict['decision'] = 'keep feature' if 0.05 > p_val else 'drop feature'
    pearsonr_list.append(pearsonr_dict)

pearsonr_df = pd.DataFrame(pearsonr_list)
print(pearsonr_df)

X = df.drop(columns='Outcome')
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
scaler = StandardScaler()
X_train[columns] = scaler.fit_transform(X_train[columns])
X_test[columns] = scaler.transform(X_test[columns])
models = {
    'LogisticRegression': LogisticRegression(),
    'KNeighborsClassifier': KNeighborsClassifier(n_neighbors=5),
    'GaussianNB': GaussianNB(),
    'DecisionTreeClassifier': DecisionTreeClassifier(),
    'SVC': SVC(),
}
for key, value in models.items():
    model = value
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f'Model name: {key}')
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    print(f'Confusion matrix: {confusion_matrix(y_test, y_pred)}')
    print(f'Classification report: {classification_report(y_test, y_pred)}')
    print('********************************')