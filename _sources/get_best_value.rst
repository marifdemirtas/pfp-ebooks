..  shortname:: get_best_value

..  description:: Retrieve the 'best' value based on a metric from a specific column and label it as 'max_value'


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Get Best Value
=================

.. plandisplay:: plans.jsonget_best_value_code
   :plan: Get Best Value

This plan selects the 'best' value in a column based on the function you want to use.

Plan I - When to use this plan?
--------------------------------
This plan is used when you want to learn a best value

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, pick a 'best' function (such as minimum or maximum) on your data.

Plan I - Exercises
--------------------
.. parsonsprob:: get_best_value_q1

   undefined

   -----

   SELECT @@best_function@@(@@col@@)
   =====
   AS best_value
   =====
   FROM @@table@@;
   =====
   SELECT best_function #distractor

.. mchoice:: get_best_value_q2
   :random: 
   :answer_a: SELECT MAX(revenue) AS best_value FROM sales_data;
   :answer_b: SELECT MIN(revenue) AS best_value FROM sales_data;
   :answer_c: SELECT MAX(revenue) AS max_value FROM sales_data;
   :answer_d: SELECT MAX(revenue) FROM sales_data;
   :correct: a

   You have a database table named 'sales_data' with a column 'revenue'. You need to write a SQL query to retrieve the maximum revenue and label it as 'best_value'. Which of the following SQL queries will achieve this?

.. mchoice:: get_best_value_q3
   :answer_a: True
   :answer_b: False
   :correct: a

   In the context of a database storing product prices, using the code template 'SELECT MAX(price) AS best_value FROM products;' will correctly retrieve the highest product price and label it as 'max_value'.

.. fillintheblank:: get_best_value_q4

   You're working with a database of student scores and want to retrieve the highest score from the 'math_scores' column of the 'student_data' table. Fill in the correct function to use in the SQL query.

   ``SELECT `` |blank| ``(@@col@@) ``

   ``AS best_value``

   ``FROM table_name;``

   -   :MAX: Correct.
       :MIN: Correct.
       :x: Try again.

.. parsonsprob:: get_best_value_q5

   Arrange the SQL query blocks to find the maximum salary from the employees table and label it as max_value.

   -----

   AS max_value
   =====
   SELECT MAX(salary)
   =====
   FROM employees
   =====
   AS best_value #distractor
   =====
   SELECT MIN(salary) #distractor
   =====
   FROM salaries #distractor

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    