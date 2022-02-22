# Initial imports
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

%matplotlib inline

# Reading whale returns
# Rading the whale returs dataset using the pandas built in function read_csv and converting the Date column into datetime format.
df = pd.read_csv('./Resources/whale_returns.csv',index_col="Date", parse_dates=True, infer_datetime_format=True)
df.sort_index(axis=0)

# Count nulls
# Checking the null values and counting them using pandas built in function sum.
df.isnull().sum().sum()

# Drop nulls
# Droping the row which contain null values using pandas build in function dropna.
df.dropna(inplace=True)

# Reading algorithmic returns
# Rading the algorithmic returns dataset using the pandas built in function read_csv and converting the Date column into datetime format.
df_algo = pd.read_csv('./Resources/algo_returns.csv',index_col="Date", parse_dates=True, infer_datetime_format=True)
df_algo.sort_index(axis=0)

# Count nulls
# Checking the null values and counting them using pandas built in function sum.
df_algo.isnull().sum().sum()


# Drop nulls
# Droping the row which contain null values using pandas build in function dropna.
df_algo.dropna(inplace=True)

# Reading S&P 500 Closing Prices
# Rading the S&P 500 Closing Prices dataset using the pandas built in function read_csv and converting the Date column into datetime format
df_SP = pd.read_csv('./Resources/sp500_history.csv',index_col="Date", parse_dates=True, infer_datetime_format=True)
df_SP['Close'] = df_SP['Close']
df_SP.sort_index(axis=0)
# Check Data Types
# Checking the data type of the specific column using the dtype.
data_type=df_SP['Close'].dtype
# Fix Data Types
# Removing the special character from the Close column and converting it into float.
df_SP['Close'] = df_SP['Close'].str.replace(r'\D','').astype(float)
# Calculate Daily Returns
# Calculating the daily returns using the pct_change function.
df_SP['Close']  = df_SP['Close'].pct_change()
# Drop nulls
# Droping the row which contain null values using pandas build in function dropna.
df_SP.dropna(inplace=True)

