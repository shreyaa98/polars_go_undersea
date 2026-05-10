
Preparations
============

.. figure:: pandas_polars.png

.. card::
    :shadow: lg

    **Upgrade to Polars**

    Aarla Frij opened the hatch to her submarine, swiftly slided down the ladder to the cockpit and cuddled comfortably into the captains seat. 
    A new expedition into the depths of the seven oceans awaited her. A new adventure. What secrets were waiting out there?
    A soft hum from the energy supply was the only sound in the cockpit. The ship was still asleep.
    
    *"I still have time for a nap before the mission,"* Aarla thought.
    
    Suddenly another bear came whistling into the cockpit, balancing tea cups on a tablet.
    That was Ming Ming, the intern from the remote world of Pandalor. Aarla sighed.. no nap.

    *"Hello captain! I've been down here for a while already. The ship is all right, but I think the computer needs a software update?
    Can you show me how to do this? Pleeease."*

    Aarla turned to the right and started searching through a pile of notes.

    *"Hm, somewhere here should be the ships instructions,"* Aarla muttered as she continued her search. 
    
    Finally, she pulled out a worn handbook. 
    
    *"OK, let's turn this thing on!"*.


----

Install Python
--------------

**Before you can start your journey, you need to install a few programs on your ships' computer.**

First, you need to install a Python distribution that allows you to run the **Jupyter Notebook** format.
**Anaconda** is a one-stop installation that contains all necessary Python packages and an editing environment.

Go to `www.anaconda.com  <https://www.anaconda.com/>`__ and download Anaconda for your system (the free version) and follow the installation instructions.

.. dropdown:: Can I use the standard Python installation?
   :animate: fade-in

   Yes. The version from `www.python.org <https://www.python.org>` works fine. While Anaconda is easier to get started with, many professional developers prefer the slimmer standard Python installation.

.. dropdown:: Can I use VSCode instead?
   :animate: fade-in

   Yes. VSCode has a great plugin that handles the interactive Python environment.
   It is very similar to Jupyter. 
   However, I am not using it so please don't ask me for configuration details.


.. dropdown:: Can I use Google Colab?
   :animate: fade-in

   Yes. `Google Colab <https://colab.research.google.com/>`__ is free and completely cloud-based.
   When using Colab, most of the Python libraries you will need are already installed.
   However, uploading files will be a bit more tedious.
   Please look up how to do that.

.. dropdown:: Can I install packages on my own?
   :animate: fade-in

   Yes. This is a good idea if you already have a Python distribution installed on your system.
   You need to install a few core libraries.
   Use the `pip` program from a terminal to install the latest version of everything:

   .. code::

      pip install --upgrade polars numpy seaborn matplotlib
          

----

Start Jupyter
-------------

- from the **Anaconda Navigator**, start the Jupyter Notebook.
- Jupyter will run as a HTTP server in the background
- From the overview page, create a new Python3 notebook with the button **New** (top-right)

Write an import section
-----------------------

Check if the core Python libraries for data analytics are installed.
Write into an empty code cell:

.. code:: python3

    import polars as pl
    import numpy as np
    import seaborn as sns
    from matplotlib import pyplot as plt

Execute the command with the triangular *"play"* button in the toolbar or press **Shift-Enter**.
You should see an empty output and a new input cell.
If you don't see an error message, everything has worked.

----

Keyboard shortcuts
------------------

Hitting those small keys with your big paws is not easy.
It takes years of practice. To make your life easier, there are a couple of useful shortcuts: 

================ ==========================
key              description  
================ ==========================
`Shift + Enter`  execute a cell
`Escape + A`     insert a cell above
`Escape + B`     insert a cell below
`Escape + X`     delete the current cell
`Tab`            autocomplete names
`Shift + Tab`    context-sensitive help
================ ==========================

----

Edit Markdown
-------------

Edit and format a Markdown cell in Jupyter

.. code::

    ### Captains log, stardate <ENTER_TODAYS_DATE>
    
    **Captain <YOUR NAME>** has taken command of the ship *<NAME YOUR SHIP>*.

Change the type of the cell to Markdown using the icons or press `Escape + M`.

Execute the code with the **play** button on top or press `Shift + Enter`.
You should see the paragraph formatted as HTML.

----

Execute Python Code
-------------------

Write a simple Python command. Insert a new cell.
Then, run the command to switch on all systems:

.. code:: python

    print("power up submarine")

Execute the code with the **play** button on top or press `Shift + Enter`.
Your computer should respond with:

.. code::

    power up submarine

----

.. card::
   :shadow: lg

   It seems your ships computer is fully online.
   Time to do some more serious stuff.
