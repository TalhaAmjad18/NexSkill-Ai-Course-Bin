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

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Iris.csv')

print(df.head())
print('************************************************************************')
print(df.shape)
print('************************************************************************')
print(df.columns)
print('************************************************************************')
print(df.dtypes)
print('************************************************************************')
print(df.info())
print('************************************************************************')
print(df.describe())
print('************************************************************************')
print(df.isnull().sum())
print('************************************************************************')
print(df.duplicated().sum())
print('************************************************************************')

df.drop('Id', axis=1, inplace=True)
numerical_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

# sns.countplot(data=df, x='Species', hue='Species')
# plt.show()

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

df['Species'] = df['Species'].map({
    'Iris-setosa': 0,       
    'Iris-versicolor': 1,  
    'Iris-virginica': 2   
})

df['SepalArea'] = df['SepalLengthCm'] * df['SepalWidthCm']
df['PetalArea'] = df['PetalLengthCm'] * df['PetalWidthCm']

columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'SepalArea', 'PetalArea']

pearson_corr_list = list()
for col in columns:
    pearson_corr_dict = dict()
    corr_coef, p_val = pearsonr(df[col], df['Species'])
    pearson_corr_dict['Feature Name'] = col
    pearson_corr_dict['Correlation Coefficient'] = corr_coef
    pearson_corr_dict['P Value'] = p_val
    pearson_corr_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    pearson_corr_list.append(pearson_corr_dict)

pearson_corr_df = pd.DataFrame(pearson_corr_list)
print(pearson_corr_df)

# chi2_list = list()
# for col in columns:
#     chi2_dict = dict()
#     contingency_table = pd.crosstab(df[col], df['Species'])
#     chi2_val, p_val, x, y = chi2_contingency(contingency_table)
#     chi2_dict['Feature Name'] = col
#     chi2_dict['Chi2 Value'] = chi2_val
#     chi2_dict['P Value'] = p_val
#     chi2_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
#     chi2_list.append(chi2_dict)

# chi2_df = pd.DataFrame(chi2_list)
# print(chi2_df)

X = df.drop('Species', axis=1)
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)
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