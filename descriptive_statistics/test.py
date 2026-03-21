import seaborn as sns
import pandas as pd
import polars as pl

df = sns.load_dataset("penguins")
# # df_pl = pl.DataFrame(df)

# bill_length =  df["bill_length_mm"].mean()
# print(bill_length)

# by_species = df.groupby("species")["bill_length_mm"].mean()
# print(by_species)

# bill_length_1 = df["bill_length_mm"].median()
# print(bill_length_1)

df.loc[1, "bill_length_mm"] = 2000
# print(df["bill_length_mm"].mean())


# df = df.with_columns(
#     pl.when(pl.arange(0, df.height) == 1)
#       .then(2000)
#       .otherwise(pl.col("bill_length_mm"))
#       .alias("bill_length_mm")
# )

# species = df["species"].mode()
# print(species)

# plot = df["bill_length_mm"].hist(bins=20)
# print(plot)

# species = pd.get_dummies(df["species"]) 
# print(species)

# species1 = df_pl.select(pl.col("species").to_dummies())
# print(species1)


# df2 = pd.concat([df, species], axis=1)
# print(df2)  



