import pandas as pd

df = pd.read_csv(r'Week-4-Assignments\Pandas-Assignments\FastFoodRestaurants.csv', delimiter=',')

print(df)

print("Columns in df: \n", df.columns)
print("Datatypes of columns: \n", df.dtypes)
print("Shape of df: \n", df.shape)

print("Statistical analysis of df: \n", df.describe())
print("Information of df: \n", df.info())

print("First 3 rows: \n", df.head(3))
print("Last 3 rows: \n", df.tail(3))

# accessing single column
restaurantName = df['name']
print("accessing one column: \n", restaurantName)

# accessing mutiple column
latitudeLongitude = df[['latitude', 'longitude']]
print("accessing multiple columns: \n", latitudeLongitude)

# using .loc

# Case 1

# accessing 1 row
row1 = df.loc[0]
print("accessing 1 row: \n", row1)

# accessing multiple rows
row2 = df.loc[[0,2,4]]
print("accessing multiple rows: \n", row2)

# accessing slice of rows
row3 = df.loc[0:10]
print("accessing slice of rows: \n", row3)

# acceesing row bases on a condition
row4 = df.loc[df['websites'] == 'http://www.wendys.com']
print("accessing row based on condition: \n", row4)

# accessing one column
column1 = df.loc[:, 'name']
print("accessing one column: \n", column1)

# accessing multiple columns
column2 = df.loc[:,['name', 'longitude', 'latitude']]
print("accessing multiple columns: \n", column2)

# accessing slice of columns
column3 = df.loc[:,'name':'province']
print("accessing slice of columns: \n", column3)

# accessing column based on a condition
column4 = df.loc[df['websites'] == 'http://www.wendys.com', 'name']
print('accessing column based on a condition: \n', column4)

# using .iloc

# accessing 1 row
row1 = df.iloc[0]
print("accessing 1 row: \n", row1)

# accessing multiple rows
row2 = df.iloc[[0,2,4]]
print("accessing multiple rows: \n", row2)

# accessing slice of rows
row3 = df.iloc[0:10]
print("accessing slice of rows: \n", row3)

# accessing one column
column1 = df.iloc[:,0]
print("accessing one column: \n", column1)

# accessing multiple columns
column2 = df.iloc[:,[0,2,4]]
print("accessing multiple columns: \n", column2)

# accessing slice of columns
column3 = df.iloc[:,0:3]
print("accessing slice of columns: \n", column3)

# adding a new row in a dataframe
df.loc[len(df)] = ['324 Main St,Massena','US','us/ny/massena/324mainst/-1161002137',44.9213,-74.89021,'McDonald',13662,'NY','http://mcdonalds.com','http://www.mcdonalds.com/?cid=RF:YXT_FM:TP::Yext:Referral']
print("added row: \n",df.tail(2))

# adding a new column in dataframe
df['index'] = [ i for i in range(len(df)) ]
print(df['index'])

# updating existing value
df.loc[df['index'] == 0, 'index'] = -1
print(df) 

# # deleting row 1
# df.drop(0, axis=0, inplace=True)
# print(df.head(5))

# # deleting row 1 using index
# df.drop(index=1, inplace=True)
# print(df.head(5))

# # deleting mutiple rows
# df.drop([2,3], axis=0, inplace=True)
# print(df.head(5))

# # deleting multiple rows using index
# df.drop(index=[4,5], inplace=True)
# print(df.head(5))

# # deleting 1 column
# df.drop('index', axis=1, inplace=True)
# print(df.columns)

# # deleting row 1 using columns
# df.drop(columns='name', inplace=True)
# print(df.columns)

# # deleting mutiple columns
# df.drop(['longitude', 'latitude'], axis=1, inplace=True)
# print(df.columns)

# # deleting multiple rows using columns
# df.drop(columns=['postalCode', 'websites'], inplace=True)
# print(df.columns)

# rename columns in df
df.rename(columns={'index':'index_column'}, inplace=True)
print(df['index_column'])

# rename mutiple columns in df using mapper
df.rename(mapper={'index_column':'index', 'name':'resto_name'}, axis=1, inplace=True)
print(df[['index', 'resto_name']])

# rename row in df
df.rename(index={0:-0}, inplace=True)
print(df)

# rename mutiple rows in df using mapper
df.rename(mapper={1:-1, 2:-2}, axis=0, inplace=True)
print(df)

# query()
selected_rows = df.query("resto_name == \"McDonald's\" and province == 'NY'")
print(selected_rows)

# sort_values()
sort_df = df.sort_values(by='latitude')
print(sort_df)

# groupby()
grouped_df = df.groupby('province')['latitude'].sum()
print(grouped_df)

# dropna, fillna

df.fillna(0,inplace=True)
print(df)

df.dropna(inplace=True)
print(df)