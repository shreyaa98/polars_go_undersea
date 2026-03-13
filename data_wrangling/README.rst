Data Wrangling
==============

Cargo Bay
---------

.. figure:: containers.jpeg

.. card::
   :shadow: lg

   One day you decide to inspect the cargo bay of your spaceship.

   What a mess!

   Many of the containers are badly labeled.
   The radioactive waste is next to the ice cream.
   Some containers are not labeled at all.

   Time for a proper cleanup of the cargo docs in :download:`cargo.csv`. 

----

Sort rows
---------

Sort a DataFrame by:

.. code:: python

   df.sort("category")

to sort by more than one column, try:

.. code:: python

   df = df.sort(["category", "type"], descending=[False, True])


Change the data type
--------------------

Convert values to strings:

.. code:: python

   df = df.with_columns(pl.col("crate_no").cast(pl.Utf8).alias("crate_str"))

You can easily combine multiple columns using standard operators:

.. code:: python

   df = df.with_columns((pl.col("crate_no").cast(pl.Utf8) + pl.col("crate_shelf")).alias("crate_id"))

Create new rows
---------------

If you have Python sequence types (lists, tuples, sets), you can assign them to new columns directly.
The only prerequisite is that the length matches that of your DataFrame:

.. code:: python

   deck = [d for _,d in zip(range(df.shape[0]), cycle("123"))]  # repeat 1,2,3,1,..
   df = df.with_columns(pl.lit(deck).alias("deck")) 

Set the index column
--------------------

In Polars, DataFrames do not have an index column like pandas. Instead, you can filter rows based on column values.

.. code:: python

   # to select rows where crate_id is '13A'
   crates = df.filter(pl.col("crate_id") == "13A")

Polars operations return new DataFrames, so no inplace parameter.

Missing values
--------------

Missing values are a common phenomenon. A quick way to diagnose missing
values is:

.. code:: python

   df.null_count().to_pandas().plot.bar()

Often, you might simply want to kick out all rows in which a None or NaN
occurs:

.. code:: python

   df_dropped = df.drop_nulls()

Alternatively, you might want to fill in a best guess value:

.. code:: python

   df_fixed = df.fill_null(42)
   # or
   df_fixed = df.fill_null(strategy="median")

There are many, many strategies to fix missing values (imputation
methods).

Swap rows and columns
---------------------

Some operations (especially plotting) are easier to implement if you
turn a DataFrame by 90°:

.. code:: python

   df.transpose()

Iterate
-------

Usually, it is possible to write one-liners or concise expressions that
get the job done. If this is not possible (or you are still learning
this stuff and can’t figure out a better way yet), you may want to fall
back to a ``for`` loop over all the rows.

.. code:: python

   for i, row in enumerate(df.iter_rows(named=True)):
       print(i, row['type'])


.. figure:: bamboo.jpg

Challenge
---------

.. card::
   :shadow: lg

   Take care of the following clean-ups in the cargo docs :download:`cargo.csv`:

   - for the radioactive waste, replace the words in the `units` column by numbers
   - convert the `units` column to the type `int`
   - fill the missing values in the `category` column for the bamboo ice cream
   - fill the missing values in the `units` column
   - sort the crates by type and by identifier in ascending order
  