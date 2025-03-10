..  shortname:: remove_null

..  description:: Remove records where a column value does not exist


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Remove Null
==============

.. plandisplay:: plans.jsonremove_null_code
   :plan: Remove Null

This plan removes records where the given column has a null value.

Plan I - When to use this plan?
--------------------------------
This plan is used when you want to calculate statistics that would be skewed by the existence of null values.

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, replace the table and the column with your data.

Plan I - Exercises
--------------------
.. mchoice:: remove_null_q1
   :answer_a: True
   :answer_b: False
   :correct: b

   This statement can only be used for columns that have numerical values.

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    