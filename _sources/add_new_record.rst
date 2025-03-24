..  shortname:: add_new_record

..  description:: Insert a new record (row) into the specified table with values for specified columns


.. setup for automatic question numbering.

.. qnum::
   :start: 1

Plan 5: Add New Record
========================

.. plandisplay:: plans.jsonadd_new_record_code
   :plan: Add New Record

This is a plan to add new records (rows) into a table.

Plan 5 - When to use this plan?
--------------------------------
This plan is used when you want to add more data to a table in your database.

Plan 5 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, replace the name of the table, specify which fields will exist in the row you will insert, and then provide the values for those fields.

Plan 5 - Exercises
--------------------
.. parsonsprob:: plan_5_q1

   Arrange the code blocks to insert a new record into the 'users' table with the specified field names and values.

   -----

   INSERT INTO users (name, email)
   =====
   VALUES ('Alice', 'alice@illinois.edu')
   =====
   INSERT INTO movies (title, release_date, genre) #distractor
   =====
   VALUES ('Inception', '2010-07-16', 'Sci-Fi') #distractor

.. mchoice:: plan_5_q2
   :random: 
   :answer_a: INSERT INTO movies (title, release_date, genre) VALUES ('Inception', '2010-07-16', 'Sci-Fi');
   :feedback_a: Correct!
   :answer_b: INSERT INTO users (name, email) VALUES ('Inception', '2010-07-16', 'Sci-Fi');
   :feedback_b: Incorrect. This statement attempts to insert into the 'users' table, which is not where movie data belongs.
   :answer_c: INSERT INTO movies (name, email) VALUES ('Inception', '2010-07-16', 'Sci-Fi');
   :feedback_c: Incorrect. This statement uses the wrong field names for the 'movies' table. It should be (title, release_date, genre).
   :answer_d: INSERT INTO users (title, release_date, genre) VALUES ('Inception', '2010-07-16', 'Sci-Fi');
   :feedback_d: Incorrect. This statement attempts to insert into the 'users' table, which is not where movie data belongs.
   :correct: a

   You are tasked with adding a new record into the 'movies' table in a database using SQL. Which of the following SQL statements correctly adds a movie titled 'Inception', released on '2010-07-16', with the genre 'Sci-Fi'?

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   If you completed all the activities on this page, click on the arrow on the bottom right to continue.