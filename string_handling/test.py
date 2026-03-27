# # ### Pandas Version

import pandas as pd
import re

text = """pokhrEYLMLAohprrr ploWdoBRKledYprrr"""

df = pd.DataFrame({'text': [text]})
print(df)

words = df["text"].str.split()
print(words)

s = words.explode()
print(s)

df1 = pd.DataFrame({"words": s}).reset_index(drop=True)
print(df1)

slice = df1["words"].str[3:]
print(slice)

# slice1 = df1["words"].str[1:-4:2].str.lower().str[1:]
# print(slice1)

# lower_Case = df1["words"].str.lower()
# print(lower_Case)

# lower_Case = df1["words"].str.upper()
# print(lower_Case)

reg = df1['words'].str.findall(r'h.e.l.l.o', re.IGNORECASE)
print(reg)

# Polars Version

import polars as pl

text = """pokhrEYLMLAohprrr ploWdoBRKledYprrr"""

dfp = pl.DataFrame({'text': [text]})
print(dfp)

words1 = dfp.select(pl.col("text").str.split(" ").alias("words"))
print(words1)
    
s1 = words1.explode("words")
print(s1)

dfp1 = s1.with_row_index()
print(dfp1)

slice_polars = dfp1.select(pl.col("words").str.slice(3))
print(slice_polars)

d = dfp1.select(
       pl.col("words").map_elements(
           lambda x: x[1:-4:2]
       )
   )
print(d)

lower_Case = dfp1.select(pl.col("words").str.to_lowercase())
print(lower_Case)

lower_Case = dfp1.select(pl.col("words").str.to_uppercase())
print(lower_Case)

sentence = dfp1.select(pl.col("words").str.join("welcome")).item()
print(sentence)


length = dfp1.select(pl.col("words").str.len_chars())
print(length)

reg = dfp1.select(
    pl.col("words").str.extract_all(r'(?i)(h.e.l.l.o)')
)
print(reg)

