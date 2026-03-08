import pandas as pd
df = pd.read_csv('C:\\Users\\shrey\\pandas_go_to_space\\inspect_data_frames\\ship_inspection.csv')
# print(df.head(5))
# print(df.tail(5))
# print(df.shape)
# print(df.dtypes)
# print(df.info())
# print(df['security'].value_counts())
print(df['security'].unique())


import polars as pl
df = pl.read_csv('C:\\Users\\shrey\\pandas_go_to_space\\inspect_data_frames\\ship_inspection.csv', row_index_name='index')
# print(df.head(5))
# print(df.tail(5))
# print(df.shape)
# print(df.dtypes)
# print(df.estimated_size('mb'))
# print(df['security'].value_counts())
print(df['security'].unique())
