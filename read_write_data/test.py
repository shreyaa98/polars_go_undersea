# import polars as pl
# df = pl.read_ndjson('C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\amoeba_sector.json') 
# print(df)


# import json
# import polars as pl

# with open("C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\amoeba_sector.json") as f:
#     data = json.load(f)

# rows = [
#     {col: data[col][idx] for col in data}
#     for idx in data["name"]
# ]

# df = pl.DataFrame(rows)
# print(df)


# import json
# import polars as pl

# with open("C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\amoeba_sector.json") as f:
#     data = json.load(f)

# df = pl.DataFrame(data).transpose(include_header=True)
# print(df)



# from sqlalchemy import create_engine

# # df = pl.read_csv('C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\panda_sector.csv', separator=',', has_header=True)
# # df = pl.read_excel('C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\penguin_sector.xlsx', engine='fastexcel')


# import polars as pl
# from sqlalchemy import create_engine

# engine = create_engine("postgresql://user:psw@host:port/dbname")

# df = pl.read_database(
#     "SELECT * FROM penguins",
#     engine
# )


import pandas as pd

# # # df = pd.read_excel('C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\penguin_sector.xlsx')
# # # print(df.columns)

# df = pl.read_json('C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\amoeba_sector.json').unnest(df.columns)
# print(df)


# df = pd.read_json('C:\\Users\\shrey\\pandas_go_to_space\\read_write_data\\amoeba_sector.json') 
# print(df)


# from sqlalchemy import create_engine

# engine = create_engine(
#     "postgresql://postgres:1234@localhost:5432/testdb"
# )
# query = "SELECT * FROM penguins"
# df = pd.read_sql(query, engine)
# print(df.head())


# import pandas as pd

# df1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
# df2 = pd.DataFrame({"a": [5, 6], "b": [7, 8]})

# df = pd.concat([df1, df2])
# df.to_excel("planets_pandas_index.xlsx")
# print(df)

import polars as pl

# df1 = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
# df2 = pl.DataFrame({"a": [5, 6], "b": [7, 8]})

# df = pl.concat([df1, df2])
# df.write_excel("planets_polars.xlsx")
# print(df)


df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "bak", "baz"]})
df.write_excel("hmm.xlsx")