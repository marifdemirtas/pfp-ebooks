..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: 03-operations
..  description:: Operations on DataFrames.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

.. _03_operations:

Operations on DataFrames
###########################################

You can call many functions on a DataFrame, such as sum(), mean(), max(), min(), etc. These functions will be applied to each column separately, unless you specify the axis parameter.

For example, to calculate the mean of each column:

.. raw:: html

    <div style='background-color: #f5f5f5; border-radius: 4px; border: 1px solid #ccc; padding:2px'>
        <p><strong>Syntax:</strong> <code>DataFrame.mean(axis=0, skipna=True, level=None, numeric_only=False, **kwargs)</code></p>
        <ul>
        <li><strong>Parameters:</strong></li>
        <ul>
        <li><code>axis</code>: {index (0), columns (1)}</li>
        <li><code>skipna</code>: Exclude NA/null values when computing the result</li>
        <li><code>level</code>: If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series</li>
        <li><code>numeric_only</code>: Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data. Not implemented for Series.</li>
        </ul>
        <li><strong>Returns:</strong></li>
        <ul>
            <li><code>mean</code>: Series or DataFrame (if level specified)</li>
        </ul>
        </ul>
    </div>


.. activecode:: ex2-1c
    :language: python3
    :hidecode:

    import pandas as pd

    # Read the CSV file
    df = pd.DataFrame({
        'name': ['John', 'Jane', 'Sue', 'Fred'],
        'age': [23, 78, 22, 19]
    })

.. activecode:: ex3-2
    :language: python3
    :include: ex2-1c

    print(df['age'].mean())

Some CSV files may have missing values, due to human error, or due to the way the data was collected. 
Pandas represents missing values as NaN (Not a Number). It is by default not included in computations. See the `Missing Data section <https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data>`_.


To check for missing values in a DataFrame, you can use the isnull() method, which returns a DataFrame of the same shape as the original, with True or False values indicating whether each cell is missing data.  

.. code-block:: python

    print(df.isnull())

You can use `fillna() <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna>`_ function to replace these values.

.. raw:: html

    <div style='background-color: #f5f5f5; border-radius: 4px; border: 1px solid #ccc; padding:2px'>
    <p><strong>Syntax:</strong> <code>DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)</code></p>
        <ul>
            <li><strong>Parameters:</strong></li>
            <ul>
                <li><code>value</code>: Static, dictionary, array, series, or dataframe to fill instead of NaN.</li>
                <li><code>method</code>: Method used if no value is passed. Options include <code>bfill</code>, <code>backfill</code>, or <code>ffill</code>, which fill values using the forward index or previous/backward values, respectively.</li>
                <li><code>axis</code>: Takes an integer (0 or 1) or a string (<code>index</code> or <code>columns</code>) to specify rows/columns.</li>
                <li><code>inplace</code>: A boolean indicating whether changes should be made directly to the dataframe if set to <code>True</code>.</li>
                <li><code>limit</code>: An integer specifying the maximum number of consecutive forward/backward NaN value fills.</li>
                <li><code>downcast</code>: A dictionary specifying dtype conversions (e.g., <code>Float64</code> to <code>int64</code>).</li>
                <li><code>**kwargs</code>: Additional keyword arguments.</li>
            </ul>
        </ul>
    </div>



Try it out!

.. activecode:: ex3-1
    :language: python3
    :hidecode:

    import pandas as pd

    # Read the CSV file
    df = pd.DataFrame({
        'name': ['John', 'Jane', 'Sue', 'Fred'],
        'age': [23, 78, 22, 19]
    })


.. activecode:: ex3-3
    :language: python3
    :include: ex3-1

    # Print the names of people between 18-65 years old.
    print(df[df['name'] ...])
