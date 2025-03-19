..  shortname:: view_processed_records

..  description:: Calculate aggregated summary statistics for the whole table, or for subsets of the table


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan: View Processed Records
================================

.. plandisplay:: plans.jsonview_processed_records_code
   :plan: View Processed Records

This is a plan

Plan I - When to use this plan?
--------------------------------
This plan is used when...

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, follow these steps...

Plan I - Exercises
--------------------
.. mchoice:: view_processed_records_q1
   :random: 
   :answer_a: SELECT AVG(grade) FROM students;
   :feedback_a: Correct!
   :answer_b: SELECT LENGTH(grade) FROM students;
   :feedback_b: The LENGTH function is used to calculate the length of a string, not to find an average.
   :answer_c: SELECT AVG(age) FROM students;
   :feedback_c: This query calculates the average age, not the grade.
   :answer_d: SELECT SUM(grade) FROM students;
   :feedback_d: This query sums up the grades instead of calculating the average.
   :correct: a

   You are given a database table named 'students' with columns 'name', 'age', and 'grade'. You need to calculate the average grade of all students. Which SQL query correctly uses the 'View Processed Records' plan to achieve this?

.. fillintheblank:: view_processed_records_q2
   :code_template: |
      SELECT @@blank1@@(column_name) 
      FROM table_name;
   :correct: ["SUM"]
   :feedback: ["Try using one of these values: processing_function, LENGTH, AVG"]
   :placeholder: ["Enter the appropriate value"]

   Suppose you have a database table named 'sales_data' which contains information about sales transactions. You want to calculate the sum of all sales figures in a column named 'total_sales'. Fill in the blank in the SQL query template to achieve this.

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    