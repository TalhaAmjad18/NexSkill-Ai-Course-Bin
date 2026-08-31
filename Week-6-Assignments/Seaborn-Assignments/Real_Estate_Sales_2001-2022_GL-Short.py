import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'Week-4-Assignments\Pandas-Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', parse_dates=['Date Recorded'], date_format={'Date Recorded': '%m/%d/%Y'})

print(df.head())

sns.set_style('darkgrid')

def show(title):
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 🟢 Easy Level

# 1.A real estate company wants to identify the 10 towns with the highest number of property sales so it can decide where to expand its business.

topTenTowns = df['Town'].value_counts().head(10).index
sns.countplot(data=df, x='Town', order=topTenTowns)
show('Graph 1')

# 2.A housing market analyst wants to understand how property sale amounts are distributed across all recorded transactions.

sns.histplot(data=df, x='Sale Amount', bins=30, kde=True)
show('Graph 2')

# 3.A government valuation department wants to analyze how assessed property values are distributed in the dataset.

sns.histplot(data=df, x='Assessed Value', bins=30, kde=True)
show('Graph 3')

# 4.A property marketplace wants to know which 10 property types are sold most frequently.

topTenProperty = df['Property Type'].value_counts().index
sns.countplot(data=df, x='Property Type', order=topTenProperty)
show('Graph 4')

# 5.A real estate consultant wants to compare the average sale amount of the 10 towns with the highest number of property sales.

topTenTowns = df['Town'].value_counts().head(10).index
filterDf0 = df[df['Town'].isin(topTenTowns)]
sns.barplot(data=filterDf0, x='Town', y='Sale Amount')
show('Graph 5')

# 6.A market research company wants to identify which list year recorded the highest number of property sales.

listYears = df['List Year'].value_counts()
sns.lineplot(x=listYears.index, y=listYears.values)
show('Graph 6')

# 7.A property investment firm wants to compare the average assessed value across different property types.

sns.barplot(data=df, x='Property Type', y='Assessed Value')
show('Graph 7')

# 🟡 Medium Level

# 8.A valuation company wants to investigate whether there is a relationship between assessed value and sale amount.

sns.scatterplot(data=df, x='Assessed Value', y='Sale Amount')
show('Graph 8')

# 9.A tax authority wants to compare the average sales ratio across different property types.

sns.barplot(data=df, x='Property Type', y='Sales Ratio')
show('Graph 9')

# 10.A housing analyst wants to compare the distribution of sale amounts across different residential types.

sns.violinplot(data=df, x='Residential Type', y='Sale Amount')
show('Graph 10')

# 11.An investment company wants to determine which towns have the highest average sale amount among the top 10 towns with the most sales.

topTenTown = df['Town'].value_counts().head(10).index
filterDf1 = df[df['Town'].isin(topTenTown)]
sns.barplot(data=filterDf1, x='Town', y='Sale Amount')
show('Graph 11')

# 12.A financial analyst wants to investigate whether expensive properties tend to have higher or lower sales ratios.

expensiveProperties = df.sort_values(by='Sale Amount', ascending=False).head(20)
sns.scatterplot(data=expensiveProperties, x='Sale Amount', y='Sales Ratio')
show('Graph 12')

# 13.A real estate research firm wants to analyze how the number of property sales has changed over the years.

listYears = df['List Year'].value_counts()
sns.lineplot(x=listYears.index, y=listYears.values)
show('Graph 13')

# 14.A property consultancy wants to compare how sale amounts vary across the 10 towns with the highest number of property sales.

topTenTowns = df['Town'].value_counts().head(10).index
filterDf2 = df[df['Town'].isin(topTenTowns)]
sns.boxplot(data=filterDf2, x='Town', y='Sale Amount')
show('Graph 14')

# 15.A fraud detection team wants to identify unusually high or unusually low property sale amounts that may require further investigation.

sns.boxplot(data=df, x='Sale Amount')
show('Graph 15')