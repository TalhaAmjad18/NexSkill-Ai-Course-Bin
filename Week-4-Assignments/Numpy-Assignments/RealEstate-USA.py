import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show(title):
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

df = pd.read_csv(r'Week-4-Assignments/Numpy-Assignments/RealEstate-USA.csv', delimiter=',')
print(df)

print(f'Columns of df: \n {df.columns}')
print(f'Data types pf columns of df: \n {df.dtypes}')
print(f'Shape of dataset: \n {df.shape}')
print(f'Statistical Analysis of df: \n {df.describe()}')
print(f'Information of df: \n {df.info()}')

df.drop(columns='prev_sold_date', inplace=True)
print(df)

df['house_size'].fillna(df['house_size'].mean(), inplace=True)

# RealEstate-USA Project

# Level 1 — Data Understanding (Easy)

# How many properties are available in the dataset?
availableProperties = df.shape[0]
print(f'Available properties: \n {availableProperties}')

# What information is available for each property?
columnNames = df.columns
print(f'Info of each property: \n {columnNames}')

# Which columns contain missing values, and how many missing values does each have?
print('prev_sold_date column is dropped because it was completely null')
print(df.isnull().sum())

# What percentage of the dataset contains incomplete records?
incomplete_rows = df.isnull().sum(axis=1)
count = incomplete_rows[~(incomplete_rows == 0)].count()
print(f'percentage: \n {(count / df.shape[0] * 100)}%')

# Which property status appears most frequently?
print('property status appears most frequently: \n',df['status'].value_counts())

# How many unique cities are represented?
print('unique cities: ', df['city'].nunique())

# How many states are included?
print('unique states: ',df['state'].nunique())

# Which five states have the largest number of listed properties?
print('five states have the largest number of listed properties: \n', df['state'].value_counts().head())

# Which ten cities have the highest number of listings?
print('ten cities have the highest number of listings: \n', df['city'].value_counts().head(10))

# Which broker has listed the highest number of properties?
print('broker has listed the highest number of properties: \n', df['brokered_by'].value_counts().head(1))

# Level 2 — Price Analysis

# What is the average property price?
print('average property price is: ', np.average(df['price']))

# What is the median property price?
print('median of property price is: ', np.median(df['price']))

# Which state has the highest average property price?
group1 = df.groupby('state')['price'].mean().sort_values(ascending=False)
print(f'state with the highest average property sale: \n {group1.index[0]}: {group1.values[0]}')

# Which state has the lowest average property price?
print(f'state with the lowest average property sale: \n {group1.index[-1]}: {group1.values[-1]}')

# Which city has the most expensive average properties?
group2 = df.groupby('city')['price'].mean().sort_values(ascending=False)
print(f'city with most expensive average properties: \n {group2.index[0]}: {group2.values[0]}')

# Which city has the cheapest average properties?
print(f'city with most cheapest average properties: \n {group2.index[-1]}: {group2.values[-1]}')

# Find the ten most expensive properties.
tenMostExpensiveProperties = df.sort_values(by='price', ascending=False).head(10)
print(f'ten most expensive properties: \n {tenMostExpensiveProperties}')

# Find the ten cheapest properties.
tenMostCheapestProperties = df.sort_values(by='price').head(10)
print(f'ten most cheapest properties: \n {tenMostCheapestProperties}')

# Which brokers usually sell the most expensive properties?
group3 = df.groupby('brokered_by')['price'].max().sort_values(ascending=False).head(1)
print(f'broker that sell the most expensive properties: {group3.index[0]} : {group3.values[0]}')
# another perspective
group4 = df.groupby('brokered_by')['price'].mean().sort_values(ascending=False).head(1)
print(f'broker that sell the most expensive properties: {group4.index[0]} : {group4.values[0]}')

# Which brokers usually sell the cheapest properties?
group5 = df.groupby('brokered_by')['price'].min().sort_values().head(1)
print(f'broker that sell the most cheapest properties: {group5.index[0]} : {group5.values[0]}')
# another perspective
group6 = df.groupby('brokered_by')['price'].mean().sort_values().head(1)
print(f'broker that sell the most cheapest properties: {group6.index[0]} : {group6.values[0]}')

# Calculate the price distribution of all properties.
# sns.histplot(data=df, x='price', bins=30)
# # show('price distribution of all properties')

# # Are property prices normally distributed or heavily skewed?
# sns.histplot(data=df, x='price', bins=30, kde=True)
# # show('price distribution of all properties using kernal density estimator')
# print('price is not normally distributed, price is right skewed')

# Detect unusually expensive properties.
iqr = np.percentile(df['price'], 75) - np.percentile(df['price'], 25)
upperLimit = np.percentile(df['price'], 75) + 1.5 * iqr
lowerLimit = np.percentile(df['price'], 25) - 1.5 * iqr
filterDf1 = df[df['price'] > upperLimit]
print(filterDf1)
# sns.boxplot(data=df, x='price')
# show('Detect unusually expensive properties')

# Detect unusually cheap properties.
filterDf2 = df[df['price'] < lowerLimit]
print(filterDf2)
# sns.boxplot(data=df, x='price')
# show('Detect unusually cheap properties')

# Compare average property prices across different property statuses.
# sns.barplot(data=df, x='status', y='price')
# show('Compare average property prices across different property statuses')

# Level 3 — House Characteristics
# What is the average house size?
print('average house size: \n', df['house_size'].mean())

# Which state has the largest average houses?
largestAvg = df.groupby('state')['house_size'].mean().sort_values(ascending=False).head(1)
print(f'state with largest average houses: \n {largestAvg.index[0]}: {largestAvg.values[0]}')

# Which city has the smallest average houses?
smallestAvg = df.groupby('city')['house_size'].mean().sort_values().head(1)
print(f'city with smallest average houses: \n {smallestAvg.index[0]}: {smallestAvg.values[0]}')

# Which properties have the largest lot sizes?
lotSizes = df.sort_values(by='acre_lot', ascending=False)
print(f'properties with largest lot sizes: \n {lotSizes.head(10)}')

# Which properties have the smallest lot sizes?
print(f'properties with smallest lot sizes: \n {lotSizes.tail(10)}')

# What is the average number of bedrooms?
print(f'avg number of bedrooms: \n {df['bed'].mean()}')

# What is the average number of bathrooms?
print(f'avg number of bathrooms: \n {df['bath'].mean()}')

# Which cities have the largest homes?
largestHomes = df.groupby('city')['house_size'].mean().sort_values(ascending=False).head(10)
print(f'city with largest homes: \n {largestHomes}')

# Which states have the smallest homes?
smallestHomes = df.groupby('state')['house_size'].mean().sort_values().head()
print(f'city with smallest homes: \n {smallestHomes}')

# Which properties have unusually large house sizes?
iqrOfHouseSizes = np.percentile(df['house_size'], 75) - np.percentile(df['house_size'], 25)
upperLimitOfHouseSize = np.percentile(df['house_size'], 75) + 1.5 * iqrOfHouseSizes
lowerLimitOfHouseSize = np.percentile(df['house_size'], 25) - 1.5 * iqrOfHouseSizes
filterDf3 = df[df['house_size'] > upperLimitOfHouseSize]
print(filterDf3)
# sns.boxplot(data=df, x='house_size')
# show('properties have unusually large house sizes')

# Which properties have unusually small house sizes?
filterDf4 = df[df['house_size'] < lowerLimitOfHouseSize]
print(filterDf4)
# sns.boxplot(data=df, x='house_size')
# show('properties have unusually small house sizes')

# Level 4 — Relationships

# Is there a relationship between house size and price?
# sns.scatterplot(data=df, x='house_size', y='price')
# show('relationship between house size and price')

# Does having more bedrooms generally increase property price?
# sns.scatterplot(data=df, x='bed', y='price')
# show('bed vs price')

# Does having more bathrooms generally increase property price?
# sns.scatterplot(data=df, x='bath', y='price')
# show('bathrooms vs price')

# Is lot size related to selling price?
# sns.scatterplot(data=df, x='acre_lot', y='price')
# show('size vs price')

# Which variable has the strongest relationship with price?
# corr = df.corr(numeric_only=True)
# sns.heatmap(data=corr, annot=True)
# show('relationship with price')
# print('acre_lot has strongest relation with price')

# Are expensive houses generally larger?
# expensiveHouses = df.sort_values(by='price', ascending=False).head(50)
# sns.scatterplot(data=expensiveHouses, x='house_size', y='price')
# show('expensive house price vs expensive house size')

# Do houses with more bathrooms tend to have larger sizes?
# morebathrooms = df.sort_values(by='bath', ascending=False).head(50)
# sns.scatterplot(data=morebathrooms, x='bath', y='house_size')
# show('bath vs house size')

# Does lot size increase with house size?
# sns.scatterplot(data=df, x='house_size', y='acre_lot')
# show('lot size vs house size')

# Compare the relationship between bedrooms and bathrooms.
# sns.scatterplot(data=df, x='bed', y='bath')
# show('bed vs bath')

# Level 5 — State Performance

# Rank states according to total property value.
group7 = df.groupby('state')['price'].sum().sort_values(ascending=False)
print(group7)

# Which states contribute the largest share of total listings?
group8 = df.groupby('state')['price'].count().sort_values(ascending=False)
print(group8)

# Which states have the highest average house size?
group9 = df.groupby('state')['house_size'].mean().sort_values(ascending=False)
print(group9)

# Which states have the highest average lot size?
group10 = df.groupby('state')['acre_lot'].mean().sort_values(ascending=False)
print(group10)

# Which states have the highest average bedroom count?
group11 = df.groupby('state')['bed'].mean().sort_values(ascending=False)
print(group11)

# Which states have the highest average bathroom count?
group12 = df.groupby('state')['bath'].mean().sort_values(ascending=False)
print(group12)

# Which state has the greatest variation in prices?
group13 = df.groupby('state')['price'].std().sort_values(ascending=False)
print(group13.index[0])

# Which state has the most consistent property prices?
group14 = df.groupby('state')['price'].std().sort_values(ascending=False)
print(group14.index[-1])

# Compare average property prices of the top ten states by listings.
topTenStates = df['state'].value_counts().sort_values(ascending=False).head(10).index
filterDf5 = df[df['state'].isin(topTenStates)]
# sns.barplot(data=filterDf5, x='state', y='price')
# show('average property prices of the top ten states by listings')

# Which state has the highest percentage of luxury homes?
mask = df['price'] > df['price'].mean()
filterDf6 = df[mask]
group15 = (filterDf6.groupby('state')['price'].count() / df.groupby('state')['price'].count()) * 100
print(group15)

# Level 6 — City Analysis

# Rank cities by average property price.
group16 = df.groupby('city')['price'].mean().sort_values(ascending=False)
print(group16)

# Rank cities by average house size.
group17 = df.groupby('city')['house_size'].mean().sort_values(ascending=False)
print(group17)

# Which cities have the largest number of luxury homes?
group18 = filterDf6.groupby('city')['price'].count().sort_values(ascending=False)
print(group18)

# Which cities have mostly affordable homes?
mask2 = df['price'] < df['price'].mean()
filterDf7 = df[mask2]
group19 = filterDf7.groupby('city')['price'].count().sort_values(ascending=False)
print(group19)

# Which cities have the highest average lot size?
group20 = df.groupby('city')['acre_lot'].mean().sort_values(ascending=False)
print(group20)

# Compare average house prices among the top 20 cities.
topTwentyCities = df['city'].value_counts().sort_values(ascending=False).head(20).index
filterDf8 = df[df['city'].isin(topTwentyCities)]
group21 = filterDf8.groupby('city')['price'].mean().sort_values(ascending=False)
print(group21)
# sns.barplot(data=filterDf8, x='city', y='price')
# show('Compare average house prices among the top 20 cities')

# Which cities have the widest range of prices?
widestRange = df.groupby('city')['price'].max() - df.groupby('city')['price'].min()
print(widestRange.sort_values(ascending=False).head(1))

# Which cities contain the largest properties?
largestProperties = df['house_size'] > df['house_size'].mean()
filterDf9 = df[largestProperties]
group22 = filterDf9.groupby('city')['house_size'].count().sort_values(ascending=False)
print(group22)

# Which cities have the smallest properties?
smallestProperties = df['house_size'] < df['house_size'].mean()
filterDf10 = df[smallestProperties]
group23 = filterDf10.groupby('city')['house_size'].count().sort_values(ascending=False)
print(group23)

# Identify cities where prices are unusually high compared to neighboring cities.
# it requires additional information such as latitude and longitude which is not present in dataset

# Level 7 — Broker Performance

# Which brokers generate the highest total listing value?
print(df.groupby('brokered_by')['price'].sum().sort_values(ascending=False).head(10))

# Which brokers handle the largest number of listings?
print(df['brokered_by'].value_counts().head(10))

# Which brokers usually sell luxury properties?
mask3 = df['price'] > df['price'].mean()
filterDf11  = df[mask3]
print(filterDf11.groupby('brokered_by')['price'].count().sort_values(ascending=False).head(10))

# Which brokers usually sell budget properties?
mask4 = df['price'] < df['price'].mean()
filterDf12  = df[mask4]
print(filterDf12.groupby('brokered_by')['price'].count().sort_values(ascending=False).head(10))

# Which brokers have the highest average selling price?
print(df.groupby('brokered_by')['price'].mean().sort_values(ascending=False).head(10))

# Which brokers specialize in large homes?
mask5 = df['house_size'] > df['house_size'].mean()
filterDf13 = df[mask5]
print(filterDf13.groupby('brokered_by')['house_size'].count().sort_values(ascending=False).head(10))

# Which brokers specialize in small homes?
mask6 = df['house_size'] < df['house_size'].mean()
filterDf14 = df[mask6]
print(filterDf14.groupby('brokered_by')['house_size'].count().sort_values(ascending=False).head(10))

# Compare average house sizes handled by the top brokers.
topTenBrokers = df['brokered_by'].value_counts().head(10).index
filterDf15 = df[df['brokered_by'].isin(topTenBrokers)]
# sns.barplot(data=filterDf15, x='brokered_by', y='house_size')
# show('Compare average house sizes handled by the top brokers')

# Compare price distributions across major brokers.
# sns.violinplot(data=filterDf15, x='brokered_by', y='price')
# show('Compare price distributions across major brokers')

# Which broker appears to dominate the market?
print(df['brokered_by'].value_counts())

# Level 8 — Missing Data Investigation

# Which columns have the highest missing percentage?
missingColumns = df.isnull().sum()
for i in missingColumns.index:
    result = ((missingColumns[i] / df.shape[0]) * 100).round(2)
    print(f'{i}: {result}%')

# Are missing house sizes concentrated in specific states?
print(df.groupby('state')['house_size'].apply(lambda x: x.isnull().sum()))

# Are missing lot sizes concentrated in specific cities?
print(df.groupby('city')['acre_lot'].apply(lambda x: x.isnull().sum()))

# Which brokers have the highest percentage of incomplete listings?
df['incompleteListing'] = df.isnull().any(axis=1)
print(df.groupby('brokered_by')['incompleteListing'].mean() * 100)

# Compare property prices with and without missing values.
incomplete_price = df[df.isnull().any(axis=1)]['price']
complete_price = df[~df.isnull().any(axis=1)]['price']
print('Average price (rows WITH missing values):', incomplete_price.mean())
print('Average price (rows WITHOUT missing values):', complete_price.mean())
print('Median price (rows WITH missing values):', incomplete_price.median())
print('Median price (rows WITHOUT missing values):', complete_price.median())

# Does missing information appear random or systematic?

# Level 9 — Visualization Tasks

# Visualize the distribution of property prices.
# sns.histplot(data=df, x='price', kde=True)
# show('Visualize the distribution of property prices')

# Visualize the distribution of house sizes.
# sns.histplot(data=df, x='house_size', kde=True)
# show('Visualize the distribution of house sizes')

# Compare average property prices across states.
# sns.barplot(data=df, x='state', y='price')
# show('Compare average property prices across states')

# Compare average prices across the top ten cities.
topTenCities = df['city'].value_counts().head(10).index
filterDf16 = df[df['city'].isin(topTenCities)]
# sns.barplot(data=filterDf16, x='city', y='price')
# show('Compare average prices across the top ten cities')

# Show the relationship between house size and price.
# sns.scatterplot(data=df, x='house_size', y='price')
# show('relationship between house size and price')

# Visualize bedroom distribution.
# sns.histplot(data=df, x='bed', kde=True)
# show('Visualize bedroom distribution')

# Visualize bathroom distribution.
# sns.histplot(data=df, x='bath', kde=True)
# show('Visualize bathroom distribution')

# Compare average prices across brokers.
# sns.barplot(data=df, x='brokered_by', y='price')
# show('average prices across brokers')

# Visualize the spread of property prices by state.
# sns.violinplot(data=df, x='state', y='price')
# show('Visualize the spread of property prices by state')

# Show how lot size varies across states.
# sns.violinplot(data=df, x='state', y='acre_lot')
# show('lot size across states')

# Visualize missing values.
# sns.heatmap(data=df.isnull(), cbar=True, yticklabels=False)
# show('Visualize missing values')

# Compare average house size for different bedroom counts.
# sns.barplot(data=df, x='bed', y='house_size')
# show('average house size for different bedroom counts')

# Compare average prices for different bathroom counts.
# sns.barplot(data=df, x='bath', y='price')
# show('average price for different bathroom counts')

# Visualize the relationship between lot size and price.
# sns.scatterplot(data=df, x='acre_lot', y='price')
# show('Visualize the relationship between lot size and price')