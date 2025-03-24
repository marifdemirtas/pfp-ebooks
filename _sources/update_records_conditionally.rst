..  shortname:: update_records_conditionally

..  description:: Update the value of a column in all records meeting a condition


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 3: Update Records Conditionally
======================================

.. plandisplay:: plans.jsonupdate_records_conditionally_code
   :plan: Update Records Conditionally

This is a plan is used to update the values of some fields (columns) in existing records (rows). Only records that meet a certain condition is updated. 

Plan 3 - When to use this plan?
--------------------------------
This plan is used when you want to update the values of some fields in the table, but only for records that meet a certain condition. For example, you may want to update the status of all users who have not verified their email address, or update the location of all users who have not logged in for a certain period.

Plan 3 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, replace the table name with the name of your table, and specify the fields (columns) that you want to update, the new values that you want to set, and the condition that must be met for the records to be updated.

Plan 3 - Exercises
--------------------

.. clickablearea:: plan_3_q1
   :question: You are working in a database with user emails. You need to mark accounts that have used a test email address for deletion. One of your colleagues shared the following query, saying that you can use this as a template. Click on the field(s) that you would need to change to check if the email column in the given table is 'test@email.com'.
   :iscode:

   :click-incorrect:UPDATE users:endclick:
   :click-incorrect:SET marked_for_deletion = true:endclick:
   :click-incorrect:WHERE :endclick::click-correct:name:endclick::click-incorrect: = :endclick::click-correct:Bob:endclick::click-incorrect:;:endclick:


.. clickablearea:: plan_3_q2
   :question: You are working in a database with user emails. You need to mark accounts who have an email address on record as verified. One of your colleagues shared the following query, saying that you can use this as a template.
   Click on the field(s) that you would need to change to set the verified_status column to True.
   :iscode:

   :click-incorrect:UPDATE users:endclick:
   :click-incorrect:SET :endclick::click-correct:online_status:endclick::click-incorrect: = :endclick::click-correct:false:endclick::click-incorrect::endclick:
   :click-incorrect:WHERE email IS NOT NULL:endclick:


.. mchoice:: plan_3_q3
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: Ensure that the column being checked is correctly specified and that the new value is being set to the desired column.
   :correct: a

   In a database of customer records, you want to update all records with an email of 'test@email.com' by setting their 'column_name' to 'a_new_value'. The query <pre>'UPDATE table_name SET column_name = 'a_new_value' WHERE column1 = 'test@email.com';'</pre> will achieve this goal.

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.