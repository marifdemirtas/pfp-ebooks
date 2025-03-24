Example 1: Dropping students with failing grades from the class
===============================

At the University of Illinois Urbana-Champaign, the registrar's office manages a database that includes a table called `student_grades`. This table contains records of students' grades for various courses. The university needs to ensure that records of students who are currently failing a course (with a grade below 60) are reviewed and potentially removed for academic advising purposes. Additionally, they want to review the list of students and their grades for reporting.

The `student_grades` table may include columns such as:

+------------+----------------------+-----------+
| student_id | name                 | grade     |
+============+======================+===========+
| 001        | James Smith          | 84        |
+------------+----------------------+-----------+
| 002        | Michael Brown        | 55        |
+------------+----------------------+-----------+
| 005        | Mary Wilson          | 68        |
+------------+----------------------+-----------+
| 006        | Jennifer Garcia      | 75        |
+------------+----------------------+-----------+
| 007        | Elizabeth Martinez   | 92        |
+------------+----------------------+-----------+
| 008        | Patricia Anderson    | 58        |
+------------+----------------------+-----------+
| ...        | ...                  | ...       |
+------------+----------------------+-----------+
| 015        | David Taylor         | 45        |
+------------+----------------------+-----------+

The goal is to remove records where the grade is below 60 and to view all students' records in the `student_grades` table.

.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Click on <b>Save & Run</b> to see the code run.

.. activecode:: example_1_q1a
   :language: sql
   :dburl: /_static/student_grades.sqlite3

   -- Remove records where the value in a column meets a condition
   DELETE FROM student_grades
   WHERE grade < 60;

   -- Select and view columns from the specified table
   SELECT student_id, name, grade
   FROM student_grades;


----------------

This example uses the following programming plans:

.. toctree::
   :maxdepth: 1
   
   remove_records
   view_records


.. plandisplay:: plans.jsonremove_records_code
   :plan: Remove Records


.. plandisplay:: plans.jsonview_records_code
   :plan: View Records


.. shortanswer:: example_1_q2

   Click on "Show Examples" three times each for the plans above. Did you notice anything?


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   🔎  First, complete the first two questions (Q1a and Q1b) on your worksheet.
   Then, click on the arrow on the bottom right to continue.