import pandas as pd

# save filepath to variable for easier access
main_file_path = '../input/train.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(main_file_path)

# print all columns 
print(melbourne_data.columns)

# print a summary of the data in Melbourne data
print(melbourne_data.describe())
