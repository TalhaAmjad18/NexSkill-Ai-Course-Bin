import pandas as pd

df = pd.read_csv(r'Week-4-Assignments\Pandas-Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', parse_dates=['Date Recorded'], date_format={'Date Recorded': '%m/%d/%Y'})

df.drop(columns=['Non Use Code', 'Assessor Remarks', 'OPM remarks', 'Location'], inplace=True)

print(df.columns)
print(df.dtypes)
print(df.shape)

print(df.describe())
print(df.info())

print("top 3 rows: \n",df.head(3))
print("bottom 3 rows: \n",df.tail(3))

print("accessing one column: \n", df['Town'])

print("accessing multiple columns: \n", df[['Town', 'Date Recorded']])

# using loc[]

print("one row: \n", df.loc[0])
print("multiple rows: \n", df.loc[[0,2,4]])
print("slice of rows: \n", df.loc[0:10])
print("conditional rows: \n", df.loc[df['Town']=='Avon'])

print("one column: \n", df.loc[:10,'Town'])
print("multiple columns: \n", df.loc[:10,['Town','Date Recorded']])
print("slice of columns: \n", df.loc[:10,'Town':])
print("conditional columns: \n", df.loc[df['Date Recorded'] == '4/14/2021','Town':])

dfIndex = pd.read_csv(r'Week-4-Assignments\Pandas-Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', parse_dates=['Date Recorded'], date_format={'Date Recorded': '%m/%d/%Y'}, index_col='Serial Number')

dfIndex.drop(columns=['Non Use Code', 'Assessor Remarks', 'OPM remarks', 'Location'], inplace=True)

print(dfIndex.head(3))
print(dfIndex.columns)
print(dfIndex.dtypes)

# using .loc[]

print("one row: \n", dfIndex.loc[20281])
print("multiple rows: \n", dfIndex.loc[[2020177, 2020225]])
print("slice of rows: \n", dfIndex.loc[2020177: 20058])
print("conditional rows: \n", dfIndex.loc[dfIndex['Town']== 'Avon'])

print("one column: \n", dfIndex.loc[20281,'Town'])
print("multiple columns: \n", dfIndex.loc[[2020177, 2020225],['Town', 'Date Recorded']])
print("slice of column: \n", dfIndex.loc[:20281,'Town':'Sales Ratio'])
print("conditional column: \n", dfIndex.loc[dfIndex['Town']=='Ansonia',:'Town'])

# using .iloc[]

print("one row: \n", dfIndex.iloc[0])
print("multiple rows: \n", dfIndex.iloc[[0,2,4]])
print("slice of rows: \n", dfIndex.iloc[:10])

print("one column: \n", dfIndex.iloc[:,0])
print("multiple columns: \n", dfIndex.iloc[:,[0,2,4]])
print("slice of columns: \n", dfIndex.iloc[:10,:2])

df.rename(columns={'Date Recorded': 'Date'}, inplace=True)
print(df)

df.rename(mapper={'Property Type': 'Property_Type', 'Residential Type': 'Residential_Type'}, axis=1, inplace=True)
print(df)

df.rename(index={1:-1}, inplace=True)
print(df)

df.rename(mapper={1:-1, 2:-2}, axis=0, inplace=True)
print(df)

selectedRows = df.query("Town == 'Avon' and `Serial Number` == 200500")
print(selectedRows)

sortedDf = df.sort_values(by='Sale Amount')
print("highest sale price: ", sortedDf.tail(1))

grouped = df.groupby('Town')['Sale Amount'].mean()
print(grouped)

print(df.info())

df['Residential_Type'].fillna(df['Residential_Type'].mode()[0], inplace=True)
print(df.info())