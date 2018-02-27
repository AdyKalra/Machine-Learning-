# Interpreting Data Description

DataFrameVariable.describe()

The results show 8 numbers for each column in your original dataset. The first number, the count, shows how many rows have non-missing values.

Missing values arise for many reasons. For example, the size of the 2nd bedroom wouldn't be collected when surveying a 1 bedroom house. We'll come back to the topic of missing data.

The second value is the mean, which is the average. Under that, std is the standard deviation, which measures how numerically spread out the values are.

To interpret the min, 25%, 50%, 75% and max values, imagine sorting each column from lowest to highest value. The first (smallest) value is the min. If you go a quarter way through the list, you'll find a number that is bigger than 25% of the values and smaller than 75% of the values. That is the 25% value (pronounced "25th percentile"). The 50th and 75th percentiles are defined analgously, and the max is the largest number.

# Selecting and Filtering Data

Before we can choose variables/columns, it is helpful to see a list of all columns in the dataset. That is done with the columns property of the DataFrame (the bottom line of code below).

Selecting a Single Column¶
You can pull out any variable (or column) with dot-notation. This single column is stored in a Series, which is broadly like a DataFrame with only a single column of data. Here's an example: 

### store the series of prices separately as melbourne_price_data.
melbourne_price_data = melbourne_data.Price
### the head command returns the top few lines of data.
print(melbourne_price_data.head())
