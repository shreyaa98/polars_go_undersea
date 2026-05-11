Select Rows and Columns
=======================

.. figure:: crew.png

.. card::
   :shadow: lg

   **Find your Crew**

   "Time to leave", Captain Aarla thought. "Wait, the ship is completely empty. 
   Wheere is everybody? Grm! of course they are hanging out at the bar."
   Aarla slammed the bar door open. The bar was full of people. Aarla yelled: "WHERE IS MY CREW?". 
   The room fell silent immediately. A few bears ducked behind a corner or jumped below a table. 
   But for sure her crew was here. She went around looking.

   To recognize your crew members again, you’ll need to load the crew roster :download:`crew.csv` using Polars and inspect the data.

----

Show column names
-----------------

You may want to access column names as a Python list.
This is also useful to check what types the names are.

.. code:: python

   df.columns

----

Select a column
---------------

A single column is returned as a `pl.Series`:

.. code:: python

   df['id']

----

Select multiple columns
-----------------------

Multiple columns require double square brackets.
The inner one is a list of column names:

.. code:: python

   df[['black_spots', 'blue_spots']]

----

Select rows by position
-----------------------

The ``slice()`` method selects rows by position.
The first argument specifies the starting row, and the second argument specifies the number of rows to return.

.. code:: python

   df.slice(5, 10)

----

Select columns by position
--------------------------

The column slice ``df.columns[1:4]`` selects columns 2–4, which are then returned using ``select()``.

.. code:: python

   df.select(df.columns[1:4])

----

Select rows and columns by position
-----------------------------------

Combine both row and column selection:

.. code:: python

   df.slice(5, 10).select(df.columns[1:4])

A pythonic index notation is also available. The first pair in the square brackets selects rows 2-5, the second pair selects columns 3 to 4.
Note that indices in Python always start at zero, and the last position is never included.

.. code:: python

   df[5:15, 1:4]

.. note::

   In this tutorial, we are giving preference to the *functional notation* using
   functions like ``slice`` because it integrates more easily with other tools.

----

Select rows by column value
---------------------------

To select rows based on column values, use the ``filter()`` method.
This is useful for selecting rows where a column matches a specific value, e.g.

.. code:: python

   df.filter(pl.col('ears') == 'pink')

----

Filter by value
---------------

This is very powerful selection logic that is applied to all rows simultaneously.

The notation with double square brackets looks a bit weird first.
It is easier to understand if you know the inner expression results in a boolean mask that is used to filter the rows of the `DataFrame`.

.. code:: python

   df.filter(pl.col('ears') == 'pink'))

   df.filter(pl.col('black_spots') < 3)

   df.filter(pl.col('black_spots').is_between(3, 7))

   df.filter((pl.col('black_spots') < 3) & (pl.col('blue_spots') > 7))

Note that you have to use the **binary operators** `&`, `|` to combine multiple conditions.
The **logical operators** `and`, `or` will not work.

----

Select random rows
------------------

.. code:: python

   df.sample(7)

----

Selecting and filtering examples
--------------------------------

===================================================== ========================================================
command                                               description
===================================================== ========================================================
df.row(0)                                             select the first row as a tuple of values
df.slice(10)                                          select all rows, skipping the first 10
df.slice(5, 10)                                       select 10 rows starting from row 6
df.select(pl.exclude('id'))                           select all columns except 'id'
df.select(pl.all())                                   select all columns explicitly
df.select(pl.col(pl.Int64))                           select columns by data type
df.filter(pl.col('ears') == 'pink')                   find rows where 'ears' is exactly 'pink'
df.filter(~pl.col('ears').is_in(['pink', 'black']))   find rows where 'ears' is neither 'pink' nor 'black'
===================================================== ========================================================

Challenge
---------

.. card::
   :shadow: lg

   Select rows from the crew roster :download:`crew.csv` to find your five officers.
   You have a couple of hints:
   
   * all of your officers have **at least 12 blue spots**
   * three of your officers have **exactly 9 black spots**
   * none of your officers has **pink ears** or **black ears**
   * **Lumi** (helmsman) easily recognizable by her red headscarf, has the **id 247**
   * **Ilmar** (ships carpenter) with at least 100 tattoos. **Has more than 18 blue spots and also have ears dyed in indigo**
   * **Andromé** (navigator) with a green headscarf. Has more blue spots than the Boreaboy.
   * **Boreaboy** (cook) with something between seven and ten earrings. Has an **unknown ear color**.
   * and of course **Ming Ming** (intern ) from the remote planet of Pandalor, with no tattoos, earrings or scarf
   **Has their ears dyed in chartreuse. They have fewer blue spots than the Andromé.**

   **Identify all five of them.**

.. dropdown:: How many blue spots do your officers have in total?
   :animate: fade-in

   There should be exactly 79.

----

.. dropdown:: How was the crew data generated?
   :animate: fade-in

   Below you find the code to generate the data in :download:`crew.csv`:

   The generator uses ``np.random.seed(42)``, so it is deterministic and reproduces the same file content.

   .. literalinclude:: crew_generator.py
