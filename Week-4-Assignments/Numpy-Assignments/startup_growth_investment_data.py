import numpy as np

# Section A: Loading Data & Basic Exploration

# Load the columns Investment Amount (USD), Valuation (USD), Number of Investors, and Growth Rate (%) from the CSV into separate 1D NumPy arrays using np.genfromtxt.
startups, fundingRounds, investmentAmount, valuation, noOfInvestors, growthRate = np.genfromtxt(r'Week-4-Assignments\Numpy-Assignments\startup_growth_investment_data.csv', delimiter=',', usecols=(0,2,3,4,5,8), skip_header=1, dtype=None, unpack=True)

# Print the shape, size, and dtype of the Investment Amount (USD) array.
print(f"Shape of investment amount: {investmentAmount.shape}")
print(f"Size of investment amount: {investmentAmount.size}")
print(f"dtype of investment amount: {investmentAmount.dtype}")

# Print the first 10 and last 10 values of the Valuation (USD) array.
print(f"First 10 values of the Valuation (USD) array: {valuation[0:10]}")
print(f"Last 10 values of the Valuation (USD) array: {valuation[-10:]}")

# Section B: Statistical Operations

# Calculate the mean, median, and standard deviation of Investment Amount (USD).
print(f"Mean of Investment Amount (USD): {np.mean(investmentAmount):.2f}")
print(f"Median of Investment Amount (USD): {np.median(investmentAmount):.2f}")
print(f"Std of Investment Amount (USD): {np.std(investmentAmount):.2f}")

# Calculate the 25th, 50th, and 75th percentiles of Valuation (USD).
print(f"25th percentile of valuation is: {np.percentile(valuation,25):.2f}")
print(f"50th percentile of valuation is: {np.percentile(valuation,50):.2f}")
print(f"75th percentile of valuation is: {np.percentile(valuation,75):.2f}")

# Find the minimum and maximum Growth Rate (%) in the dataset.
print(f"Minimum growth rate: {np.min(growthRate):.2f}")
print(f"Maximum growth rate: {np.max(growthRate):.2f}")

# Calculate the average number of investors across all startups.
print(f"Average number of investors across all startups: {np.average(noOfInvestors):.2f}")

# Find the range (max - min) of Investment Amount (USD).
print(f"Range of Investment Amount (USD): {np.max(investmentAmount)-np.min(investmentAmount):.2f}")

# Section C: Mathematical Operations

# Compute the square of every value in the Number of Investors array.
print(f"Square of every value in the Number of Investors array: {np.square(noOfInvestors)}")

# Compute the square root of every value in Investment Amount (USD).
print(f"Square root of every value in Investment Amount (USD): {np.sqrt(investmentAmount)}")

# Compute the absolute difference between Valuation (USD) and Investment Amount (USD) for every startup.
print(f"Absolute difference between Valuation (USD) and Investment Amount (USD) for every startup: {np.abs(valuation-investmentAmount)}")

# Raise every value in Growth Rate (%) to the power of 2.
print(f"Raise every value in Growth Rate (%) to the power of 2: {np.pow(growthRate,2)}")

# Section D: Arithmetic Operations & Broadcasting

# Create a new array representing the "Return Multiple" by dividing Valuation (USD) by Investment Amount (USD) element-wise.
returnMultiple = valuation / investmentAmount
print(f"Dividing Valuation (USD) by Investment Amount (USD) element-wise: {returnMultiple}")

# Add a flat 5% increase to every value in Growth Rate (%) using broadcasting (i.e., add a scalar to the whole array).
increasedGrowthRate = growthRate * 1.05
print(f"Old growth rate: {growthRate[:5]}")
print(f"Increased growth rate: {increasedGrowthRate[:5]}")

# Subtract the mean Investment Amount (USD) from every element in the Investment Amount (USD) array (mean-centering using broadcasting).
updatedInvestmentAmount = investmentAmount - np.mean(investmentAmount)
print(f"Subtract the mean Investment Amount (USD) from every element in the Investment Amount (USD) array (mean-centering using broadcasting): {updatedInvestmentAmount}")

# Multiply Funding Rounds and Number of Investors arrays element-wise to create a new array called Engagement Score.
engagementScore = fundingRounds * noOfInvestors
print(f"Engagement score: {engagementScore}")

# Divide Valuation (USD) by 1,000,000 (broadcasting a scalar) to convert it into millions.
print(f"Divide Valuation (USD) by 1,000,000 (broadcasting a scalar) to convert it into millions: {valuation/1000000}")

# Section E: Trigonometric, Exponential, and Logarithmic Functions

# Divide Growth Rate (%) by np.pi and add 1 to create a new array growthPie.
growthPie = (growthRate / np.pi) + 1
print(f"Growth pie: {growthPie}")

# Calculate the sine, cosine, and tangent values of growthPie.
print(f"Sin of growth pie: {np.sin(growthPie)}")
print(f"Cos of growth pie: {np.cos(growthPie)}")
print(f"Tan of growth pie: {np.tan(growthPie)}")

# Calculate the exponential values of growthPie.
print(f"Exponential values of growthPie: {np.exp(growthPie)}")

# Calculate the natural logarithm and base-10 logarithm of growthPie.
print(f"Natural log: {np.log(growthPie)}")
print(f"Base-10 log: {np.log10(growthPie)}")

# Calculate the hyperbolic sine, hyperbolic cosine, and hyperbolic tangent of growthPie.
print(f"Sinh of growth pie: {np.sinh(growthPie)}")
print(f"Cosh of growth pie: {np.cosh(growthPie)}")
print(f"Tanh of growth pie: {np.tanh(growthPie)}")

# Calculate the inverse hyperbolic sine and inverse hyperbolic cosine of growthPie.
print(f"Inverse Sinh of growth pie: {np.arcsinh(growthPie)}")
print(f"Inverse Cosh of growth pie: {np.arccosh(growthPie)}")

# Section F: 2D Arrays, Indexing & Slicing

# Create a 2D array named FundingValuation2D by stacking Investment Amount (USD) and Valuation (USD) using np.array([...]).
FundingValuation2D = np.array([investmentAmount,valuation])
print(f"FundingValuation2D: {FundingValuation2D}")

# Print the ndim, size, shape, and dtype of FundingValuation2D.
print(f"ndim of FundingValuation2D: {FundingValuation2D.ndim}")
print(f"size of FundingValuation2D: {FundingValuation2D.size}")
print(f"shape of FundingValuation2D: {FundingValuation2D.shape}")
print(f"dtype of FundingValuation2D: {FundingValuation2D.dtype}")

# Slice FundingValuation2D to get only the first row and the first 10 columns.
print(f"Slice FundingValuation2D to get only the first row and the first 10 columns: {FundingValuation2D[0,:10]}")

# Slice FundingValuation2D to get columns 5 through 20 with a step of 3, for both rows.
slicedArray = FundingValuation2D[:,5:21:3]
print(f"Slice FundingValuation2D to get columns 5 through 20 with a step of 3, for both rows: {slicedArray}")

# From the slice in Q26, extract only a single specific element (e.g., the 5th value) using indexing.
firstRowFirst10Cols = FundingValuation2D[0,:10]
print(f"From the slice in Q26, extract only a single specific element (e.g., the 5th value) using indexing: {firstRowFirst10Cols[4]}")

# From the slice in Q27, extract only a single specific element using indexing.
print(f"From the slice in Q27, extract only a single specific element (e.g., the 5th value) using indexing: {slicedArray[0,0]}")

# Section G: Iterating Arrays

# Use np.nditer to iterate through all elements of FundingValuation2D and print each one.
for i in np.nditer(FundingValuation2D):
    print(i)

# Use np.ndenumerate to iterate through FundingValuation2D and print both the index and the element.
for index, value in np.ndenumerate(FundingValuation2D):
    print(index,value)

# Section H: Reshaping

# Reshape FundingValuation2D (which has 2 rows and 5000 columns) into a shape of (1, 10000).
reshapedArray = np.reshape(FundingValuation2D, (1,-1))
print(f"Reshape FundingValuation2D (which has 2 rows and 5000 columns) into a shape of (1, 10000): {reshapedArray}")

# Print the size, ndim, and shape of the reshaped array from Q32.
print(f"Size of reshaped array: {reshapedArray.size}")
print(f"ndim of reshaped array: {reshapedArray.ndim}")
print(f"shape of reshaped array: {reshapedArray.shape}")

# Reshape FundingValuation2D into a shape of (10, 1000) and print its shape.
reshapedArrayTwo = np.reshape(FundingValuation2D,(10,-1))
print(reshapedArrayTwo)
print(f"Size of reshaped array: {reshapedArrayTwo.size}")
print(f"ndim of reshaped array: {reshapedArrayTwo.ndim}")
print(f"shape of reshaped array: {reshapedArrayTwo.shape}")

# Section I: Boolean Masking & Filtering

# Create a boolean mask that identifies which startups have a Growth Rate (%) greater than 100, then use it to filter and print the corresponding Investment Amount (USD) values.
growthRateMask = growthRate > 100
print(f"Startups having growth rate greater than 100: {growthRate[growthRateMask]}")

# Filter and print all Valuation (USD) values where Number of Investors is greater than 40.
noOfInvestorsMask = noOfInvestors > 40
print(f"Filter evaluation where number of investors is greater than 40: {valuation[noOfInvestorsMask]}")

# Create a boolean mask for startups where Funding Rounds is exactly 5, and use it to count how many such startups exist.
fundingRoundsMask = fundingRounds == 5
count = startups[fundingRoundsMask]
print(f"Startups where Funding Rounds is exactly 5: {len(count)}")

# Filter out all Investment Amount (USD) values that fall below the 25th percentile calculated in Q5's equivalent for this column.
investmentAmount25thPercentile = np.percentile(investmentAmount,25)
investmentAmountMask = investmentAmount < investmentAmount25thPercentile
print(f"Filter out all Investment Amount (USD) values that fall below the 25th percentile calculated in Q5's equivalent for this column: {investmentAmount[investmentAmountMask]}")

# Using boolean masking, replace all Growth Rate (%) values below 0 (if any) with 0 in a copy of the array.
growthRateCopy = growthRate.copy()
growthRateCopy[growthRateCopy < 0] = 0
print(f"Growth rate with negatives replaced by 0: {growthRateCopy}")

# Section J: Fancy Indexing

# Using fancy indexing, extract the Valuation (USD) values at index positions [0, 10, 50, 100, 999].
print(f"Fancy indexing: {valuation[[0, 10, 50, 100, 999]]}")

# Create an array of indices where Growth Rate (%) is in the top 10 highest values, then use fancy indexing to extract the corresponding Investment Amount (USD) values.
top10Indices = np.argsort(growthRate)[-10:]
print(f"Indices of top 10 growth rates: {top10Indices}")
print(f"Corresponding Investment Amount (USD) values: {investmentAmount[top10Indices]}")

# Use fancy indexing on FundingValuation2D to select rows [0, 1] and columns [2, 4, 6, 8] simultaneously.
print(FundingValuation2D[np.ix_([0,1],[2,4,6,8])])