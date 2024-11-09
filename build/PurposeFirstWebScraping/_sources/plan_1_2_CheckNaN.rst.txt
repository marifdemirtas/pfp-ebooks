..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan2
..  description:: Worked examples plus practice for Plan2.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: Plan2-

.. Plan2:

Plan2: Check NaN
#####################################

Plan2: Example
====================================

This is a plan

.. plandisplay:: plans.json
    :plan: Check NaN

Plan2: When to use this plan
====================================

This plan is used when...

Plan2: How to use this plan
====================================

.. changeable_areas:: Plan2_click


Plan 1: Exercises
====================================

.. clickablearea:: Check NaN_click
    :question: Click on parts of the code that would be modified to adapt this plan to a new problem.
    :iscode:
    :feedback: Check out the changeable areas for this plan above to identify what you should change in this example.

    :click-incorrect:# Handling missing data with fillna:endclick:
    :click-incorrect:df_filled = df.fillna({:endclick::click-correct:'C': 0:endclick::click-incorrect:}):endclick:


.. fillintheblank:: 'Check NaN_fill'

   Fill in the plan to...

   ``# Handling missing data with fillna``

   ``df_filled = df.fillna({`` |blank| ``})``


   -    :'A'\:\sdf['A'].mean(): Correct.
        :'B'\:\sdf['B'].median(): Correct.
        :'C'\:\s0: Correct.
        :.*: Incorrect.



.. note:: 
      
        .. raw:: html

           <a href="/index.html" >Click here to go back to the main page</a>


 
