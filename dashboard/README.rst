
Dashboard
=========


.. card::
   :shadow: lg

   **Coming Home**

   After the polars safely return to their harbor, they report to their elders, as tradition requires.
   Aarla and her crew visit the long house of **Ursa Maior**, the polar matriarch.
   Handing out a round of cold ales, she addresses the expedition:

   *"Now, captain Aarla, what did you find out there? Make it a good story that the Skaldi will sing of for a long time.
   And we want some plots and pictures, too! We are scientists after all, not some drunk barbarians, HAR HAR HAR!"*

   Aarla takes a deep breath, and starts to tell:

   *"We were sailing the stormy seas, with our hearts full of bravery, until one day we discovered this: ..."*

   **Create a visual report about the penguins.**

Install streamlit
-----------------

First, install the `streamlit` library:

.. code::

    pip install streamlit

Start the server
----------------

Create a new file ``dashboard.py``:

.. code:: python

   import streamlit as st
   
   st.write("here is our report ...")

Then, open a terminal in the folder with the code and run:

.. code::

   streamlit run dashboard.py

Open your browser at `http://127.0.0.1:8501 <http://127.0.0.1:8501>`__ . You should see the text from the program.

Format text with Markdown
-------------------------

The ``st.write()`` understands **Markdown**. Use it to add headings, enumerations and similar:

.. code::

   st.write("# Penguins and their Beaks")


Display the data
----------------

Load the penguin data and print the DataFrame:

.. code:: python

   import seaborn as sns

   df = sns.load_dataset("penguins")
   st.write(df)

You should see a nicely formatted table in the browser.

Streamlit plots
---------------

Streamlit has its own plotting functions for DataFrames. Here is a **bar chart**:

.. code:: python

   counts = df["species"].value_counts()
   st.bar_chart(counts)

Here are a **line chart** and a **scatter plot**. All plots take very similar format options:

.. code:: python

   st.line_chart(data=df, x="body_mass_g", y=["bill_length_mm", "flipper_length_mm"], 
               color=["#ff00ff", "#00ff00"],
               width=0, height=0,
               use_container_width=True)

   st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", 
               color="species",
               width=0, height=500,
               use_container_width=True)


Matplotlib and Seaborn plots
----------------------------

Matplotlib and seaborn plots will be rendered as static images. Here is a histogram:

.. code:: python

   fig = plt.figure()
   sns.histplot(df["body_mass_g"], kde=True)
   st.pyplot(fig)

Tabs
----

As an example of many convenient HTML elements, here is how you would subdivide your dashboard into multiple tabs:

.. code:: python

   tab1, tab2, tab3 = st.tabs(["Part 1", "Part 2", "Part 3"])

    with tab1:
        st.write("## Part 1")
        ...

    with tab2:
        st.write("## Part 2")
        ...


Control elements
----------------

A very convenient feature is that you can make your dashboard interactive using one line functions:

Select one or multiple entries from a list of strings:

.. code:: python

   options = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]

   column: str = st.selectbox("pick a data column", options)

   species: list[str] = st.multiselect("species", options=["Adelie", "Chinstrap", "Gentoo"])


Select a number between two boundaries:

.. code:: python

   min_val: int = st.slider("minimum value", 0, 100)


Input some text:

.. code:: python

   text: str = st.text_input("enter some text: ", value=":sunglasses:")
  

Switch parts of your dashboard on and off:
   
.. code:: python

   show_plots: bool = st.toggle('Show some plots')


.. card::
   :shadow: lg

   **Create an interactive dashboard by using the results of these functions in plotting or data filtering commands.**


Caching
-------

A streamlit script is fully executed every time the page is updated.
With a larger dataset, you may want to cache the loading and/or data wrangling in a function:

.. code:: python

   @st.cache_data
   def load_data():
       return sns.load_dataset('penguins')
   
   df = load_data()


.. seealso::

   `Streamlit documentation and deployment <https://streamlit.io/>`__
