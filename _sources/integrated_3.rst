Example: Dropping students with failing grades from the class
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

.. activecode:: integrated_3
   :language: sql

   -- Remove records where the value in a column meets a condition
   DELETE FROM student_grades
   WHERE grade < 60;

   -- Select and view columns from the specified table
   SELECT student_id, name, grade
   FROM student_grades;


This example uses the following programming plans:


.. plandisplay:: plans.jsonremove_records_code
   :plan: Remove Records


.. plandisplay:: plans.jsonview_records_code
   :plan: View Records


.. shortanswer:: integrated_3_q1
   Click on "Show Examples" three times each for the plans above. Did you notice anything?


.. toctree::
   :maxdepth: 1
   :hidden:
   
   remove_records
   view_records

