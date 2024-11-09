..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan1
..  description:: Worked examples plus practice for Plan1.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: Plan1-

.. Plan1:

Plan1: Load Data
#####################################

Plan1: Example
====================================

This is a plan

.. plandisplay:: plans.json
    :plan: Load Data

Plan1: When to use this plan
====================================

This plan is used when...

Plan1: How to use this plan
====================================

.. changeable_areas:: Plan1_click


Plan 1: Exercises
====================================

.. clickablearea:: Load Data_click
    :question: Click on parts of the code that would be modified to adapt this plan to a new problem.
    :iscode:
    :feedback: Check out the changeable areas for this plan above to identify what you should change in this example.

    :click-incorrect:import pandas as pd:endclick:
    :click-incorrect::endclick:
    :click-incorrect:df = pd.read_csv(:endclick::click-correct:data.csv:endclick::click-incorrect:):endclick:


.. fillintheblank:: 'Load Data_fill'

   Fill in the plan to...

   ``import pandas as pd``

   ``df = pd.read_csv(`` |blank| ``)``


   -    :data.csv: Correct.
        :.*: Incorrect.



.. note:: 
      
        .. raw:: html

           <a href="/index.html" >Click here to go back to the main page</a>


 
