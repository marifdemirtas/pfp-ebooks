Integrated Example - 4
===============================

In this context, we are managing a database of movie releases. Each record in the database represents a movie, with details such as the movie title, release date, and genre. Our database needs to be updated regularly with new movie releases, and we also want to generate reports on how many movies have been released in each genre. 

To achieve this, we will use two key SQL operations: inserting new records into the database and summarizing records to understand trends. 

Below is a sample structure of the 'movies' table in the database:

+-------------+-------------+-----------+
| Title       | Release Date| Genre     |
+=============+=============+===========+
| Inception   | 2010-07-16  | Sci-Fi    |
+-------------+-------------+-----------+
| Avatar      | 2009-12-18  | Sci-Fi    |
+-------------+-------------+-----------+
| Titanic     | 1997-12-19  | Romance   |
+-------------+-------------+-----------+

We will demonstrate how to insert a new movie record into this table and how to summarize the number of movies for each genre. This will help us keep the database updated and generate insightful reports on movie genre trends.

.. activecode:: integrated_4
   :language: sql

   # Insert a new record (row) into the specified table with values for specified columns
   INSERT INTO movies (title, release_date, genre) 
   VALUES ('Inception', '2010-07-16', 'Sci-Fi') 

   # Calculate aggregated summary statistics for the whole table, or for subsets of the table
   SELECT genre, COUNT(title) 
   FROM movies 
   GROUP BY genre;

Related Plans:

.. plandisplay:: plans.jsonadd_new_record_code
   :plan: Add New Record

* Click to go to the plan page for :doc:`add_new_record`

.. plandisplay:: plans.jsonsummarize_records_code
   :plan: Summarize Records

* Click to go to the plan page for :doc:`summarize_records`


