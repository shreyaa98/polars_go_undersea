### Pandas Version
import pandas as pd
df = pd.read_csv('C:\\Users\\shrey\\polars_go_to_space\\data_wrangling\\cargo.csv')
# df.sort_values(by="category", inplace=True)
# print(df)

df.sort_values(by=["category", "type"], ascending=[True, False], inplace=True)
print(df)




### Polars Version
import polars as pl
df = pl.read_csv('C:\\Users\\shrey\\polars_go_to_space\\data_wrangling\\cargo.csv')
# df = df.sort(by="category")
# print(df)
df.sort(by=["category", "type"], descending=[False, True], nulls_last=True)
print(df)