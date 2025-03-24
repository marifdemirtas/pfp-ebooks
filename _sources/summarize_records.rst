..  shortname:: summarize_records

..  description:: Calculate aggregated summary statistics for the whole table, or for subsets of the table


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 6: Summarize Records
===========================

.. plandisplay:: plans.jsonsummarize_records_code
   :plan: Summarize Records

This is a plan to view records summarized by some attribute. By summarize, we mean using some kind of aggregation function: such as taking the mean, maximum, minimum, or sum of the values. You can calculate this summary in subsets of the data (by using the GROUP BY part of the query), or you can calculate the summary values across all records.

Plan 6 - When to use this plan?
--------------------------------
This plan is used when you want to get insights about your data by using statistical aggregation functions. You can use the 'GROUP BY' part to get results **for each subgroup**.

Plan 6 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, replace the name of the table with your table, decide which function you want to use and which column(s) you want to summarize or see. If you want to calculate summary values over subsets, keep the GROUP BY line in the query and replace the column with a field. A separate group will be shown for each value of that field. For example, if you select AVG(quiz_grade) and if you group by letter_grade, you can see what was the average quiz grade for students who got an A, for students who got a B, etc.

Plan 6 - Exercises
--------------------
.. parsonsprob:: plan_6_q1

   Arrange the following SQL query blocks to calculate the maximum value of 'column_2' for each genre in the 'movies' table.

   -----

   SELECT genre, MAX(column_2)
   =====
   FROM movies
   =====
   GROUP BY genre
   =====
   SELECT title, AVG(column1) #distractor
   =====
   GROUP BY column_name #distractor

.. mchoice:: plan_6_q2
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: This query correctly uses the 'AVG' aggregation function on the 'rating' column and groups the results by 'genre', which is a valid approach to obtain the average rating for each genre.
   :correct: a

   In the context of a movie database, using the plan 'Summarize Records', the SQL query ``SELECT genre, AVG(rating) FROM movies GROUP BY genre;`` correctly calculates the average rating for each genre.

.. mchoice:: plan_6_q3
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: Make sure to check if the aggregation function and the column names used in the query match the plan's template structure.
   :correct: a

   Using the 'Summarize Records' plan, the following query will correctly calculate the average rating of movies grouped by genre: ``SELECT genre, AVG(rating) FROM movies GROUP BY genre;``

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   🔎  First, complete the next two questions (Q2a and Q2b) on your worksheet.
   Then, if you completed all the activities on this page, click on the arrow on the bottom right to continue.