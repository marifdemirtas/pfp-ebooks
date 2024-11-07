..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan4
..  description:: Worked examples plus practice for Plan4.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: Plan4-

.. Plan4:

Plan4: Visualize Distribution
#####################################

Plan4: Example
====================================

This is a plan

.. plandisplay:: plans.json
    :plan: Visualize Distribution

Plan4: When to use this plan
====================================

This plan is used when...

Plan4: How to use this plan
====================================

.. changeable_areas:: Plan4_click


Plan 1: Exercises
====================================

.. clickablearea:: Visualize Distribution_click
    :question: Click on areas to change for...
    :iscode:
    :feedback: Check out the example of this plan above to identify the area that should be changed.

    :click-incorrect:import matplotlib.pyplot as plt:endclick:
    :click-incorrect:# Plotting histogram:endclick:
    :click-incorrect:df[:endclick: :click-correct:'column_name':endclick: :click-incorrect:].plot(kind='hist', bins=:endclick: :click-correct:bincount:endclick: :click-incorrect:, edgecolor='black'):endclick:
    :click-incorrect:# Display the plot:endclick:
    :click-incorrect:plt.xlabel('Values'):endclick:
    :click-incorrect:plt.ylabel('Frequency'):endclick:
    :click-incorrect:plt.title('Histogram of column_name'):endclick:
    :click-incorrect:plt.grid(True):endclick:
    :click-incorrect:plt.show():endclick:


.. fillintheblank:: 'Visualize Distribution_fill'
    Fill in the plan to...
    ``import matplotlib.pyplot as plt``

    ````
    ``# Plotting histogram``
    ``df[``|blank|

    ````
    ``# Display the plot``
    ``plt.xlabel('Values')``
    ``plt.ylabel('Frequency')``
    ``plt.title('Histogram of column_name')``
    ``plt.grid(True)``
    ``plt.show()``

   -    :'height': Correct.
        :'weight': Correct.
        :'age': Correct.
        :.*: Incorrect.



.. note:: 
      
        .. raw:: html

           <a href="/index.html" >Click here to go back to the main page</a>


 
