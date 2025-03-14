..  shortname:: remove_null

..  description:: Remove records where a column value does not exist


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan: Remove Null
=====================

.. plandisplay:: plans.jsonremove_null_code
   :plan: Remove Null

This is a plan

Plan I - When to use this plan?
--------------------------------
This plan is used when...

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, follow these steps...

Plan I - Exercises
--------------------
.. mchoice:: remove_null_q1
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: The statement is True because the SQL query removes all records where the 'email' column value is NULL, effectively removing entries where the email is not set.
   :correct: a

   In a database containing a 'users' table, executing the plan 'Remove Null' on the 'email' column will remove all records where the email is not set.

.. parsonsprob:: remove_null_q2

   You have a table named 'employees' in your SQL database, and you need to remove all records where the 'email' column is NULL. Arrange the following code blocks in the correct order to accomplish this task.

   -----

   DELETE FROM employees
   =====
   WHERE email IS NULL;
   =====
   UPDATE employees SET email = '' #distractor
   =====
   WHERE email IS NOT NULL; #distractor

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    