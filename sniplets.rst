Read from Clipboard
-------------------

This is sometimes useful when improvising.
In Polars, there is no direct read_clipboard() function like in pandas. 
But you can easily achieve the same thing by reading the clipboard text and passing it to Polars.

.. code:: python

   df = pl.from_pandas(pd.read_clipboard())



add an index column
-------------------

   df = df.with_row_count("index")


from prep
.. figure:: polars_control_room.png
.. figure:: new_world.png

