
Time Series
===========

.. figure:: reactor.jpeg

Gravity Rift
------------

.. card::
   :shadow: lg

   **Alert!** The anti-matter reactor of the ship has become unstable.
   High-energy particles drift in random directions.
   You manage to avoid turning your ship into a fireball by throwing the anti-matter out through a hatch just in time.
   As it is the matter with anti-matter, it messes with the time-space continuum.

   In this case, it creates a gravity rift that sucks you in.
   Your ship pops out in a completely different space and time, next to a habitable planet.
   Judging by the air pollution, you ended up in the early 21st century.

   Fortunately, you should be able to make it back from this barbaric place.
   All you need to do is to find out when the gravity displacement is the biggest.
   Then, you should be able to open another rift and jump back to your own world.

   You find the gravity displacement data over time in :download:`gravity.csv`.
   
   Use the local time system to calibrate the time.


.. dropdown:: The pollution phrase looks familiar. Who is it from?
   :animate: fade-in

   This is a reference to the legendary Leonard Nimoy in `Star Trek IV: The Voyage Home <https://en.wikipedia.org/wiki/Star_Trek_IV:_The_Voyage_Home>`__

Create a Time Series
--------------------

Handling timestamps is one of the strongest features in ``Polars``.
In Polars, timestamps are typically stored in a normal column instead of a row index.
With :py:func:`polars.date_range` you can create series of timestamps from scratch:

.. code:: python3

    import polars as pl
    import numpy as np
    from datetime import date

    displacement = np.random.randn(200)

    df = pl.DataFrame(
        {
            "date": pl.date_range(date(2023, 3, 9), date(2023, 9, 24), interval="1d", eager=True),
            "reactor_temp": displacement,
        }
    )
    df.head()

Instead of a single-column setup, you can use a DataFrame with multiple value columns.
In Polars, time is usually tracked with a dedicated datetime column.

You could also create timestamps by specifying both boundaries and an interval:

.. code:: python3

    from datetime import datetime

    displacement = np.random.randn(195) 
    df = pl.DataFrame(
        {
            "date": pl.datetime_range(datetime(2023, 3, 9, 8, 22), datetime(2023, 3, 9, 16, 0), interval="2m21s", eager=True),
            "displacement": displacement
        }
    )
    df.head()

----

Timestamps from Strings
-----------------------

Parsing strings to timestamps is very convenient.
``Polars`` can parse many different formats.
This makes your life much easier, e.g. when parsing the log files of an anti-matter reactor.

.. code:: python3

    raw = [
        "2020",
        "September 16th, 2020",
        "2020 Sep 16 11:11",
        "2020/09/16",
        "09/16/2020",
        ]
        
    df = pl.DataFrame({"raw": raw})

    strings = (
        df.with_columns(
            pl.col("raw")
            .str.replace_all(r"(\d{1,2})(st|nd|rd|th)", "${1}")
            .alias("raw_clean")
        )
        .select(
            pl.coalesce(
                [
                    pl.col("raw_clean").str.strptime(pl.Datetime, "%Y", strict=False),
                    pl.col("raw_clean").str.strptime(pl.Datetime, "%B %d, %Y", strict=False),
                    pl.col("raw_clean").str.strptime(pl.Datetime, "%Y %b %d %H:%M", strict=False),
                    pl.col("raw_clean").str.strptime(pl.Datetime, "%Y/%m/%d", strict=False),
                    pl.col("raw_clean").str.strptime(pl.Datetime, "%m/%d/%Y", strict=False),
                ]
            ).alias("parsed")
        )
        .to_series()
    )


Technically, the timestamps are stored in integers and measured in nanoseconds since the **Unix epoch on Jan 1st, 1970** when the first Unix machine officially started to tick.

.. note::

    When reading timestamp columns from a CSV file in Polars, use ``try_parse_dates=True`` in ``pl.read_csv`` for automatic parsing, or parse explicitly with ``pl.col("col_name").str.strptime(...)``.

----

Plotting Time Series
--------------------

Polars does not provide a built-in plotting API, so a common approach is to plot with ``matplotlib`` using explicit x/y columns:

.. code:: python3

    from matplotlib import pyplot as plt

    plt.plot(df["x"], df["y"])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

.. image:: random.png

A frequently used trick is to sum up values with a **cumulative sum**.
The **random data** becomes a **random walk**.
You see that the small changes add up over time and the data is drifting.
Note that the resulting data still uses the same timestamp column:

.. code:: python3

    ts = df.with_columns(pl.col("y").cum_sum().alias("y_cumsum"))

    plt.plot(ts["x"], ts["y_cumsum"])
    plt.xlabel("x")
    plt.ylabel("y_cumsum")
    plt.show()

``matplotlib`` decides on the fly which scale and which ticks to use for the x-axis.
This works well almost all the time:

.. image:: walk.png

----

Accessing DateTime Attributes
-----------------------------

Every datetime column has a couple of useful fields that can be accessed:

.. code:: python3

    df.select(pl.col("date").dt.year())
    df.select(pl.col("date").dt.month())
    df.select(pl.col("date").dt.hour())
    df.select(pl.col("date").dt.weekday())
    df.select(pl.col("date").dt.day())
    df.select(pl.col("date").dt.minute())
    df.select(pl.col("date").dt.strftime("%B"))
    df.select(pl.col("date").dt.strftime("%A"))

----

Indexing and Slicing
--------------------

Datetime columns can be filtered and sliced comfortably using comparison expressions:

.. code:: python3

    df.filter(pl.col("date") == datetime(2023, 3, 9, 9, 0))
    df.filter(pl.col("date").is_between(datetime(2023, 3, 9, 9, 0), datetime(2023, 3, 9, 12, 0)))
    df.filter(pl.col("date") >= datetime(2023, 3, 9, 12, 0))
    df.filter(pl.col("date").is_between(datetime(2023, 3, 9, 10, 0), datetime(2023, 3, 9, 14, 0)))

----

Resampling
----------

A frequent task is changing rows so that different intervals between the time stamps are used.
There are two types of resampling.

**Downsampling** condenses the data (fewer rows).
Like with ``df.group_by()``, you need to specify how the rows should be aggregated:

.. code:: python3

    df.group_by_dynamic("date", every="1mo").agg(pl.col("reactor_temp").mean())
    df.group_by_dynamic("date", every="2w").agg(pl.col("reactor_temp").sum())
    df.group_by_dynamic("date", every="10d").agg(pl.col("reactor_temp").first())

**Upsampling** changes the time column to a wider timescale (more rows).
The resulting gaps need to be filled or interpolated, otherwise they stay empty:

.. code:: python3

    df.sort("date").upsample(time_column="date", every="6h10m")
    df.sort("date").upsample(time_column="date", every="6h10m3s").with_columns(pl.col("reactor_temp").fill_null(strategy="forward"))
    df.sort("date").upsample(time_column="date", every="6h").with_columns(pl.col("reactor_temp").interpolate())
    


.. seealso::

    Check out the dynamic grouping and interval strings in the `Polars time-series documentation <https://docs.pola.rs/user-guide/transformations/time-series/>`__

----

Rolling Mean
------------

A frequent type of aggregation is the **rolling mean** (or moving average).
It shifts a window of N data points over the time series and returns a value for each position.
This smoothes out noise in the data.

.. code:: python3

    ts = df.with_columns(
        pl.col("reactor_temp").rolling_mean(window_size=10).alias("roll_mean_10"),
        pl.col("reactor_temp").rolling_std(window_size=10).alias("roll_std_10"),
    )

    from matplotlib import pyplot as plt
    plt.plot(ts["date"], ts["roll_mean_10"])
    plt.show()

Try different window sizes and see how the curve becomes smoother and smoother.
Polars rolling expressions also support standard deviations and additional rolling aggregations.

.. seealso::

   You can find more examples in the `Polars expressions documentation <https://docs.pola.rs/api/python/stable/reference/expressions/index.html>`__

----


Challenge
---------

.. card::
   :shadow: lg

   To find out when you need to jump back, solve the following tasks:

   1. create timestamps for an entire year (2025), one per day

    2. create a ``pl.DataFrame`` with ``date`` and ``gravity`` columns

   3. display the weekday for each timestamp. On Sunday, your chef will be cooking bamboo with mushrooms, so no time travel on that day.

   4. select the data after January. Time traveling before January is strictly forbidden.

   5. calculate the sum of all gravity displacements for each of the remaining 11 months

   6. calculate a rolling average with a 7-day window.

   7. plot the rolling average data. The day with the highest average is where you should time-travel.


.. dropdown:: How to create time-rift data?
   :animate: fade-in

   Here is the code. Use it at your own risk!

   .. code:: python3

      import numpy as np
      import polars as pl
      from matplotlib import pyplot as plt

      noise = np.random.normal(size=365)

      x = np.linspace(0, 40, 365)
      y = np.sin(x)
      yy = y + noise
    df = pl.DataFrame({"gravity": yy})
    df.write_csv("gravity.csv")
