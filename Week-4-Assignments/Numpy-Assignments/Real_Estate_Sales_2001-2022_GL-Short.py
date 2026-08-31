import numpy as np

# Level 1 — Loading and Inspection
#Q1
# Load only the following numeric columns into a NumPy array:

# List Year
# Assessed Value
# Sale Amount
# Sales Ratio

listYear, assessedValue, saleAmount, salesRatio = np.genfromtxt(r'Week-4-Assignments\Numpy-Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', usecols=(1,5,6,7), unpack=True, dtype=None, skip_header=1, invalid_raise=False)

print(listYear)
print(assessedValue)
print(saleAmount)
print(salesRatio)

#Q2
# listYear, assessedValue, saleAmount, aur salesRatio ke liye alag-alag print karo:
# Shape
# Number of dimensions (ndim)
# Total number of elements (size)
# Data type (dtype)

print(f"shape of list year: {listYear.shape}")
print(f"ndim of list year: {listYear.ndim}")
print(f"size of list year: {listYear.size}")
print(f"dtype of list year: {listYear.dtype}")

print(f"shape of assessedValue: {assessedValue.shape}")
print(f"ndim of assessedValue: {assessedValue.ndim}")
print(f"size of assessedValue: {assessedValue.size}")
print(f"dtype of assessedValue: {assessedValue.dtype}")

print(f"shape of saleAmount: {saleAmount.shape}")
print(f"ndim of saleAmount: {saleAmount.ndim}")
print(f"size of saleAmount: {saleAmount.size}")
print(f"dtype of saleAmount: {saleAmount.dtype}")

print(f"shape of salesRatio: {salesRatio.shape}")
print(f"ndim of salesRatio: {salesRatio.ndim}")
print(f"size of salesRatio: {salesRatio.size}")
print(f"dtype of salesRatio: {salesRatio.dtype}")

# Q3

# Print the first 10 values of each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"list year first 10 values: {listYear[:10]}")
print(f"assessedValue first 10 values: {assessedValue[:10]}")
print(f"saleAmount first 10 values: {saleAmount[:10]}")
print(f"salesRatio first 10 values: {salesRatio[:10]}")

# Q4

# Print the last 10 values of each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"list year last 10 values: {listYear[-10:]}")
print(f"assessedValue last 10 values: {assessedValue[-10:]}")
print(f"saleAmount last 10 values: {saleAmount[-10:]}")
print(f"salesRatio last 10 values: {salesRatio[-10:]}")

# Q5

# Print values from index 100 to index 150 (inclusive) for each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"list year values from index 100 to index 150 (inclusive): {listYear[100:151]}")
print(f"assessedValue values from index 100 to index 150 (inclusive): {assessedValue[100:151]}")
print(f"saleAmount values from index 100 to index 150 (inclusive): {saleAmount[100:151]}")
print(f"salesRatio values from index 100 to index 150 (inclusive): {salesRatio[100:151]}")

# Q6

# Print every 5th value of each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"list year Print every 5th value: {listYear[::5]}")
print(f"assessedValue Print every 5th value: {assessedValue[::5]}")
print(f"saleAmount Print every 5th value: {saleAmount[::5]}")
print(f"salesRatio Print every 5th value: {salesRatio[::5]}")

# Q7

# Print all values in reverse order for each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"list year all values in reverse order: {listYear[::-1]}")
print(f"assessedValue all values in reverse order: {assessedValue[::-1]}")
print(f"saleAmount all values in reverse order: {saleAmount[::-1]}")
print(f"salesRatio all values in reverse order: {salesRatio[::-1]}")

# Q8

# Print the last 100 values of each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"list year last 100 values: {listYear[-100::]}")
print(f"assessedValue last 100 values: {assessedValue[-100::]}")
print(f"saleAmount last 100 values: {saleAmount[-100::]}")
print(f"salesRatio last 100 values: {salesRatio[-100::]}")

# Q9

# Find the minimum value of each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"List year min value: {np.min(listYear)}")
print(f"assessedvalue min value: {np.min(assessedValue):.2f}")
print(f"sale amount min value: {np.min(saleAmount):.2f}")
print(f"sales ratio min value: {np.min(salesRatio):.2f}")

# Q10

# Find the maximum value of each array:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"List year max value: {np.max(listYear)}")
print(f"assessedvalue max value: {np.max(assessedValue):.2f}")
print(f"sale amount max value: {np.max(saleAmount):.2f}")
print(f"sales ratio max value: {np.max(salesRatio):.2f}")

# Q11 (Boolean Masking Begins)

# Print all values where the Sale Amount is greater than 500000.

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

saleAmountMask = saleAmount > 500000
print(f"listYear all values where the Sale Amount is greater than 500000: {listYear[saleAmountMask]}")
print(f"assessedValue all values where the Sale Amount is greater than 500000: {assessedValue[saleAmountMask]}")
print(f"saleAmount all values where the Sale Amount is greater than 500000: {saleAmount[saleAmountMask]}")
print(f"salesRatio all values where the Sale Amount is greater than 500000: {salesRatio[saleAmountMask]}")

# Q12

# Print all properties where the Assessed Value is less than 100000.

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

assessedValueMask = assessedValue < 100000
print(f"listYear all properties where the Assessed Value is less than 100000: {listYear[assessedValueMask]}")
print(f"assessedValue all properties where the Assessed Value is less than 100000: {assessedValue[assessedValueMask]}")
print(f"saleAmount all properties where the Assessed Value is less than 100000: {saleAmount[assessedValueMask]}")
print(f"salesRatio all properties where the Assessed Value is less than 100000: {salesRatio[assessedValueMask]}")

# Q13

# Print all properties where the Sales Ratio is greater than 1.

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

salesRatioMask = salesRatio > 1
print(f"listYear all properties where the Sales Ratio is greater than 1: {listYear[salesRatioMask]}")
print(f"assessedValue all properties where the Sales Ratio is greater than 1: {assessedValue[salesRatioMask]}")
print(f"saleAmount all properties where the Sales Ratio is greater than 1: {saleAmount[salesRatioMask]}")
print(f"salesRatio all properties where the Sales Ratio is greater than 1: {salesRatio[salesRatioMask]}")

# Q14

# Print all properties where the Sale Amount is greater than the Assessed Value.

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

mask = saleAmount > assessedValue
print(f"listYear all properties where the Sale Amount is greater than the Assessed Value: {listYear[mask]}")
print(f"assessedValue all properties where the Sale Amount is greater than the Assessed Value: {assessedValue[mask]}")
print(f"saleAmount all properties where the Sale Amount is greater than the Assessed Value: {saleAmount[mask]}")
print(f"salesRatio all properties where the Sale Amount is greater than the Assessed Value: {salesRatio[mask]}")

# Q15

# Print all properties where the Sale Amount is less than the Assessed Value.

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

maskOne = saleAmount < assessedValue
print(f"listYear all properties where the Sale Amount is less than the Assessed Value: {listYear[maskOne]}")
print(f"assessedValue all properties where the Sale Amount is less than the Assessed Value: {assessedValue[maskOne]}")
print(f"saleAmount all properties where the Sale Amount is less than the Assessed Value: {saleAmount[maskOne]}")
print(f"salesRatio all properties where the Sale Amount is less than the Assessed Value: {salesRatio[maskOne]}")

# Q16

# Print all properties where the List Year is between 2005 and 2015 (inclusive).

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

maskTwo = (listYear >= 2005) & (listYear <= 2015)
print(f"listyear all properties where the List Year is between 2005 and 2015 (inclusive): {listYear[maskTwo]}")
print(f"assessed year all properties where the List Year is between 2005 and 2015 (inclusive): {assessedValue[maskTwo]}")
print(f"sale amount all properties where the List Year is between 2005 and 2015 (inclusive): {saleAmount[maskTwo]}")
print(f"sales ratio all properties where the List Year is between 2005 and 2015 (inclusive): {salesRatio[maskTwo]}")

# Q17

# Print all properties where the List Year is greater than 2020.

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

maskThree = listYear > 2020
print(f"listyear all properties where the List Year is greater than 2020: {listYear[maskThree]}")
print(f"assessed year all properties where the List Year is greater than 2020: {assessedValue[maskThree]}")
print(f"sale amount all properties where the List Year is greater than 2020: {saleAmount[maskThree]}")
print(f"sales ratio all properties where the List Year is greater than 2020: {salesRatio[maskThree]}")

# Q18

# Print all properties where both of the following conditions are true:

# Sale Amount > 300000
# Sales Ratio > 1

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

maskFour = (saleAmount > 300000) & (salesRatio > 1)
print(f"listyear all properties where saleAmount > 300000 and salesRatio > 1: {listYear[maskFour]}")
print(f"assessed year all properties where saleAmount > 300000 and salesRatio > 1: {assessedValue[maskFour]}")
print(f"sale amount all properties where saleAmount > 300000 and salesRatio > 1: {saleAmount[maskFour]}")
print(f"sales ratio all properties where the saleAmount > 300000 and salesRatio > 1: {salesRatio[maskFour]}")

# Q19

# Print all properties where either of the following conditions is true:

# Sale Amount > 300000

# OR

# Assessed Value < 100000

# Print the corresponding values from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

maskFive = (saleAmount > 300000) | (assessedValue < 100000)
print(f"listyear all properties where saleAmount > 300000 or assessedValue < 100000: {listYear[maskFive]}")
print(f"assessed year all properties where saleAmount > 300000 or assessedValue < 100000: {assessedValue[maskFive]}")
print(f"sale amount all properties where saleAmount > 300000 or assessedValue < 100000: {saleAmount[maskFive]}")
print(f"sales ratio all properties where the saleAmount > 300000 or assessedValue < 100000: {salesRatio[maskFive]}")

# Q20

# Count how many properties have a Sale Amount greater than 500000.

# Important: Don't print the properties themselves. Only print the total count.

maskSix = saleAmount > 500000
saleAmountFilter = saleAmount[maskSix]
print(f"properties have a Sale Amount greater than 500000: {len(saleAmountFilter)}")

# Q21

# Find the average (mean) of the saleAmount array.

averageSaleAmount = np.mean(saleAmount)
print(f"Average sale amount is: {averageSaleAmount:.2f}")

# Q22

# Find the median of the assessedValue array.

medianAssessedValue = np.median(assessedValue)
print(f"Median of assessed value is: {medianAssessedValue:.2f}")

# Q23

# Find the standard deviation of the salesRatio array.

stdSalesRatio = np.std(salesRatio)
print(f"Standard deviation of sales ratio is: {stdSalesRatio:.2f}")

# Q24

# Find the 25th percentile of the saleAmount array.

saleAmount25thPercentile = np.percentile(saleAmount,25)
print(f"25th percentile of the saleAmount array: {saleAmount25thPercentile}")

# Q25

# Find the 50th percentile of the saleAmount array.

saleAmount50thPercentile = np.percentile(saleAmount,50)
print(f"50th percentile of the saleAmount array: {saleAmount50thPercentile}")

# Q26

# Find the 75th percentile of the saleAmount array.

saleAmount75thPercentile = np.percentile(saleAmount,75)
print(f"75th percentile of the saleAmount array: {saleAmount75thPercentile}")

# Q27

# Find the total Sale Amount of all properties.

totalSaleAmount = np.sum(saleAmount)
print(f"Total sale amount of all properties: {totalSaleAmount}")

# Q28

# Find the average Sale Amount for each List Year.

# Print the year along with its average sale amount.

uniqueListYear = np.unique(listYear)
for year in uniqueListYear:
    mask = (listYear == year)
    avg = np.mean(saleAmount[mask])
    print(f"year: {year}, avg: {avg}")

# Q29

# Find the List Year that has the highest average Sale Amount.
# Print:
# List Year
# Average Sale Amount

yearArray = np.array([])
meanArray = np.array([])
uniqueListYear = np.unique(listYear)
for year in uniqueListYear:
    mask = (listYear == year)
    avg = np.mean(saleAmount[mask])
    yearArray = np.append(yearArray,year)
    meanArray = np.append(meanArray,avg)
maxIndex = np.argmax(meanArray)
print(f"Year with highest avg sale amount: {yearArray[maxIndex]}, avg: {meanArray[maxIndex]}")

# Q30

# Find the List Year that has the highest number of property sales.

# Print:

# List Year
# Number of Sales

yearArrayTwo = np.array([])
countArray = np.array([])
for year in uniqueListYear:
    mask = (listYear == year)
    yearArrayTwo = np.append(yearArrayTwo, year)
    countArray = np.append(countArray, np.sum(mask))
maxIndex = np.argmax(countArray)
print(f"Year with highest no of propert sale: {yearArrayTwo[maxIndex]}, no of property sale: {countArray[maxIndex]}")

# Q31

# Print the top 10 highest Sale Amounts.

highestSaleAmounts = np.sort(saleAmount)[::-1][:10]
print(highestSaleAmounts)

# Q32

# Print the indices of the top 10 highest Sale Amounts.

highestSaleAmountsIndices = np.argsort(saleAmount)[::-1][:10]
print(highestSaleAmountsIndices)

# Q33

# Using the indices obtained in Q32, print the complete information of those properties from all four arrays:

# listYear
# assessedValue
# saleAmount
# salesRatio

print(f"List year: {listYear[highestSaleAmountsIndices]}")
print(f"assessedValue: {assessedValue[highestSaleAmountsIndices]}")
print(f"saleAmount: {saleAmount[highestSaleAmountsIndices]}")
print(f"salesRatio: {salesRatio[highestSaleAmountsIndices]}")

# Q34

# Print the top 10 highest Sale Amounts in descending order, along with:

# listYear
# assessedValue
# saleAmount
# salesRatio

saleAmountDescOrder = np.sort(saleAmount)[-1:-11:-1]
print(saleAmountDescOrder)
saleAmountDescOrderIndices = np.argsort(saleAmount)[-1:-11:-1]
print(listYear[saleAmountDescOrderIndices])
print(assessedValue[saleAmountDescOrderIndices])
print(saleAmount[saleAmountDescOrderIndices])
print(salesRatio[saleAmountDescOrderIndices])

# Q35

# Find the indices where the Sale Amount is greater than 500000.

# Print only the indices.

saleAmountIndices = np.where(saleAmount > 500000)
print(saleAmountIndices)

# Q36

# Find the indices where the Sales Ratio is less than 1.

# Print only the indices.

salesRatioIndices = np.where(salesRatio < 1)
print(salesRatioIndices)

# Q37

# Using np.where(), replace every Sales Ratio less than 1 with 1.

# Print the modified array.

updatedSalesRatio = np.where(salesRatio < 1, 1, salesRatio)
print(updatedSalesRatio)

# Q38

# Using np.where(), replace every Sale Amount greater than 1000000 with 1000000.

# Print the modified array.

updatedSaleAmount = np.where(saleAmount > 1000000, 1000000, saleAmount)
print(updatedSaleAmount)

# Q39

# Using np.where(), create a new array that contains:

# "High" if Sale Amount > 500000
# "Low" otherwise.

# Print the new array.

updatedSaleAmountTwo = np.where(saleAmount > 500000, "High", "Low")
print(updatedSaleAmountTwo)

# Q40

# Find the indices where both of the following conditions are true:

# Sale Amount > 500000
# Sales Ratio > 1

# Print only the indices.

indices = np.where((saleAmount > 500000) & (salesRatio > 1))
print(indices)

# Q41

# Using np.take(), print the first 20 Sale Amounts.

print(np.take(saleAmount, range(20)))

# Q42

# Using np.take(), print the last 20 Assessed Values.
print(np.take(assessedValue, range(-20,0)))

# Q43

# Using np.take(), print the Sale Amounts at the following indices:

# [5, 25, 50]

print(np.take(saleAmount, [5, 25, 50]))

# Q44

# Using np.take(), print the corresponding List Years for the indices used in Q43.

print(np.take(listYear, [5, 25, 50]))

# Q45

# Create a 2D NumPy array named propertyData by combining the following arrays in this order:

# listYear
# assessedValue
# saleAmount
# salesRatio

# Each row should represent one property.

# Print:

# Shape
# First 5 rows

propertyData = np.array([
    listYear,
    assessedValue,
    saleAmount,
    salesRatio
]).T

print(propertyData.shape)
print(propertyData[:5])

# Q46

# Print the first 10 rows of propertyData.

print(propertyData[:10])

# Using fancy indexing, print only the following columns from propertyData:

# List Year
# Sale Amount

print(propertyData[:,[0,2]])

# Q48

# Print rows 100 to 120 (inclusive) from propertyData.

print(propertyData[100:121])

# Q49

# Print every 10th row from propertyData.
print(propertyData[::10])

# Q50

# Using fancy indexing, print the following rows from propertyData:

# [0, 10, 20, 30, 40]
print(propertyData[[0, 10, 20, 30, 40]])

# Q51

# Using fancy indexing, print the following columns from all rows of propertyData:

# [1, 3]
print(propertyData[:,[1,3]])

# Q52

# Using np.ix_(), print the following rows and columns simultaneously:

# Rows:

# [5, 10, 15, 20]

# Columns:

# [0, 2]

print(propertyData[np.ix_([5, 10, 15, 20], [0, 2])])

# Q53

# Using np.ix_(), print the following rows and columns simultaneously:

# Rows:

# [50, 100]

# Columns:

# [1, 2, 3]

print(propertyData[np.ix_([50, 100], [1, 2, 3])])

# Q54 (Final Challenge)

# Find the top 5 properties with the highest Sale Amount.

# Print the complete information for each property:

# List Year
# Assessed Value
# Sale Amount
# Sales Ratio

mask = np.argsort(saleAmount)[::-1][:5]
print(listYear[mask])
print(assessedValue[mask])
print(saleAmount[mask])
print(salesRatio[mask])