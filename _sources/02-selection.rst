..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: 02-selection
..  description:: Selecting data from DataFrames.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

.. _02_selection:

Selecting data from DataFrames
###########################################

For a DataFrame, passing a single label selects a columns and yields a Series equivalent to df.A:

.. code-block:: python

    print(df["A"])

These Series objects can be used with Boolean operators:

.. code-block:: python

    print(df["A"] > 5)

You can pass in a condition to select rows that satisfy the condition:

.. code-block:: python

    print(df[df["A"] > 5])

You can also combine multiple conditions with Boolean operators, such as & (and) and | (or):

.. code-block:: python

    print(df[(df["A"] < 2) | (df["A"] > 5)])



Try it out!

.. activecode:: ex2-1
    :language: python3
    :hidecode:

    import pandas as pd

    # Read the CSV file
    df = pd.DataFrame({
        'name': ['John', 'Jane', 'Sue', 'Fred'],
        'age': [23, 78, 22, 19]
    })


.. activecode:: ex2-2
    :language: python3
    :include: ex2-1

    # Print the names of people between 18-65 years old.
    print(df[df['name'] ...])
