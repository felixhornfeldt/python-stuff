import pandas as pd

data = pd.read_csv('./train.csv')

# p_desc = data.describe()

# print(p)

# print(data.columns)

# data = data.dropna(axis=0)
# print(data)

y = data.SalePrice
x = data[['Id', 'SalePrice']]

# print(x.describe())
# print(x.head())
# print(y)