import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'Week-6-Assignments\Seaborn-Assignments\FastFoodRestaurants.csv', delimiter=',')
print(df.head())

# # 🟢 Easy Level (10 Questions)
# # Which 10 states have the highest number of restaurants?
tenHighestStates = df['province'].value_counts()[:10].index
sns.countplot(data=df, x='province', order=tenHighestStates)
plt.title('10 states have the highest number of restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which 10 cities have the highest number of restaurants?
tenHighestCities = df['city'].value_counts()[:10].index
sns.countplot(data=df, x='city', order=tenHighestCities)
plt.title('10 cities have the highest number of restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which 10 restaurant chains have the highest number of locations?
tenHighestRestaurants = df['name'].value_counts()[:10].index
sns.countplot(data=df, x='name', order=tenHighestRestaurants)
plt.title('10 restaurant chains have the highest number of locations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which 10 restaurant chains have the lowest number of locations?
tenLowestRestaurants = df['name'].value_counts()[-10:].index
sns.countplot(data=df, x='name', order=tenLowestRestaurants)
plt.title('10 restaurant chains have the lowest number of locations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which 10 states have the fewest restaurants?
tenLowestStates = df['province'].value_counts()[-10:].index
sns.countplot(data=df, x='province', order=tenLowestStates)
plt.title('10 states have the lowest number of restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which 10 cities have the fewest restaurants?
tenLowestCities = df['city'].value_counts()[-10:].index
sns.countplot(data=df, x='city', order=tenLowestCities)
plt.title('10 cities have the lowest number of restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # How are restaurant locations distributed by latitude?
sns.histplot(data=df, x='latitude')
plt.title('restaurant locations distributed by latitude')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # How are restaurant locations distributed by longitude?
sns.histplot(data=df, x='longitude')
plt.title('restaurant locations distributed by longitude')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which restaurant chain appears only once in the dataset?
oneRestaurant = df['name'].value_counts()
oneRestaurant = oneRestaurant[oneRestaurant == 1].index

sns.countplot(
    data=df,
    x='name',
    order=oneRestaurant
)

plt.title('Restaurant chains that appear only once')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# # Which cities contain only one restaurant in the dataset?
cityWithOneRestaurant = df['city'].value_counts()
cityWithOneRestaurant = cityWithOneRestaurant[cityWithOneRestaurant == 1].index

sns.countplot(
    data=df,
    x='city',
    order=cityWithOneRestaurant
)

plt.title('Cities containing only one restaurant')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 Distribution (Numerical Column)
# How are restaurant latitudes distributed?
sns.histplot(data=df, x='latitude')
plt.title("Distribution of latitude")
plt.tight_layout()
plt.show()

# How are restaurant longitudes distributed?
sns.histplot(data=df, x='longitude')
plt.title("Distribution of longitude")
plt.tight_layout()
plt.show()

# Which numerical column (latitude or longitude) appears closer to a normal distribution?
# latitude column

# 🔗 Relationship (Two Numerical Columns)
# What relationship exists between restaurant latitude and longitude?
sns.scatterplot(data=df, x='latitude', y='longitude')
plt.title('Relationship between latitude and longitude')
plt.show()

# Are there any clusters or unusual location patterns when comparing latitude and longitude?
# yes a cluster with unusal points

# 📈 Comparison (One Numerical + One Categorical)
# Compare the average latitude of the top 10 states with the most restaurants.
topTenStates = df['province'].value_counts().head(10).index
filteredDf = df.loc[df['province'].isin(topTenStates),:]
sns.set_style('whitegrid')
sns.barplot(data=filteredDf, x='province', y='latitude')
plt.title('average latitude of the top 10 states with the most restaurants')
plt.xticks(rotation=45)
plt.show()

# Compare the average longitude of the top 10 restaurant chains.
topTenRestaurant = df['name'].value_counts().head(10).index
filterDf2 = df.loc[df['name'].isin(topTenRestaurant),:]
sns.barplot(data=filterDf2, x='name', y='longitude')
plt.title('average longitude of the top 10 restaurant chains')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Which city has the highest average latitude among the top 10 cities with the most restaurants?
topTenCities = df['city'].value_counts().head(10).index
filterDf3 = df.loc[df['city'].isin(topTenCities),:]
sns.barplot(data=filterDf3, x='city', y='latitude')
plt.title('highest average latitude among the top 10 cities with the most restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📦 Composition / Frequency (Categorical)
# Which 10 restaurant chains have the highest number of locations?
highestNumberOfLocations = df['name'].value_counts().head(10).index
filterDf4 = df.loc[df['name'].isin(highestNumberOfLocations),:]
sns.countplot(data=filterDf4, x='name')
plt.title('10 restaurants with highest number of locations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Which 10 states have the highest number of restaurants?
highestNumberOfRestaurants = df['province'].value_counts().head(10).index
filterDf5 = df.loc[df['province'].isin(highestNumberOfRestaurants),:]
sns.countplot(data=filterDf5, x='province')
plt.title('10 states with highest number of restaurants')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
