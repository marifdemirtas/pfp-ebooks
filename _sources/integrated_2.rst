Example: Awarding Grammy's and finding recent Grammy nominee songs
===============================

In this example, we are managing a database of songs and their artists. Recently, several artists have won Grammy awards, and we need to update our records to reflect their new status as Grammy winners. The database contains columns such as 'artist_name', 'song_title', 'release_date', and 'award_status'. We will update the 'award_status' to 'Awarded' for all songs by artists who have won a Grammy.

Additionally, to showcase the most recent Grammy-winning songs, we will order the records by their release date in descending order. This allows us to present the latest award-winning songs at the top.

Below is an example of the table structure:

+--------------+-------------+--------------+--------------+
| artist_name  | song_title  | release_date | award_status |
+==============+=============+==============+==============+
| Artist A     | Song 1      | 2023-05-01   | Nominated    |
+--------------+-------------+--------------+--------------+
| Artist B     | Song 2      | 2023-02-15   | Awarded      |
+--------------+-------------+--------------+--------------+
| Artist C     | Song 3      | 2022-11-12   | Nominated    |
+--------------+-------------+--------------+--------------+

By employing the plans 'Update Records Conditionally' and 'Order Records', we effectively maintain and display our data in a way that highlights recent achievements in the music industry.

.. activecode:: integrated_2
   :language: sql

   # Update the value of a column in all records meeting a condition
   UPDATE songs
   SET award_status = 'Awarded'
   WHERE artist_name = 'Artist C';

   # View records sorted in a given order
   SELECT * FROM songs
   ORDER BY release_date DESC;
   

This example uses the following programming plans:

.. toctree::
   :maxdepth: 1
   
   update_records_conditionally
   order_records

.. plandisplay:: plans.jsonupdate_records_conditionally_code
   :plan: Update Records Conditionally

.. plandisplay:: plans.jsonorder_records_code
   :plan: Order Records


