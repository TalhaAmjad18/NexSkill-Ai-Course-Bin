import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'Week-6-Assignments\Seaborn-Assignments\startup_growth_investment_data.csv')
print(df.head())

sns.set_style('darkgrid')

def show(title):
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# # 1. Top Industries by Startup Count
# # A startup incubator ye samajhna chahta hai ke kis industry mein sabse zyada startups hain. Visualize karo ke top 10 industries mein kitne startups maujood hain.

topIndustries = df['Industry'].value_counts().head(10).index
sns.countplot(data=df, x='Industry', order=topIndustries)
show('Top Industries by Startup Count')

# # 2. Countries with the Highest Number of Startups
# # Ek international investor different countries ka startup ecosystem compare kar raha hai. Visualize karo ke top 10 countries mein startup count kitna hai.

topCountries = df['Country'].value_counts().head(10).index
sns.countplot(data=df, x='Country', order=topCountries)
show('Countries with the Highest Number of Startups')

# # 3. Distribution of Investment Amount
# # Ek venture capital firm dekhna chahti hai ke startups ko milne wali investment amounts kis tarah distribute hoti hain. Investment Amount ki distribution visualize karo.

sns.histplot(data=df, x='Investment Amount (USD)', bins=30, kde=True)
show('Distribution of Investment Amount')

# # 4. Distribution of Growth Rate
# # Business analyst ye dekhna chahta hai ke startups ki growth rates zyada tar kis range mein aati hain. Growth Rate (%) ki distribution visualize karo.

sns.histplot(data=df, x='Growth Rate (%)', bins=30, kde=True)
show('Distribution of Growth Rate')

# 5. Top Startup Industries by Average Funding Rounds
# Founder ye jan'na chahta hai ke kin industries ke startups average mein sabse zyada funding rounds complete karte hain. Top 10 industries compare karo.

topTenIndustries = df['Industry'].value_counts().head(10).index
filterDf1 = df[df['Industry'].isin(topTenIndustries)]
sns.barplot(data=filterDf1, x='Industry', y='Funding Rounds')
show('Top Startup Industries by Average Funding Rounds')

# 6. Countries with the Highest Average Valuation
# Ek global investment report ke liye identify karo ke kaun se countries ke startups ki average valuation sabse zyada hai. Top 10 countries compare karo.

topTenCountries = df['Country'].value_counts().head(10).index
filterDf2 = df[df['Country'].isin(topTenCountries)]
sns.barplot(data=filterDf2, x='Country', y='Valuation (USD)')
show('Countries with the Highest Average Valuation')

# 7. Industries with the Highest Average Number of Investors
# Ek VC firm ye dekhna chahti hai ke kis industry ke startups average mein sabse zyada investors attract karte hain. Top industries compare karo.

top10Industries = df['Industry'].value_counts().head(10).index
filterDf3 = df[df['Industry'].isin(top10Industries)]
sns.barplot(data=filterDf3, x='Industry', y='Number of Investors')
show('Industries with the Highest Average Number of Investors')

# 8. Relationship Between Investment and Valuation
# Investor ye samajhna chahta hai ke investment amount aur startup valuation ke darmiyan koi relationship hai ya nahi. Dono numerical columns ko visualize karo aur pattern observe karo.

sns.scatterplot(data=df, x='Investment Amount (USD)', y='Valuation (USD)')
show('Relationship Between Investment and Valuation')

# 9. Relationship Between Funding Rounds and Growth Rate
# Business analyst dekhna chahta hai ke zyada funding rounds lene wale startups ki growth generally zyada hoti hai ya kam. Is relationship ko visualize karo.

sns.scatterplot(data=df, x='Funding Rounds', y='Growth Rate (%)')
show('Relationship Between Funding Rounds and Growth Rate')

# 10. Growth Rate Comparison Across Industries
# Management team compare karna chahti hai ke mukhtalif industries ki average growth rate mein kya difference hai. Top 10 industries ko compare karo.

top10Industries = df['Industry'].value_counts().head(10).index
filterDf4 = df[df['Industry'].isin(top10Industries)]
sns.barplot(data=filterDf4, x='Industry', y='Growth Rate (%)')
show('Growth Rate Comparison Across Industries')

# 11. Investment Amount Comparison Across Countries
# Ek investment company dekhna chahti hai ke mukhtalif countries mein startups ko average investment kitni milti hai. Top 10 countries compare karo.

topTenCountries = df['Country'].value_counts().head(10).index
filterDf5 = df[df['Country'].isin(topTenCountries)]
sns.barplot(data=filterDf5, x='Country', y='Investment Amount (USD)')
show('Investment Amount Comparison Across Countries')

# 12. Valuation Distribution by Industry
# Ek market research company ye analyze karna chahti hai ke different industries mein startup valuations kis tarah spread hoti hain. Industries ke beech valuation distribution compare karo.

sns.violinplot(data=df, x='Industry', y='Valuation (USD)')
show('Valuation Distribution by Industry')

# 13. Growth Rate Distribution by Country
# Ek international accelerator ye dekhna chahta hai ke different countries ke startups ki growth rate distribution kis tarah differ karti hai. Top countries compare karo.

sns.violinplot(data=df, x='Country', y='Growth Rate (%)')
show('Growth Rate Distribution by Country')

# 14. Number of Investors vs Growth Rate
# Ek VC firm investigate karna chahti hai ke investors ki tadaad aur startup growth ke darmiyan koi noticeable relationship hai ya nahi. Visualization ke zariye analysis karo.

sns.scatterplot(data=df, x='Number of Investors', y='Growth Rate (%)')
show('Number of Investors vs Growth Rate')

# 15. Startup Trends by Year Founded
# Ek research organization ye dekhna chahti hai ke kis saal sabse zyada startups establish hue. Year Founded ke basis par startup counts visualize karo aur trend observe karo.

startupCounts = df['Year Founded'].value_counts()
sns.lineplot(x=startupCounts.index, y=startupCounts.values)
show('Startup Trends by Year Founded')