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
from sklearn.model_selection import GridSearchCV

df = pd.read_csv(r'Week-8-Assignments\Classification-Assignments\Titanic-Survival-Prediction.csv')
print(df.head())
print('**********************************************************************************************')
print(df.shape)
print('**********************************************************************************************')
print(df.columns)
print('**********************************************************************************************')
print(df.dtypes)
print('**********************************************************************************************')
print(df.info())
print('**********************************************************************************************')
print(df.describe())
print('**********************************************************************************************')
print(df.isnull().sum())
print('**********************************************************************************************')
print(df.duplicated().sum())
print('**********************************************************************************************')

df.drop(columns='PassengerId', inplace=True)

numerical_columns = ['Age', 'SibSp', 'Parch', 'Fare']
categorical_columns = ['Sex', 'Embarked', 'Pclass', 'Survived']

# for col in numerical_columns:
#     sns.histplot(data=df, x=col, bins=20, kde=True)
#     plt.show()

# for col in categorical_columns:
#     sns.countplot(data=df, x=col, hue='Survived')
#     plt.show()

# for col in numerical_columns:
#     sns.boxplot(data=df, x=col)
#     plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()

df_cleaned = df.copy()

df_cleaned['Embarked'] = df_cleaned['Embarked'].fillna(
    df_cleaned['Embarked'].mode()[0]
)

df_cleaned['Age'] = df_cleaned['Age'].fillna(
    df_cleaned['Age'].median()
)

print(df_cleaned.isnull().sum())

df_cleaned['Sex'] = df_cleaned['Sex'].map({
    'male': 1,
    'female': 0
})

print(df_cleaned.head())

df_cleaned['Title'] = df_cleaned['Name'].str.split(',').str[1].str.split('.').str[0].str.strip()

df_cleaned = df_cleaned.loc[
    (df_cleaned['Title'] == 'Mr') | (df_cleaned['Title'] == 'Mrs') |
    (df_cleaned['Title'] == 'Master') | (df_cleaned['Title'] == 'Miss') 
    , :
]

df_cleaned.drop('Name', axis=1, inplace=True)

df_cleaned = pd.get_dummies(df_cleaned, columns=['Embarked', 'Title'], drop_first=True)
print(df_cleaned.columns)

df_cleaned[['Embarked_Q', 'Embarked_S', 'Title_Miss', 'Title_Mr', 'Title_Mrs']] = df_cleaned[['Embarked_Q', 'Embarked_S', 'Title_Miss', 'Title_Mr', 'Title_Mrs']].astype(int)

df_cleaned.drop(columns=['Ticket', 'Cabin'], inplace=True)

print(df_cleaned.columns)

numerical_columns = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
categorical_columns = ['Sex', 'Embarked_Q', 'Embarked_S', 'Title_Miss', 'Title_Mr', 'Title_Mrs']

pearson_corr_list = list()
for col in numerical_columns:
    pearson_corr_dict = dict()
    corr_coef, p_val = pearsonr(df_cleaned[col], df_cleaned['Survived'])
    pearson_corr_dict['Feature Name'] = col
    pearson_corr_dict['Correlation Coefficient'] = corr_coef
    pearson_corr_dict['P Value'] = p_val
    pearson_corr_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    pearson_corr_list.append(pearson_corr_dict)

pearson_corr_df = pd.DataFrame(pearson_corr_list)
print(pearson_corr_df)

chi2_list = list()
for col in categorical_columns:
    chi2_dict = dict()
    contingency_table = pd.crosstab(df_cleaned[col], df_cleaned['Survived'])
    chi2_val, p_val, x, y = chi2_contingency(contingency_table)
    chi2_dict['Feature Name'] = col
    chi2_dict['Chi2 Value'] = chi2_val
    chi2_dict['P Value'] = p_val
    chi2_dict['Decision'] = 'Keep Feature' if 0.05 > p_val else 'Drop Feature'
    chi2_list.append(chi2_dict)

chi2_df = pd.DataFrame(chi2_list)
print(chi2_df)

# Drop nothing

X = df_cleaned.drop('Survived', axis=1)
y = df_cleaned['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
scaler = StandardScaler()
columns = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
X_train[columns] = scaler.fit_transform(X_train[columns])
X_test[columns] = scaler.transform(X_test[columns])

logistic_classifier = LogisticRegression()
logistic_classifier.fit(X_train,y_train)
y_pred_logistic_classifier = logistic_classifier.predict(X_test)
print(accuracy_score(y_test, y_pred_logistic_classifier))
print(confusion_matrix(y_test, y_pred_logistic_classifier))
print(classification_report(y_test, y_pred_logistic_classifier))

print('*******************************************************************')

knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train,y_train)
y_pred_knn_classifier = knn_classifier.predict(X_test)
print(accuracy_score(y_test, y_pred_knn_classifier))
print(confusion_matrix(y_test, y_pred_knn_classifier))
print(classification_report(y_test, y_pred_knn_classifier))

print('*******************************************************************')

nb_classifier = GaussianNB()
nb_classifier.fit(X_train,y_train)
y_pred_nb_classifier = nb_classifier.predict(X_test)
print(accuracy_score(y_test, y_pred_nb_classifier))
print(confusion_matrix(y_test, y_pred_nb_classifier))
print(classification_report(y_test, y_pred_nb_classifier))

print('*******************************************************************')

dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train,y_train)
y_pred_dt_classifier = dt_classifier.predict(X_test)
print(accuracy_score(y_test, y_pred_dt_classifier))
print(confusion_matrix(y_test, y_pred_dt_classifier))
print(classification_report(y_test, y_pred_dt_classifier))

print('*******************************************************************')

svm_classifier = SVC()
svm_classifier.fit(X_train,y_train)
y_pred_svm_classifier = svm_classifier.predict(X_test)
print(accuracy_score(y_test, y_pred_svm_classifier))
print(confusion_matrix(y_test, y_pred_svm_classifier))
print(classification_report(y_test, y_pred_svm_classifier))

print('*******************************************************************')

# Hyperparameter tuning

logistic_classifier_gsc = GridSearchCV(estimator=LogisticRegression(), param_grid={
    'penalty': ['l1', 'l2', 'elasticnet', None],
    'C': [0.01, 0.1, 1.0, 10.0],
    'max_iter': [10, 100, 1000]
}, cv=5)

logistic_classifier_gsc.fit(X_train, y_train)
y_pred_logistic_classifier_gsc = logistic_classifier_gsc.predict(X_test)
print(accuracy_score(y_test, y_pred_logistic_classifier_gsc))
print(confusion_matrix(y_test, y_pred_logistic_classifier_gsc))
print(classification_report(y_test, y_pred_logistic_classifier_gsc))
print(logistic_classifier_gsc.best_estimator_)
print(logistic_classifier_gsc.best_params_)
print(logistic_classifier_gsc.best_score_)

print('*************************************************************************')

knn_classifier_gsc = GridSearchCV(estimator=KNeighborsClassifier(), param_grid={
    'n_neighbors': [3,5,7,9,11],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'minkowski']
}, cv=5)

knn_classifier_gsc.fit(X_train, y_train)
y_pred_knn_classifier_gsc = knn_classifier_gsc.predict(X_test)
print(accuracy_score(y_test, y_pred_knn_classifier_gsc))
print(confusion_matrix(y_test, y_pred_knn_classifier_gsc))
print(classification_report(y_test, y_pred_knn_classifier_gsc))
print(knn_classifier_gsc.best_estimator_)
print(knn_classifier_gsc.best_params_)
print(knn_classifier_gsc.best_score_)

print('*************************************************************************')

dt_classifier_gsc = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid={
    'criterion': ['gini', 'entropy', 'log_loss'],
    'splitter': ['best', 'random'],
    'max_features': ['sqrt', 'log2', None]
}, cv=5)

dt_classifier_gsc.fit(X_train, y_train)
y_pred_dt_classifier_gsc = dt_classifier_gsc.predict(X_test)
print(accuracy_score(y_test, y_pred_dt_classifier_gsc))
print(confusion_matrix(y_test, y_pred_dt_classifier_gsc))
print(classification_report(y_test, y_pred_dt_classifier_gsc))
print(dt_classifier_gsc.best_estimator_)
print(dt_classifier_gsc.best_params_)
print(dt_classifier_gsc.best_score_)

print('*************************************************************************')

svm_classifier_gsc = GridSearchCV(estimator=SVC(), param_grid={
    'C': [0.01, 0.1, 1, 10, 100],
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    'gamma': ['scale', 'auto']
}, cv=5)
svm_classifier_gsc.fit(X_train, y_train)
y_pred_svm_classifier_gsc = svm_classifier_gsc.predict(X_test)
print(accuracy_score(y_test, y_pred_svm_classifier_gsc))
print(confusion_matrix(y_test, y_pred_svm_classifier_gsc))
print(classification_report(y_test, y_pred_svm_classifier_gsc))
print(svm_classifier_gsc.best_estimator_)
print(svm_classifier_gsc.best_params_)
print(svm_classifier_gsc.best_score_)