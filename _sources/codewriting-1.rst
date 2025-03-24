Exercise 1: Writing Queries for Ad Management
================================

Let's assume that you are running the advertisement campaign for a drink company. You have multiple ads with different celebrities, and you keep track of who you worked with, the cost of each ad, and projected reach (how many users have seen the ad). Here's an example table: 

image[Ad campaign with celebrity endorsements]

+------------------+----------------+-----------------+
| Celebrity        | Ad Cost (USD)  | Projected Reach |
+==================+================+=================+
| Taylor Swift     | 500,000        | 5,000,000       |
+------------------+----------------+-----------------+
| George Clooney   | 300,000        | 2,000,000       |
+------------------+----------------+-----------------+
| Emma Watson      | 150,000        | 1,000,000       |
+------------------+----------------+-----------------+
| Chris Hemsworth  | 200,000        | 1,500,000       |
+------------------+----------------+-----------------+
| Jennifer Lopez   | 400,000        | 3,000,000       |
+------------------+----------------+-----------------+
| Robert Downey Jr.| 450,000        | 4,000,000       |
+------------------+----------------+-----------------+

.. parsonsprob:: exercise_1_q1

   You just started a new ad campaign with the rapper Kendrick Lamar. However, to afford it, you will need to stop the ad campaign with the lowest reach *first*. Which plans could you use to find this campaign, stop this campaign, and start the new campaign? Order them below.

   -----

   Order Records
   =====
   Remove Records
   =====
   Add New Record
   =====
   Summarize Records #distractor
   =====
   View Records #distractor
   =====
   Update Records Conditionally #distractor
   

.. parsonsprob:: exercise_1_q2

   You have already started your campaign with Kendrick Lamar. Your manager wants to learn what is the average cost for your ads. How can you calculate the average cost of all your ad campaigns?

   -----

   SELECT AVG('Ad Cost') 
   =====
   FROM 'Ads' 
   =====
   GROUP BY 'Celebrity' #distractor
   =====
   DELETE FROM 'Ad Cost' #distractor
   =====
   WHERE 'Ad Cost' = AVG('Ad Cost') #distractor
   =====
   ORDER BY 'Ad Cost' #distractor
   

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   🔎 First, complete the next question (Q3) on your worksheet.
   Then, click on the arrow on the bottom right to continue.