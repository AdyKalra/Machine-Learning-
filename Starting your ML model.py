import pandas as pd

# save filepath to variable for easier access
main_file_path = '../input/train.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(main_file_path)

# print a summary of the data in Melbourne data
print(melbourne_data.describe())

# print all columns 
print(melbourne_data.columns)

# store the series of prices separately as melbourne_yearbuilt_data.
melbourne_yearbuilt_data = melbourne_data.YearBuilt

# the head command returns the top few lines of data.
print(melbourne_yearbuilt_data.head())

#Selecting two columns from data
columns_of_interest = ['LotArea', 'YearBuilt']
two_columns_of_data = melbourne_data[columns_of_interest]

#print a summary of two columns selected in the subset of the dataframe
two_columns_of_data.describe()


#Choosing the Prediction Target 
y = melbourne_data.SalePrice
print(y.head())

# Choosing predictors
melbourne_predictors = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

x = melbourne_data[melbourne_predictors]
                        
#importing Decision Tree model from the scikit learn tree library
from sklearn.tree import DecisionTreeRegressor

# Define model
melbourne_model = DecisionTreeRegressor()

# Fit model
melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))


#The calculation of mean absolute error in the Melbourne data is
# import MAE from scikitlearn metrics library
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(x)
mean_absolute_error(y, predicted_home_prices)

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both predictors and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_x, val_x, train_y, val_y = train_test_split(x, y,random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_x, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_x)
print(mean_absolute_error(val_y, val_predictions))
