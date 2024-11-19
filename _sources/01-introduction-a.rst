..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: 01-introduction-a
..  description:: Introduction to Pandas and data representations.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

.. _01_intro_a: 

Introduction to Pandas
###########################################

Pandas is a library in Python that provides data structures and data analysis tools. It is built on top of the NumPy package, which means that a lot of the NumPy functions are also available in Pandas. Pandas is particularly useful for data manipulation and analysis. We start by importing pandas package as **'pd'**. We will use **pd** as a prefix for all the pandas functions.

.. code-block:: python

    import pandas as pd


Pandas provides two types of classes for handling data:

- `Series <https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series>`_: a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc.

- `DataFrame <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame>`_: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.

In this textbook, we will focus on the DataFrame class, where we will load our dataset into a DataFrame where each row is an observation and each column is a feature.

Creating a DataFrame by passing a dictionary of objects where the keys are the column labels and the values are the column values:

.. code-block:: python

    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": pd.Timestamp("20130102"),
            "C": 'foo',
        }
    )

To see the contents of the DataFrame, you can use the print() function:

.. code-block:: python

    print(df)

.. code-block:: text

    A          B    C
    0  1 2013-01-02  foo
    1  2 2013-01-02  foo
    2  3 2013-01-02  foo
    3  4 2013-01-02  foo
    4  5 2013-01-02  foo



Run and try it!

.. activecode:: ex1_dataframe
    :language: python3

    import pandas as pd

    data = {'Name': ['Tom', 'Nick', 'John'],
            'Age': [20, 21, 19]}
    df = pd.DataFrame(data)
    print(df)