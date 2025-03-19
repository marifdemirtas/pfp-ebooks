..  shortname:: drop_column

..  description:: Alter the existing table to remove an unnecessary column


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan: Drop Column
=====================

.. plandisplay:: plans.jsondrop_column_code
   :plan: Drop Column

This is a plan

Plan I - When to use this plan?
--------------------------------
This plan is used when...

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, follow these steps...

Plan I - Exercises
--------------------
.. mchoice:: drop_column_q1
   :random: 
   :answer_a: ALTER TABLE Books DROP COLUMN Edition;
   :feedback_a: Correct!
   :answer_b: ALTER TABLE Books REMOVE COLUMN Edition;
   :feedback_b: The SQL command to remove a column is 'DROP COLUMN', not 'REMOVE COLUMN'.
   :answer_c: DELETE COLUMN Edition FROM Books;
   :feedback_c: The syntax for deleting a column is incorrect. You need to use 'ALTER TABLE ... DROP COLUMN'.
   :answer_d: ALTER TABLE Books DELETE Edition;
   :feedback_d: The correct SQL syntax is 'ALTER TABLE ... DROP COLUMN', not 'DELETE COLUMN'.
   :correct: a

   You are working with a database for a library management system. The table 'Books' contains a column 'Edition' that is no longer needed. How would you remove this column from the 'Books' table?

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    