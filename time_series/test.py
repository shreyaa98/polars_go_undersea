## Pandas Version

import datetime

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

displacement = np.random.randn(200)  

s = pd.Series(
    data=displacement,
    # index=pd.date_range("2023-03-09", freq="D", periods=200),
    index=pd.date_range("2023-03-09 08:22:00", "2023-03-09 16:00:00", periods=200),
    name="reactor_temp",
)
# print(s.head())
# ax = s.plot()
# ax.set_title("reactor_temp")
# ax.set_xlabel("time")
# ax.set_ylabel("reactor_temp")
# plt.tight_layout()
# plt.savefig("time_series/random1.png")
# plt.show()

# s1 = pd.to_datetime(
#         ["2020", "September 16th, 2020", "2020 Sep 16 11:11", "2020/09/16", "09/16/2020"],
#         dayfirst=False,
#         format="mixed")

# print(s1)


# print(s.index.year)
# print(s.index.month)
# print(s.index.hour)
# print(s.index.weekday)
# print(s.index.minute)
# print(s.index.month_name())
# print(s.index.day_name())


# print(s['1/10/2011'])
# print(s["2023-03-20":"2023-04-17"])
# print(s[datetime(2011, 1, 7):])
# print(s['1/6/2011':'1/11/2011'])


idx = pd.date_range("2023-01-01", periods=120, freq="D")
s = pd.Series(np.random.randn(len(idx)), index=idx, name="reactor_temp")

s = s.sort_index()

# print(s.resample("1ME").mean())
# print(s.resample("2W").sum())
# print(s.resample("10D").first())

# print(s.resample("6h10min").first())
# print(s.resample("6h10min3s").ffill())
# print(s.resample("6h").first().interpolate())

print(s.rolling(window=10).mean())
print(s.rolling(window=10).std())
print(s.rolling(window=10).mean().plot())


### Polars Version

import polars as pl
import numpy as np
from datetime import datetime

displacement = np.random.randn(195) 

df = pl.DataFrame(
    {
        "date": pl.datetime_range(datetime(2023, 3, 9, 8, 22), datetime(2023, 3, 9, 16, 0), interval="2m21s", eager=True),
        "displacement": displacement
    }
)
# print(df.head())

# raw = [
#     "2020",
#     "September 16th, 2020",
#     "2020 Sep 16 11:11",
#     "2020/09/16",
#     "09/16/2020",
# ]

# df = pl.DataFrame({"raw": raw})

# s1 = (
#     df.with_columns(
#         pl.col("raw")
#         .str.replace_all(r"(\d{1,2})(st|nd|rd|th)", "${1}")
#         .alias("raw_clean")
#     )
#     .select(
#         pl.coalesce(
#             [
#                 pl.col("raw_clean").str.strptime(pl.Datetime, "%Y", strict=False),
#                 pl.col("raw_clean").str.strptime(pl.Datetime, "%B %d, %Y", strict=False),
#                 pl.col("raw_clean").str.strptime(pl.Datetime, "%Y %b %d %H:%M", strict=False),
#                 pl.col("raw_clean").str.strptime(pl.Datetime, "%Y/%m/%d", strict=False),
#                 pl.col("raw_clean").str.strptime(pl.Datetime, "%m/%d/%Y", strict=False),
#             ]
#         ).alias("parsed")
#     )
#     .to_series()
# )

# print(s1)

# print(df.select(pl.col("date").dt.year().alias("year")))
# print(df.select(pl.col("date").dt.month().alias("month")))
# print(df.select(pl.col("date").dt.hour().alias("hour")))
# print(df.select(pl.col("date").dt.weekday().alias("weekday")))
# print(df.select(pl.col("date").dt.minute().alias("minute")))
# print(df.select(pl.col("date").dt.strftime("%B").alias("month_name")))
# print(df.select(pl.col("date").dt.strftime("%A").alias("day_name")))


# print(df.filter(pl.col("date") == datetime(2023, 3, 9, 9, 0)))
# print(df.filter(pl.col("date").is_between(datetime(2023, 3, 9, 9, 0), datetime(2023, 3, 9, 12, 0))))
# print(df.filter(pl.col("date") >= datetime(2023, 3, 9, 12, 0)))
# print(df.filter(pl.col("date").is_between(datetime(2023, 3, 9, 10, 0), datetime(2023, 3, 9, 14, 0))))


# df = df.sort("date")

# print(
#     df.group_by_dynamic("date", every="1mo")
#       .agg(pl.col("displacement").mean().alias("mean_displacement"))
# )

# print(
#     df.group_by_dynamic("date", every="2w")
#       .agg(pl.col("displacement").sum().alias("sum_displacement"))
# )

# print(
#     df.group_by_dynamic("date", every="10d")
#       .agg(pl.col("displacement").first().alias("first_displacement"))
# )

# print(df.sort("date").upsample(time_column="date", every="6h10m"))
# print(df.sort("date").upsample(time_column="date", every="6h10m3s").with_columns(pl.col("reactor_temp").fill_null(strategy="forward")))
# print(df.sort("date").upsample(time_column="date", every="6h").with_columns(pl.col("reactor_temp").interpolate()))

ts = df.with_columns(
        pl.col("reactor_temp").rolling_mean(window_size=10).alias("roll_mean_10"),
        pl.col("reactor_temp").rolling_std(window_size=10).alias("roll_std_10"),
    )


plt.plot(ts["date"], ts["roll_mean_10"])
plt.show()