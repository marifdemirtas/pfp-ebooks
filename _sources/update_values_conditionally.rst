..  shortname:: update_values_conditionally

..  description:: Update the value of a column in all records meeting a condition


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Update Values Conditionally
==============================

.. plandisplay:: plans.jsonupdate_values_conditionally_code
   :plan: Update Values Conditionally

This is a plan

Plan I - When to use this plan?
--------------------------------
This plan is used when...

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, follow these steps...

Plan I - Exercises
--------------------
.. parsonsprob:: update_values_conditionally_q1

   Update the blocks to complete the code.

   -----

   UPDATE @@table@@
   =====
   SET @@column_to_update@@ = @@new_value@@
   =====
   WHERE @@column_to_check@@ = @@condition_value@@;

.. fillintheblank:: update_values_conditionally_q2

   Fill in the blanks to replace all records where the column is equal to min_val

   ``UPDATE table_name``

   ``SET column1 = 0``

   ``WHERE @@column_to_check@@ = `` |blank| ``;``

   -   :min_val: Correct.
       :x: Try again.

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    