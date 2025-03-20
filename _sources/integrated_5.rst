Example: Looking at student records in a school database
===============================

In the context of managing a school's database system, there is a need to access and review student records efficiently. The database contains a table named 'student_grades' that stores information about students, including their unique student identifiers, names, and their respective grades in various subjects. To facilitate the process of monitoring academic performance and conducting administrative tasks, such as preparing report cards or identifying students eligible for academic awards, we need to be able to select and view specific columns from this table.

Consider the following example data setup for the 'student_grades' table:

+------------+------------+-----------+
| student_id | name       | grade     |
+============+============+===========+
| 001        | John Doe   | A         |
+------------+------------+-----------+
| ...        | ...        | ...       |
+------------+------------+-----------+
| 915        | Emily Jones| A-        |
+------------+------------+-----------+

By executing the appropriate SQL query, we can quickly look at what data has been stored in the database, *SELECT*ing only the relevant columns.

.. activecode:: integrated_5
   :language: sql

   -- Select and view columns from the specified table
   SELECT student_id, name, grade
   FROM student_grades;


This example uses the following programming plans:

.. toctree::
   :maxdepth: 1
   
   view_records


.. plandisplay:: plans.jsonview_records_code
   :plan: View Records
