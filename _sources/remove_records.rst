..  shortname:: remove_records

..  description:: Remove records where the value in a column meets a condition


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 1: Remove Records
========================

.. plandisplay:: plans.jsonremove_records_code
   :plan: Remove Records

This plan is used to remove some records permanently from the table, using a condition to decide which records will be deleted.

Plan 1 - When to use this plan?
--------------------------------
This plan is used when you want to remove records from the table using some criteria, such as dropping all student grades below some threshold, removing records that is missing a value in the specified field, or simply processing records that are marked for deletion.

Plan 1 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, replace the table with the name of your table, and specify a condition using fields (columns) such that each record (row) that satisfies that condition will be deleted.

Plan 1 - Exercises
--------------------
.. parsonsprob:: plan_1_q1

   Rearrange the SQL code blocks to remove records from the 'student_grades' table where the 'grade' is less than 60.

   -----

   DELETE FROM student_grades
   =====
   WHERE grade < 60
   =====
   WHERE COLUMN IS NULL #distractor
   =====
   WHERE column=1 #distractor
   =====
   WHERE COLUMN < 2 #distractor

.. mchoice:: plan_1_q2
   :random: 
   :answer_a: DELETE FROM student_grades WHERE mt1 IS NULL;
   :feedback_a: Correct!
   :answer_b: DELETE FROM student_grades WHERE grade IS NULL;
   :feedback_b: This option checks the 'grades' column for non-existent (NULL) values, but not the mt1 column.
   :answer_c: DELETE FROM student_grades WHERE mt1 = 0;
   :feedback_c: This option removes records with a grade exactly equal to 0, but not for students who do not have any value.
   :correct: a

   You are working with a database containing student grades. Students who have taken the first midterm have a value under the field 'mt1'. This field is empty for students who have not taken the exam (denoted by the special value NULL). You need to remove records for students who have not taken the exam. Which SQL statement correctly achieves this task?

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.