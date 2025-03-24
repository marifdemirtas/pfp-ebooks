..  shortname:: order_records

..  description:: View records sorted in a given order


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 4: Order Records
=======================

.. plandisplay:: plans.jsonorder_records_code
   :plan: Order Records

This plan is used to see records (rows) sorted by some field (column), without actually modifying the table. The sorting will only apply to the output you see. It will not be ordered if you try to see it with a regular SELECT query.

Plan 4 - When to use this plan?
--------------------------------
This plan may be used to see who are the top performers in a class, or which products in a database have the cheapest prices.

Plan 4 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, complete the fields of the regular SELECT query as you saw in 'View Records', and then provide which field (column) to sort the records by, along with whether you want it ascending or descending. 

Plan 4 - Exercises
--------------------
.. mchoice:: plan_4_q1
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: Remember that DESC is used to sort results in descending order, which means from newest to oldest.
   :correct: a

   In a music database, to view all songs sorted by their release date in descending order, the following query is used: ``SELECT * FROM songs ORDER BY release_date DESC``;

.. mchoice:: plan_4_q2
   :random: 
   :answer_a: SELECT * FROM songs ORDER BY release_date DESC;
   :feedback_a: Correct!
   :answer_b: SELECT * FROM songs ORDER BY release_date ASC;
   :feedback_b: This option sorts the songs in ascending order, showing the oldest songs first. You need to sort them in descending order.
   :answer_c: SELECT * FROM songs ORDER BY column_name DESC;
   :feedback_c: This option uses 'column_name' instead of 'release_date'. Make sure to use the correct column to sort by.
   :answer_d: SELECT * FROM table_name ORDER BY release_date DESC;
   :feedback_d: This option uses 'table_name' instead of 'songs'. Ensure you are querying from the correct table.
   :correct: a

   You are working with a music database and need to retrieve a list of songs sorted by their release date in descending order. Which SQL query would you use?

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.