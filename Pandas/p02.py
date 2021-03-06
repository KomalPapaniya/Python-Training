import numpy as np
import pandas as pd

# Pandas program to create today's date
today_dt = pd.to_datetime('today')
print(today_dt)

# ---------------------------------------------------------------------------------------------------------

# Pandas program to calculate all the sighting days of the unidentified flying object (ufo) from the current date.
ufo_data = pd.read_csv("ufo_sighting_data.csv")
print(ufo_data.head())

print(ufo_data.info())

# changing 'Date_time' column datatype from object to datetime64
ufo_data['Date_time'] = ufo_data['Date_time'].str.replace('24.00', '00:00')

ufo_data['Date_time'] = pd.to_datetime(ufo_data['Date_time'])
print(ufo_data.info())
# print(ufo_data.head())

# getting date from user
dt = input('Enter date in YYYY-MM-DD format: ')

# finding data of sighting days of the unidentified flying object (ufo) from the given date
condition = (ufo_data['Date_time'] > dt)
print(ufo_data.loc[condition])

# calculating all the sighting days of the unidentified flying object (ufo) from the given date
print("ufo appeared",len(ufo_data.loc[condition]), 'times after', dt)