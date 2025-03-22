How to query data with SQL?
==============================

Welcome! We have learned how databases work and why you might want to use them to organize your data. In this lab, we will go over *four* common types of SQL queries: Creating new records, Updating existing records, Reading records, and Deleting records (known as CRUD operations). 

As a reminder, SQL queries are run on **tables**. Tables are like spreadsheets, with rows and columns. Each row represents a **record**, and each column represents a **field** in that record. For example, each **record** might be a student, with **fields** being IDs, names, grades.

+------------+----------------------+-----------+
| student_id | name                 | grade     |
+============+======================+===========+
| 001        | James Smith          | A         |
+------------+----------------------+-----------+
| 002        | Michael Brown        | B+        |
+------------+----------------------+-----------+
| 005        | Mary Wilson          | A         |
+------------+----------------------+-----------+
| 006        | Jennifer Garcia      | A-        |
+------------+----------------------+-----------+
| 007        | Elizabeth Martinez   | B+        |
+------------+----------------------+-----------+
| 008        | Patricia Anderson    | A         |
+------------+----------------------+-----------+
| ...        | ...                  | ...       |
+------------+----------------------+-----------+
| 015        | David Taylor         | A-        |
+------------+----------------------+-----------+

------------------------------

.. admonition:: Tutorial Structure
   :class: note

   This tutorial is organized around common *patterns* in SQL queries, also known as programming plans.

   Each programming plan has a clear goal describing what it helps you achieve, a code template that you can modify for your own use case, and annotations on which areas to change.

   Throughout the tutorial, you will first see real-world examples of how SQL is used, and then you will see how these examples break down into plans.

======

.. highlightedtextbox::
   :title: Getting Started
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Look for these golden boxes for instructions. You will see a magnifying glass (🔎) when you need to go back to your worksheet.

   To start, click on the arrow on the bottom right (or the link below that says "Before You Start The Activity").


.. toctree::
   :maxdepth: 2
   
   start_here
   integrated_3.rst
   integrated_2.rst
   integrated_4.rst
   codewriting-1
   codereading-1
   end_here_comparison
   end_here_usability

