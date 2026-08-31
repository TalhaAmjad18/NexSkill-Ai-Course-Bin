import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv(r'Week-8-Assignments/Classification-Assignments/Mushroom-Classification.csv')
print(df.head())
print('****************************************************************')
print(df.shape)
print('****************************************************************')
print(df.columns)
print('****************************************************************')
print(df.dtypes)
print('****************************************************************')
print(df.info())
print('****************************************************************')
print(df.describe())
print('****************************************************************')
print(df.isnull().sum())
print('****************************************************************')
print(df.duplicated().sum())
print('****************************************************************')

columns = ['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat']

df['stalk-root'] = df['stalk-root'].replace('?', df['stalk-root'].mode()[0])

for col in columns:
    print(f'{col}: {df[col].nunique()}')
    print(df[col].value_counts())
    print()
    print('*******************************')
    print()

# all columns are categorical so we will make countplots for each column

# for col in columns:
#     sns.countplot(data=df, x=col, hue='class')
#     plt.show()

df['class'] = df['class'].map({
    'e': 0,
    'p': 1
})

df['bruises'] = df['bruises'].map({
    'f': 0,
    't': 1
})

df['gill-attachment'] = df['gill-attachment'].map({
    'f': 0,
    'a': 1
})

df['gill-spacing'] = df['gill-spacing'].map({
    'c': 0,
    'w': 1
})

df['gill-size'] = df['gill-size'].map({
    'b': 0,
    'n': 1
})

df['stalk-shape'] = df['stalk-shape'].map({
    't': 0,
    'e': 1
})

df['veil-type'] = df['veil-type'].map({
    'p': 1,
})

df = pd.get_dummies(df, columns=['cap-shape','cap-surface','cap-color','odor','gill-color','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'], drop_first=True)

df = df.astype(int)

print(df.head())
print(df.columns)

updated_columns = ['bruises', 'gill-attachment', 'gill-spacing', 'gill-size',
       'stalk-shape', 'veil-type', 'cap-shape_c', 'cap-shape_f', 'cap-shape_k',
       'cap-shape_s', 'cap-shape_x', 'cap-surface_g', 'cap-surface_s',
       'cap-surface_y', 'cap-color_c', 'cap-color_e', 'cap-color_g',
       'cap-color_n', 'cap-color_p', 'cap-color_r', 'cap-color_u',
       'cap-color_w', 'cap-color_y', 'odor_c', 'odor_f', 'odor_l', 'odor_m',
       'odor_n', 'odor_p', 'odor_s', 'odor_y', 'gill-color_e', 'gill-color_g',
       'gill-color_h', 'gill-color_k', 'gill-color_n', 'gill-color_o',
       'gill-color_p', 'gill-color_r', 'gill-color_u', 'gill-color_w',
       'gill-color_y', 'stalk-root_c', 'stalk-root_e', 'stalk-root_r',
       'stalk-surface-above-ring_k', 'stalk-surface-above-ring_s',
       'stalk-surface-above-ring_y', 'stalk-surface-below-ring_k',
       'stalk-surface-below-ring_s', 'stalk-surface-below-ring_y',
       'stalk-color-above-ring_c', 'stalk-color-above-ring_e',
       'stalk-color-above-ring_g', 'stalk-color-above-ring_n',
       'stalk-color-above-ring_o', 'stalk-color-above-ring_p',
       'stalk-color-above-ring_w', 'stalk-color-above-ring_y',
       'stalk-color-below-ring_c', 'stalk-color-below-ring_e',
       'stalk-color-below-ring_g', 'stalk-color-below-ring_n',
       'stalk-color-below-ring_o', 'stalk-color-below-ring_p',
       'stalk-color-below-ring_w', 'stalk-color-below-ring_y', 'veil-color_o',
       'veil-color_w', 'veil-color_y', 'ring-number_o', 'ring-number_t',
       'ring-type_f', 'ring-type_l', 'ring-type_n', 'ring-type_p',
       'spore-print-color_h', 'spore-print-color_k', 'spore-print-color_n',
       'spore-print-color_o', 'spore-print-color_r', 'spore-print-color_u',
       'spore-print-color_w', 'spore-print-color_y', 'population_c',
       'population_n', 'population_s', 'population_v', 'population_y',
       'habitat_g', 'habitat_l', 'habitat_m', 'habitat_p', 'habitat_u',
       'habitat_w']

chi2_list = list()
for col in updated_columns:
    chi2_dict = dict()
    contingency_table = pd.crosstab(df[col], df['class'])
    chi2_val , p_val , x , y = chi2_contingency(contingency_table)
    chi2_dict['name'] = col
    chi2_dict['chi2 value'] = chi2_val
    chi2_dict['p val'] = p_val
    chi2_dict['decision'] = 'keep feature' if 0.05 > p_val else 'feature drop'
    chi2_list.append(chi2_dict)

chi2_df = pd.DataFrame(chi2_list)
print(chi2_df)

# keep all features

X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
scaler = StandardScaler()
X_train[updated_columns] = scaler.fit_transform(X_train[updated_columns])
X_test[updated_columns] = scaler.transform(X_test[updated_columns])

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