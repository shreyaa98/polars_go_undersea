
Edit columns
============

.. figure:: polars_control_room.png

.. card::
   :shadow: lg

   **Planetary Descent**

   Finally you decide to land on the planet of the mysterious penguins.
   Because your ship is not equipped with teleportation, your delegation will have to take a shuttle to the surface.
   Your job is to bring them down safely.

   * Currently, your ship (and the shuttle) is orbiting in an altitude of **1000 km**.
   * Once the shuttle leaves orbit, the planets gravity accelerates the shuttle constantly by :math:`10.00 \frac{m}{s^2}`.
   * At any moment, you can **activate the thrusters** with an acceleration of :math:`10.0-100.0\frac{m}{s^2}`.
   * You can change the strength of the thrusters or deactivate them 
   * Reach an altitude **and** speed of exactly 0 to safely land on the surface.
  
   Let's simulate the landing to find a good timing for activating the thrusters.

----

Create a DataFrame with a single column
---------------------------------------

Simulate the ships' altitude over time with a resolution of one second.
Start by creating the time as a column. 1000 seconds should be enough:

.. code:: python

   import polars as pl

   seconds = list(range(1000))
   df = pl.DataFrame({'seconds': seconds})

The dictionary format in the parentheses allows you to define a DataFrame with multiple columns as well.

.. dropdown:: Could I use a Polars sequence instead?
   :animate: fade-in

   Yes. Polars has native functions like ``pl.arange()`` or ``pl.int_range()`` that are faster and simpler.
   For simple integer sequences, ``list(range(...))`` is a straightforward Python approach.

----

Add columns
-----------

Because the gravity does not change, we create a new column and fill it up with one value:

.. code:: python

   df = df.with_columns(pl.lit(10.00).alias('gravity'))

For the thrust, we create a new column, settting all values to zero:

.. code:: python

   df = df.with_columns(pl.lit(0.0).alias('thrust'))

An alternative is to use Polars functions like ``pl.zeros()`` or ``pl.lit()``. 
This works as long as the size matches the shape of the DataFrame:

.. code:: python

   df = df.with_columns(pl.lit(0.0).alias('thrust'))

If you re-assign to an existing column, the old column gets replaced.

----

Modify a column
---------------

Now we need to switch on the thrusters.
Use conditional expressions to fire the thrusters for a given time period:

.. code:: python

   df = df.with_columns(
       pl.when((pl.arange(0, pl.len()) >= 500) & (pl.arange(0, pl.len()) <= 600))
       .then(100)
       .otherwise(pl.col('thrust'))
       .alias('thrust')
   )

This will activate the thrusters from second 500 to 600 with a strength of 100.

----

Column arithmetics
------------------

We can create new columns using math equations:

.. code:: python

   df = df.with_columns(
       (pl.col('gravity') - pl.col('thrust')).alias('acceleration')
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

   The pandas spaceship is equipped with quantum displacement technology that
   dynamically modifies the Planck constant. So technically, the ship is performing
   a series of very small jumps in space-time. 
   
   A side effect of this is that the acceleration gently strokes your fur while the ship is
   descending and you would not want to mess with that.

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
We add a horizontal line to indicate the surface.

.. code:: python

   from matplotlib import pyplot as plt

   df.to_pandas()['altitude'].plot()
   plt.hlines(xmin=0, xmax=1500, y=0.0, color="red")


To debug the descent, it may help to see the speed as well.
We can show both columns in a line plot, but need to switch to a log-scale 
(both for comparability and precision).

.. code:: python

   ax = df.select(['altitude', 'speed']).to_pandas().plot()
   ax.set_yscale('log')

When you see that your altitude goes through the floor of the log plot, it means that the spaceship would crash into the planet.


----

.. figure:: landing.jpeg

Challenge
---------

.. card::
   :shadow: lg

   Once you reach an altitude of exactly **0 m** and a speed of exactly **0 m/s**,
   your **anti-gravitational landing gear** will finish the landing automatically.

   Add as many thruster activations as you need using the pattern:

   .. code:: python

      df = df.with_columns(
          pl.when((pl.arange(0, pl.len()) >= start_time) & (pl.arange(0, pl.len()) <= end_time))
          .then(strength)
          .otherwise(pl.col('thrust'))
          .alias('thrust')
      )

   The following code checks whether the landing was successful:

   .. code:: python

      lowest = df.filter(pl.col('altitude') == pl.col('altitude').min()).row(0, named=True)
      if lowest['altitude'] == 0 and lowest['speed'] == 0:
          print("landing successful!")
