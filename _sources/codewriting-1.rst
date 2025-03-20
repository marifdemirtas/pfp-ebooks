Exercise: Writing Queries for Ad Management
================================

Let's assume that you are running the advertisement campaign for a drink company. You have multiple ads with different celebrities, and you keep track of who you worked with, the cost of each ad, and projected reach (how many users have seen the ad). Here's an example table: 

image[Ad campaign with celebrity endorsements]

+------------+----------------+-----------------+
| Celebrity  | Ad Cost (USD)  | Projected Reach |
+============+================+=================+
| A-list     | 50,000         | 500,000         |
+------------+----------------+-----------------+
| B-list     | 30,000         | 300,000         |
+------------+----------------+-----------------+
| C-list     | 10,000         | 150,000         |
+------------+----------------+-----------------+

.. parsonsprob:: 1_q1

   You just started a new ad campaign with celebrity John Doe. However, to afford it, you will need to stop the ad campaign with the lowest reach *first*. Which plans could you use to achieve this? Order them below.

   -----

   Order Records
   =====
   Remove Records
   =====
   Add New Record
   =====
   Summarize Records
   =====
   View Records #distractor
   =====
   Update Records Conditionally #distractor
   

.. parsonsprob:: 1_q2

   Assuming that you have already started your John Doe campaign, how can you calculate the average cost of all your ad campaigns?

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
   

   

