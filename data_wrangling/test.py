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

# Sort rows
df = df.sort("category")

df = df.sort(
    by=["category", "type"],
    descending=[False, True],
    nulls_last=True
)

df = df.sort("units", descending=True)

df = df.sort(["type", "uuid"])

# Change data type
df = df.with_columns(
    crate_str=pl.col("crate_no").cast(pl.Utf8)
)

df = df.with_columns(
    pl.col("units").cast(pl.Int64)
)

df = df.with_columns(
    pl.col("crate_no").cast(pl.Float64)
)

# Combine columns
df = df.with_columns(
    (
        pl.col("crate_no").cast(pl.Utf8)
        + pl.col("crate_shelf")
    ).alias("crate_id")
)

# Create new columns
df = df.with_columns(
    pl.lit("unknown").alias("status")
)

df = df.with_columns(
    (pl.col("units") * 2).alias("double_units")
)

# Missing values
df.null_count()

df_dropped = df.drop_nulls()

df_dropped = df.drop_nulls("category")

df_fixed = df.with_columns(
    pl.col("units").fill_null(
        pl.col("units").median()
    )
)

df_fixed = df.with_columns(
    pl.col("category").fill_null("unknown")
)

df_fixed = df.with_columns(
    pl.col("units").fill_null(0)
)

# Swap rows and columns
df.transpose()

df.transpose(include_header=True)