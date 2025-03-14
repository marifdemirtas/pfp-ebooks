..  shortname:: get_best_value

..  description:: Retrieve the 'best' value based on a metric from a specific column and label it as 'max_value'


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan: Get Best Value
========================

.. plandisplay:: plans.jsonget_best_value_code
   :plan: Get Best Value

This is a plan

Plan I - When to use this plan?
--------------------------------
This plan is used when...

Plan I - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, follow these steps...

Plan I - Exercises
--------------------
.. mchoice:: get_best_value_q1
   :random: 
   :answer_a: SELECT MAX(price) AS best_value FROM products;
   :feedback_a: Correct!
   :answer_b: SELECT MIN(price) AS best_value FROM products;
   :feedback_b: This option retrieves the minimum price, but the goal is to find the highest price.
   :answer_c: SELECT MAX(column) AS best_value FROM table_name;
   :feedback_c: This option incorrectly uses 'column' and 'table_name' instead of 'price' and 'products'.
   :answer_d: SELECT price AS best_value FROM products;
   :feedback_d: This option selects the price without using an aggregate function to find the maximum value.
   :correct: a

   In a database of products, you want to find the highest price among all products and label it as 'best_value'. Which SQL query would you use?

.. mchoice:: get_best_value_q2
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: Incorrect. The query does indeed use the MIN function to find the lowest price from the 'price' column in the 'products' table, which matches the plan goal of retrieving the 'best' value based on the metric of minimum price.
   :correct: a

   In a database of products, the following SQL query is used to find the lowest price of a product: SELECT MIN(price) AS best_value FROM products;

.. fillintheblank:: get_best_value_q3

   You are asked to find the highest price from the 'products' table. Which function will you use to retrieve the 'best' value?

   ``SELECT `` |blank| ``(@@col@@) AS best_value``

   ``FROM table_name;``

   -   :MAX: Correct.
       :MIN: Correct.
       :x: Try again.

.. clickablearea:: get_best_value_q4
   :question: Click on the areas to configure a SQL query that retrieves the maximum or minimum value from a specific column in a table.
   :iscode:

   :click-incorrect::click-incorrect::click-incorrect:SELECT :click-correct:MAX:endclick:(:click-correct:column:endclick:) AS best_value:endclick::endclick::endclick:
   :click-incorrect::click-incorrect::click-incorrect:FROM :click-correct:table_name:endclick:;:endclick::endclick::endclick:
.. parsonsprob:: get_best_value_q5

   Arrange the SQL code blocks to retrieve the highest price from the products table and label it as 'max_value'.

   -----

   SELECT MAX(price) AS max_value
   =====
   FROM products;
   =====
   SELECT MIN(price) AS max_value #distractor
   =====
   FROM table_name; #distractor

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    