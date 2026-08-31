import pandas as pd

# 1. Load & Inspect

# Read startup_growth_investment_data.csv into a DataFrame.
df = pd.read_csv(r'Week-4-Assignments\Pandas-Assignments\startup_growth_investment_data.csv', delimiter=',')
print(df)

# Print its shape, data types, and a summary of statistics (describe()).
print(f"Shape of dataset is: \n {df.shape}")
print(f"Columns of dataset is: \n {df.columns}")
print(f"Datatypes columns of dataset is: \n {df.dtypes}")
print(f"Summary of statistical analysis of dataset is: \n {df.describe()}")

# Show the first 5 and last 5 rows.
print(f"First 5 rows: \n {df.head(5)}")
print(f"Last 5 rows: \n {df.tail(5)}")

# 2. Selection Practice (.loc / .iloc)

# Select only the Startup Name, Industry, and Valuation (USD) columns for all rows.
selected_columns1 = df.loc[:,['Startup Name', 'Industry', 'Valuation (USD)']]
print(selected_columns1)

# Using .loc, select all startups founded in India.
selected_columns2 = df.loc[df['Country'] == 'India', :]
print(selected_columns2)

# Using .iloc, select rows 10 to 20 (positional) and columns 2 to 5 (positional).
selected_columns3 = df.iloc[10:21, 2:6]
print(selected_columns3)

# Select all startups where Growth Rate (%) is greater than 150 and Number of Investors is greater than 40 (conditional .loc).
selected_columns4 = df.loc[(df['Growth Rate (%)'] > 150) & (df['Number of Investors'] > 40), :]
print(selected_columns4)

# 3. Sorting

# Sort the DataFrame by Valuation (USD) in descending order and show the top 10 startups.
sorted_df1 = df.sort_values(by='Valuation (USD)', ascending=False)
print(sorted_df1.head(10))

# Sort by Country (ascending) then Investment Amount (USD) (descending).
# sorted_df2 = df.sort_values(by='Country').sort_values(by='Investment Amount (USD)', ascending=False) -> yeh ghalat hai.
sorted_df2 = df.sort_values(by=['Country', 'Investment Amount (USD)'], ascending=[True, False])
print(sorted_df2.head(10))

# 4. Grouping & Aggregation

# Group by Industry and find the average Valuation (USD) per industry.
group1 = df.groupby('Industry')['Valuation (USD)'].mean()
print(f"Group by Industry and find the average Valuation (USD) per industry: \n {group1}")

# Group by Country and find the total Investment Amount (USD) per country, sorted descending.
group2 = df.groupby('Country')['Investment Amount (USD)'].sum().sort_values(ascending=False)
print(f"Group by Country and find the total Investment Amount (USD) per country, sorted descending: \n {group2}")

# Find which Industry has the highest average Growth Rate (%).
group3 = df.groupby('Industry')['Growth Rate (%)'].mean().sort_values(ascending=False)
print(f"Industry with the highest average Growth Rate (%): {group3.index[0]}:{group3.values[0]:.2f}")

# 5. Filtering with query()

# Use .query() to find all startups founded after 2015 with a valuation over $5 billion.
selected_rows = df.query("`Year Founded` > 2015 and `Valuation (USD)` > 5000000000")
print(f"all startups founded after 2015 with a valuation over $5 billion: \n {selected_rows}")

# 6. Data Manipulation

# Add a new column Investment per Round = Investment Amount (USD) / Funding Rounds.
df['Investment per Round'] = df['Investment Amount (USD)'] / df['Funding Rounds']
print(df.head())

# Rename Number of Investors to Investor Count.
df.rename(columns={'Number of Investors':'Investor Count'}, inplace=True)
print(df['Investor Count'])

# Drop the Year Founded column (assume it's no longer needed for this specific report).
#df.drop(columns='Year Founded', inplace=True)
print(df.head())

# 7. Data Cleaning

# Check for any missing values (isnull().sum()).
print(df.isnull().sum())

# If there are missing values, decide whether to fillna() or dropna(), and justify your choice in a comment.
# no missing value

# 8. Bonus (Insight Question)

# Which country has the highest average Growth Rate (%) among startups with more than 5 funding rounds?
selectedDf = df[df['Funding Rounds'] > 5]
group4 = selectedDf.groupby('Country')['Growth Rate (%)'].mean().sort_values(ascending=False)
print(f"country with the highest average Growth Rate (%) among startups with more than 5 funding rounds: \n {group4.index[0]} : {group4.values[0]:.2f}")

country_region = pd.DataFrame({
    'Country': ['USA', 'UK', 'Germany', 'France', 'India', 'China', 'Singapore', 'Australia'],
    'Region': ['North America', 'Europe', 'Europe', 'Europe', 'Asia', 'Asia', 'Asia', 'Oceania'],
    'Currency': ['USD', 'GBP', 'EUR', 'EUR', 'INR', 'CNY', 'SGD', 'AUD']
})

# 1. Merging (the #1 real-world skill)

# Merge df with country_region on Country so every startup has a Region and Currency.
mergedDf = pd.merge(df, country_region, on='Country')
print(mergedDf.head())

# Use how='left' — check if any countries in df didn't find a match (Region is NaN). This mimics real data where lookup tables are incomplete.
mergedDf2 = pd.merge(df, country_region, on='Country', how='left')
print(mergedDf2.head())
selected_countries = mergedDf2[mergedDf2['Region'].isnull()]
nan_countries = selected_countries['Country'].value_counts()
print(nan_countries)

# Then group by Region and find total Investment Amount (USD) per region.
group5 = mergedDf2.groupby('Region')['Investment Amount (USD)'].sum()
print(group5)

# 2. apply() / lambda (custom logic)

# Create a new column Valuation Tier: "Unicorn" if Valuation (USD) >= 1_000_000_000, else "Sub-Unicorn". Use .apply() with a lambda (don't just use np.where — practice the apply pattern).
mergedDf2['Valuation Tier'] = mergedDf2['Valuation (USD)'].apply(lambda x: 'Unicorn' if x >= 1_000_000_000 else "Sub-Unicorn")
print(mergedDf2.head())

# Create a column Startup Age = a fixed reference year (say 2025) minus Year Founded.
mergedDf2['Startup Age'] = mergedDf2['Year Founded'].apply(lambda x: 2026 - x)
print(mergedDf2.head())

# Use .apply() on Growth Rate (%) to bucket it into "Low" (<50), "Medium" (50-150), "High" (>150).
mergedDf2['Growth Category'] = mergedDf2['Growth Rate (%)'].apply(lambda x: 'Low' if x < 50 else 'Medium' if x >= 50 and x <= 150 else 'High')
print(mergedDf2.head())

# 3. String operations (.str)

# Extract the numeric suffix from Startup Name (e.g., "Startup_42" → 42) into a new column, using .str.split() or .str.extract() with regex.
mergedDf2['index'] = mergedDf2['Startup Name'].str.split('_').str[1]
print(mergedDf2.head())

# Find how many startups have Industry names containing the letter "e" (case-insensitive) using .str.contains().
count = mergedDf2['Industry'].str.lower().str.contains('e').sum()
print(count)

# 4. Reshaping — pivot_table()

# Build a pivot table: rows = Industry, columns = Country, values = average Valuation (USD).
pivotTable = pd.pivot_table(mergedDf2, index='Industry', columns='Country', values='Valuation (USD)', aggfunc='mean')
print(pivotTable)

# Build a pivot table showing count of startups per Industry per Region (after your merge in Q1).
pivotTable2 = pd.pivot_table(mergedDf2, index='Industry', columns='Region', values='Startup Name', aggfunc='count')
print(pivotTable2)
