
Edit Columns
============

.. figure:: polars_control_room.png

.. card::
   :shadow: lg

   **Down to the Bottom**

   *"Listen up!" – Helmsman Lumi gained the attention of the entire crew.*
   
   *The penguins told us there might be the remains of an ancient civilization in these waters.
   We need to check the sea bed, and go all the way down. But we have to go down safely.
   If we go too fast, the change in pressure will crush you landlubbers like jellyfish.*
   
   *Andromé will take us through the math:"*

   * Currently, your submarine is cruising **1000 m above the bottom**.
   * Once we start our descent, gravitation will accelerate us by :math:`1 \frac{m}{s^2}`.
   * At any moment, we can **blow the floaters**. They will push us up with an acceleration of :math:`1-10 \frac{m}{s^2}`.
   * We can change the strength of the floaters or deactivate them at any point.
   * To touch down safely, we need to reach an altitude **and** speed of exactly zero.
  
   **This is not an arcade game, folks. Let's simulate the landing to find a good timing first.**

----

Create a DataFrame with a single column
---------------------------------------

Simulate the submarines depth over time with a resolution of one second.
Start by creating the time as a column. 1000 seconds should be enough:

.. code:: python

   import polars as pl

   seconds = pl.select(pl.arange(1000))
   df = pl.DataFrame({'seconds': seconds})

The dictionary format in the parentheses allows you to define a DataFrame with multiple columns as well.

.. dropdown:: Could I use other sequences instead?
   :animate: fade-in

   Yes. Polars supports multiple formats, e.g.:
   
   - numpy arrays created with ``np.arange(1000)`` or ``np.linspace(0, 1000, 1000)``
   - Python lists, e.g. ``list(range(1000))``

----

Add columns
-----------

Because the gravity does not change, we create a new column and fill it up with one value:

.. code:: python

   df = df.with_columns(pl.lit(1.0).alias('gravity'))

For the float, we create a new column, settting all values to zero:

.. code:: python

   df = df.with_columns(pl.lit(0.0).alias('floaters'))

An alternative is to use Polars functions like ``pl.zeros()`` or ``pl.lit()``. 
This works as long as the size matches the shape of the DataFrame:

.. code:: python

   df = df.with_columns(pl.lit(0.0).alias('floaters'))

If you re-assign to an existing column, the old column gets replaced.

----

Modify a column
---------------

Now we need to switch on the floaters.
Use conditional expressions to blow the floaters for a given time period:

.. code:: python

   df = df.with_columns(
       pl.when((pl.arange(0, pl.len()) >= 500) & (pl.arange(0, pl.len()) <= 600))
       .then(10)
       .otherwise(pl.col('floaters'))
       .alias('floaters')
   )

This will activate the floaters from second 500 to 600 with a strength of 10.

----

Column arithmetics
------------------

We can create new columns using math equations:

.. code:: python

   df = df.with_columns(
       (pl.col('gravity') - pl.col('floaters')).alias('acceleration')
   )

To calculate the speed, we need to add all acceleration values up to a given row:

.. code:: python

   df = df.with_columns(
       pl.col('acceleration').cum_sum().alias('speed')
   )

Inspect the data with ``df.head()`` to see the effect of the ``.cum_sum()`` method.

Adding up the speed column lets you calculate the altitude:

.. code:: python

   df = df.with_columns(
       (1000 - (pl.col('speed').cum_sum() / 100)).alias('altitude')
   )


.. dropdown:: Shouldn't we use differential calculus to solve this problem?
   :animate: fade-in

   The polar submarine is equipped with a vibrational controller that absorbs some of the water current. 
   The vibrations create chaotic movements that the helmsman needs to adjust in real time.
   Yes, differential calculus would help with the simulation.
   But in practice, the polars prefer the vibrations, since they are directly connected to their massage chairs.

----

Remove a column
---------------

The `seconds` column was useful in the beginning, so that the DataFrame was not empty.
But we do not really need it for the calculation.
To remove it, use:

.. code:: python

   df = df.drop('seconds')

The `drop()` method removes columns by default.

----

Zooming in
----------

To highlight the area with the lowest altitude, you can use the following code:

.. code:: python

   lowest_idx = df.with_row_number().filter(
       pl.col('altitude') == pl.col('altitude').min()
   )['row_number'][0]
   df.slice(0, lowest_idx + 5).tail(10)


----

Visualize the descent
---------------------

Let's plot the outcome of the simulation.
A simple line plot is sufficient.
We add a horizontal line to indicate the sea bottom.

.. code:: python

   from matplotlib import pyplot as plt

   df.to_pandas()['altitude'].plot()
   plt.hlines(xmin=0, xmax=1500, y=0.0, color="blue")


To debug the descent, it may help to see the speed as well.
We can show both columns in a line plot, but need to switch to a log-scale 
(both for comparability and precision).

.. code:: python

   ax = df.select(['altitude', 'speed']).to_pandas().plot()
   ax.set_yscale('log')

When you see that your altitude goes through the floor of the log plot, it means that the submarine would crash into the sea bottom.


----

Challenge
---------

.. card::
   :shadow: lg

   Once you reach an altitude of exactly **0 m** and a speed of exactly **0 m/s**,
   the submarine will gently touch down.

   Add as many floater activations as you need using the pattern:

   .. code:: python

      df = df.with_columns(
          pl.when((pl.arange(0, pl.len()) >= start_time) & (pl.arange(0, pl.len()) <= end_time))
          .then(strength)
          .otherwise(pl.col('floaters'))
          .alias('floaters')
      )

   The following code checks whether the landing was successful:

   .. code:: python

      lowest = df.filter(pl.col('altitude') == pl.col('altitude').min()).row(0, named=True)
      if lowest['altitude'] == 0 and lowest['speed'] == 0:
          print("sea bottom reached!")
