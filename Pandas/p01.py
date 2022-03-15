import pandas as pd
import numpy as np

# reading csv file
data = pd.read_csv("Automobile_data.csv")

# printing data of first 5 rows
print(data.head())

# printing data of last 5 rows
print(data.tail())

# ----------------------------------------------------------------------------------------------------------

# data cleaning: replacing all '?' with NaN
data = data.replace('?', np.NaN)
print(data)

# ----------------------------------------------------------------------------------------------------------

# updating the csv file
data.to_csv("Automobile_data.csv", index=False)

# ----------------------------------------------------------------------------------------------------------

print(data.info())

# Find the most expensive car company name
most_exp_car = data.loc[data['price'].idxmax(), 'make']
print(most_exp_car)

# ----------------------------------------------------------------------------------------------------------

# Print All Toyota Cars details
toyota = data[data['make']=='toyota']
print(toyota)

# ----------------------------------------------------------------------------------------------------------

# Count total car per company
company_wise_total_cars = data.groupby('make').size()
print(company_wise_total_cars)

# ----------------------------------------------------------------------------------------------------------

# Find each company’s Highest price car
highest_priced_cars = data.groupby('make')['price'].max()
print(highest_priced_cars)

# ----------------------------------------------------------------------------------------------------------

# Find the average mileage of each car making company

# average city mileage of each car making company
city_avg = data.groupby('make')['city-mpg'].mean()
print(city_avg)

# average city mileage of each car making company
hwy_avg = data.groupby('make')['highway-mpg'].mean()
print(hwy_avg)

# overall average of each car making company

# creating new column "total mileage" containing average of city and highway mileage
data['total mileage'] = data.apply(lambda row: (row['city-mpg']  + row['highway-mpg'])/2, axis=1)
print(data)

avg = data.groupby('make')['total mileage'].mean()
print(avg)

# ----------------------------------------------------------------------------------------------------------

# Sort all cars by Price column
sorted_by_price = data.sort_values(by=("price"))
print(sorted_by_price)