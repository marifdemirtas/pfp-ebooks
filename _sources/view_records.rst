..  shortname:: view_records

..  description:: Select and view columns from the specified table


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 2: View Records
======================

.. plandisplay:: plans.jsonview_records_code
   :plan: View Records

The most fundamental query we will learn about is viewing records from the table using SELECT. This query will return a list of records (rows). For each record, you can see values for the fields (columns) that you specify in the query.

Plan 2 - When to use this plan?
--------------------------------
Use this plan when you want to **view** some values in the database without modifying the table.

Plan 2 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, replace the table with the table you want to get records (rows) from, and specify the fields (columns) you want to look for.

Plan 2 - Exercises
--------------------
.. fillintheblank:: plan_2_q1
   :code_template:
      SELECT @@blank1@@
      FROM student_grades;
   :correct: ["student_id"]
   :feedback: ["Try using student_id as the name of the field."]
   :placeholder: ["Enter the appropriate value"]

   Complete the query to show the values of student_id for all records in the table student_grades.

.. mchoice:: plan_2_q2
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: The SQL statement is correct. Using '*' in the SELECT clause retrieves all columns from the specified table, which in this case is 'student_grades'.
   :correct: a

   In the context of a database system where you want to view student records, the following SQL statement correctly selects all columns from the student_grades table: ``SELECT * FROM student_grades;``

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.