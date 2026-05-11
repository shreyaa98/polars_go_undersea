
Dashboard
=========


.. card::
   :shadow: lg

   **Coming Home**

   After the polars safely return to their harbor, they report to their elders, as tradition requires.
   Aarla and her crew visit the long house of **Ursa Maior**, the polar matriarch.
   Handing out a round of cold ales, she addresses the expedition:

   *"Now, captain Aarla, what did you find? Make it a good story that the Skaldi will sing of for a long time.
   And we want some plots and pictures, too! We are scientists after all, not some drunk barbarians, HAR HAR HAR!"*

   **Create a visual report about the penguins.**

Install streamlit
-----------------

First, install the `streamlit` library:

.. code::

    pip install streamlit

Copy the code
-------------

Save the following code in a file `dashboard.py`:

.. literalinclude:: pingu_streamlit.py

Run the server
--------------

Run from a terminal with the code:

.. code::

   streamlit run dashboard.py

.. seealso::

   `Streamlit documentation and deployment <https://streamlit.io/>`__
