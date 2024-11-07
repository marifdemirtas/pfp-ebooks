..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan3
..  description:: Worked examples plus practice for Plan3.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: Plan3-

.. Plan3:

Plan3: Filter Values
#####################################

Plan3: Example
====================================

This is a plan

.. plandisplay:: plans.json
    :plan: Filter Values

Plan3: When to use this plan
====================================

This plan is used when...

Plan3: How to use this plan
====================================

.. changeable_areas:: Plan3_click


Plan 1: Exercises
====================================

.. clickablearea:: Filter Values_click
    :question: Click on areas to change for...
    :iscode:
    :feedback: Check out the example of this plan above to identify the area that should be changed.

    :click-incorrect:# Keep elements that satisfy the given condition:endclick:
    :click-incorrect:filtered_df = df[:endclick: :click-correct:condition:endclick: :click-incorrect:]:endclick:


.. fillintheblank:: 'Filter Values_fill'
    Fill in the plan to...
    ``# Keep elements that satisfy the given condition``
    ``filtered_df = df[``|blank|

    ````

   -    :(df['A'] > 2) & (df['B'] < 50): Correct.
        :(df['date_column'] >= start_date) & (df['date_column'] <= end_date): Correct.
        :df['A'] > 25: Correct.
        :.*: Incorrect.



.. note:: 
      
        .. raw:: html

           <a href="/index.html" >Click here to go back to the main page</a>


 
