Example 3: Tracking new movie releases
===============================

In this context, we are managing a database of movie releases. Each record in the database represents a movie, with details such as the movie title, release date, and genre. Our database needs to be updated regularly with new movie releases. 

To track the status of movie industry, we also want to generate reports on how many movies have been released in each genre. 

To achieve this, we will use two key SQL operations: inserting new records into the database and summarizing records to understand trends. 

Below is a sample structure of the 'movies' table in the database:

+-------------+-------------+-----------+
| Title       | Release Date| Genre     |
+=============+=============+===========+
| Oppenheimer | 2023-07-21  | Drama     |
+-------------+-------------+-----------+
| Barbie      | 2023-07-21  | Comedy    |
+-------------+-------------+-----------+
| Spider-Man  | 2021-12-17  | Action    |
+-------------+-------------+-----------+
| Everything  | 2022-03-25  | Sci-Fi    |
+-------------+-------------+-----------+
| Avatar      | 2009-12-18  | Sci-Fi    |
+-------------+-------------+-----------+
| Get Out     | 2017-02-24  | Horror    |
+-------------+-------------+-----------+
| La La Land  | 2016-12-09  | Musical   |
+-------------+-------------+-----------+
| Parasite    | 2019-10-11  | Drama     |
+-------------+-------------+-----------+

We will demonstrate how to insert a new movie record into this table and how to summarize the number of movies for each genre. This will help us keep the database updated and generate insightful reports on movie genre trends.

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Click on <b>Save & Run</b> to see the code run.

.. activecode:: integrated_4
   :language: sql
   :dburl: /_static/movies.sqlite3

   -- Insert a new record (row) into the specified table with values for specified columns
   INSERT INTO movies (title, release_date, genre) 
   VALUES ('Inception', '2010-07-16', 'Sci-Fi') 

   -- Calculate aggregated summary statistics for the whole table, or for subsets of the table
   SELECT genre, COUNT(title) 
   FROM movies 
   GROUP BY genre;


This example uses the following programming plans:

.. toctree::
   :maxdepth: 1
   
   add_new_record
   summarize_records

.. plandisplay:: plans.jsonadd_new_record_code
   :plan: Add New Record

.. plandisplay:: plans.jsonsummarize_records_code
   :plan: Summarize Records


.. shortanswer:: integrated_4_q1

   Click on "Show Examples" three times each for the plans above. What are some other values for the changeable parts of these plans?


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Click on the arrow on the bottom right to continue.