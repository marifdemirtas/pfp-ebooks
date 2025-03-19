..  shortname:: update_records_conditionally

..  description:: Update the value of a column in all records meeting a condition


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan: Update Records Conditionally
======================================

.. plandisplay:: plans.jsonupdate_records_conditionally_code
   :plan: Update Records Conditionally

This is a plan

Plan I - When to use this plan?
--------------------------------
This plan is used when...

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, follow these steps...

Plan I - Exercises
--------------------
.. clickablearea:: update_records_conditionally_q1
   :question: You need to update the email addresses of users in a database if their current email address matches a certain condition. Click on the field that you would need to change to check if the email column in the given table is 'test@email.com'.
   :iscode:

   :click-incorrect:UPDATE table_name:endclick:
   :click-incorrect:SET column1 = 0:endclick:
   :click-incorrect:WHERE :endclick::click-correct:column1:endclick::click-incorrect: = :endclick::click-correct:min_val:endclick::click-incorrect:;:endclick:
.. clickablearea:: update_records_conditionally_q2
   :question: You need to update the verification status of users in a database if their current email address matches a certain condition. Click on the field that you would need to change to set the verified_status column to True.
   :iscode:

   :click-incorrect:UPDATE table_name:endclick:
   :click-incorrect:SET :endclick::click-correct:column1:endclick::click-incorrect: = :endclick::click-correct:0:endclick::click-incorrect::endclick:
   :click-incorrect:WHERE column1 = min_val;:endclick:
.. mchoice:: update_records_conditionally_q3
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: Ensure that the column being checked is correctly specified and that the new value is being set to the desired column.
   :correct: a

   In a database of customer records, you want to update all records with an email of 'test@email.com' by setting their 'column_name' to 'a_new_value'. The query 'UPDATE table_name SET column_name = 'a_new_value' WHERE column1 = 'test@email.com';' will achieve this goal.

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    