Example 2: Awarding Grammy's and finding recent Grammy nominee songs
===============================

In this example, we are managing a database of songs and their artists. Recently, several artists have won Grammy awards, and we need to update our records to reflect their new status as Grammy winners. The database contains columns such as 'artist_name', 'song_title', 'release_date', and 'award_status'. We will update the 'award_status' to 'Awarded' for all songs by artists who have won a Grammy.

Additionally, to showcase the most recent Grammy-winning songs, we will order the records by their release date in descending order. This allows us to present the latest award-winning songs at the top.

Below is an example of the table structure:

+-----------------+-------------------------+--------------+--------------+
| artist_name     | song_title              | release_date | award_status |
+=================+=========================+==============+==============+
| Taylor Swift    | Anti-Hero               | 2023-05-01   | Nominated    |
+-----------------+-------------------------+--------------+--------------+
| Harry Styles    | As It Was               | 2023-02-15   | Awarded      |
+-----------------+-------------------------+--------------+--------------+
| Adele           | Easy On Me              | 2022-11-12   | Nominated    |
+-----------------+-------------------------+--------------+--------------+
| Lizzo           | About Damn Time         | 2022-09-20   | Awarded      |
+-----------------+-------------------------+--------------+--------------+
| Beyoncé         | Break My Soul           | 2022-07-29   | Awarded      |
+-----------------+-------------------------+--------------+--------------+

By employing the plans 'Update Records Conditionally' and 'Order Records', we effectively maintain and display our data in a way that highlights recent achievements in the music industry.

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Click on <b>Save & Run</b> to see the code run.

.. activecode:: example_2_q1
   :language: sql
   :dburl: /_static/songs.sqlite3

   -- Update the value of a column in all records meeting a condition
   UPDATE songs
   SET award_status = 'Awarded'
   WHERE artist_name = 'Adele';

   -- View records sorted in a given order
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

.. shortanswer:: example_2_q2

   Click on "Show Examples" three times each for the plans above. Have you noticed any other values that could be used in these plans?


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Click on the arrow on the bottom right to continue.