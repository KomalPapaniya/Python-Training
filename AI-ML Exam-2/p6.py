# importing necessary libraries 
import pandas as pd

# reading and displaying the csv file
df = pd.read_csv('ML-1-1Use-1-210720201428.csv')
# print(df.head())

# finding the shape of dataframe
# print(df.shape)

# checking null values in the entire dataframe
print(df.isnull().sum().sum())

# Filtering Data based on columns...
FFTs = df.loc[:,['FFT' in i for i in df.columns]]
print(FFTs.head(5))

# Calculating the sum of 4 contiguous rows...
contiguous_sum = FFTs.groupby(FFTs.index // 4).transform('sum')
print(contiguous_sum.head())

# removing duplicate rows...
final_df = contiguous_sum.iloc[::4, :]
print(final_df.head())

# resetting index...
final_df.reset_index(drop=True, inplace=True)
print(final_df)
