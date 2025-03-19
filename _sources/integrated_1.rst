Integrated Example - 1
===============================

In the realm of social media analytics, particularly for platforms like TikTok, understanding and optimizing engagement metrics is crucial. The 'tiktok_engagement' table stores various metrics associated with user interactions. However, not all columns provide valuable insights; some may hinder efficient data processing.

In this example, we aim to refine our dataset and derive valuable statistics from it. Initially, we will remove a column deemed unnecessary for our current analysis—'unnecessary_metric'. This streamlining allows us to focus on relevant metrics that impact engagement.

Subsequently, we will calculate the average number of likes each post receives, providing a baseline for assessing engagement. This statistic helps gauge the effectiveness of content and informs potential strategy adjustments.

Lastly, we will conditionally update the 'engagement_score' for posts that have garnered more than 100 likes. By boosting the visibility of these posts, we aim to enhance user interaction and retention.

Example Data:

+------------+-------------------+------------------+
| post_id    | likes             | engagement_score |
+============+===================+==================+
| 1          | 120               | 50               |
+------------+-------------------+------------------+
| 2          | 80                | 40               |
+------------+-------------------+------------------+
| 3          | 150               | 60               |
+------------+-------------------+------------------+

image[TikTok engagement visualization]

.. activecode:: integrated_1
   :language: sql

   # Alter the existing table to remove an unnecessary column
   ALTER TABLE tiktok_engagement
   DROP COLUMN unnecessary_metric;

   # Calculate aggregated summary statistics for the whole table, or for subsets of the table
   SELECT AVG(likes) 
   FROM tiktok_engagement;
   

   # Update the value of a column in all records meeting a condition
   UPDATE tiktok_engagement
   SET engagement_score = engagement_score * 1.1
   WHERE likes = 100;

Related Plans:

.. plandisplay:: plans.jsondrop_column_code
   :plan: Drop Column

* Click to go to the plan page for :doc:`drop_column`

.. plandisplay:: plans.jsonview_processed_records_code
   :plan: View Processed Records

* Click to go to the plan page for :doc:`view_processed_records`

.. plandisplay:: plans.jsonupdate_records_conditionally_code
   :plan: Update Records Conditionally

* Click to go to the plan page for :doc:`update_records_conditionally`


