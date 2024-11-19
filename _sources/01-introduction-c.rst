..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: 01-introduction-c
..  description:: Loading data from files.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: ex1-
   

.. _01_intro_c: 

Loading DataFrames
###########################################

So far, we created DataFrames from scratch. However, in real-world scenarios, you will be working with data stored in files. Pandas provides functions to read data from different file formats such as CSV, Excel, JSON, and more.

In this tutorial, we will focus on CSV files.

To read a CSV file, you can use the **read_csv()** function. This function reads the content of the CSV file and returns a DataFrame.

.. raw:: html

    <div style='background-color: #f5f5f5; border-radius: 4px; border: 1px solid #ccc; padding:2px'>
        <p><strong>Syntax:</strong> <code>pd.read_csv(filepath_or_buffer, sep=’,’, header=’infer’, index_col=None, usecols=None, engine=None, skiprows=None, nrows=None)</code></p>
        <ul>
            <li><strong>Parameters:</strong></li>
            <ul>
                <li><code>filepath_or_buffer</code>: Location of the CSV file. Accepts a string path or URL of the file.</li>
                <li><code>sep</code>: Separator, default is <code>,</code>.</li>
                <li><code>header</code>: Accepts an int, a list of int, or row numbers to use as the column names and the start of the data. If <code>header=None</code>, columns will be displayed as 0, 1, and so on.</li>
                <li><code>usecols</code>: Retrieves only selected columns from the CSV file.</li>
                <li><code>nrows</code>: Number of rows to be displayed from the dataset.</li>
                <li><code>index_col</code>: If <code>None</code>, no index numbers are displayed with records.</li>
                <li><code>skiprows</code>: Skips the specified rows in the new DataFrame.</li>
            </ul>
        </ul>
    </div>

Try it!

.. datafile:: test.csv

   Colt McCoy QB CLE  135 222 1576    6   9   60.8%   74.5
   Josh Freeman QB TB 291 474 3451    25  6   61.4%   95.9
   Michael Vick QB PHI    233 372 3018    21  6   62.6%   100.2
   Matt Schaub QB HOU 365 574 4370    24  12  63.6%   92.0
   Philip Rivers QB SD    357 541 4710    30  13  66.0%   101.8
   Matt Hasselbeck QB SEA 266 444 3001    12  17  59.9%   73.2
   Jimmy Clausen QB CAR   157 299 1558    3   9   52.5%   58.4


.. activecode:: ex1c-1
    :language: python3
    :datafile: test.csv

    import pandas as pd

    # Read the CSV file
    df = pd.read_csv('test.csv')

    # Display the DataFrame
    print(df)
