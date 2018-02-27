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


# Choosing the Prediction Target

You have the code to load your data, and you know how to index it. You are ready to choose which column you want to predict. This column is called the prediction target. There is a convention that the prediction target is referred to as y. Here is an example doing that with the example data.

y = melbourne_data.Price
Choosing Predictors
Next we select the predictors. Sometimes, you will want to use all of the variables except the target..

It's possible to model with non-numeric variables, but we'll start with a narrower set of numeric variables. In the example data, the predictors will be chosen as:

In [3]:
melbourne_predictors = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
                        
By convention, this data is called X.


## Building Your Model
You will use the scikit-learn library to create your models. When coding, this library is written as sklearn, as you will see in the sample code. Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.

The steps to building and using a model are:

### Define: 
What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
### Fit: 
Capture patterns from provided data. This is the heart of modeling.
### Predict: 
Just what it sounds like
### Evaluate: 
Determine how accurate the model's predictions are.
