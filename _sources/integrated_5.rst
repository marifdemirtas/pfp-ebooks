Integrated Example - 5
===============================

In the context of managing a school's database system, there is a need to access and review student records efficiently. The database contains a table named 'student_grades' that stores information about students, including their unique student identifiers, names, and their respective grades in various subjects. To facilitate the process of monitoring academic performance and conducting administrative tasks, such as preparing report cards or identifying students eligible for academic awards, we need to be able to select and view specific columns from this table.

Consider the following example data setup for the 'student_grades' table:

+------------+------------+-----------+
| student_id | name       | grade     |
+============+============+===========+
| 001        | John Doe   | A         |
+------------+------------+-----------+
| 002        | Jane Smith | B         |
+------------+------------+-----------+
| 003        | Emily Jones| A-        |
+------------+------------+-----------+

By executing the appropriate SQL query, we can efficiently extract the necessary columns, enabling us to focus on the data that is most relevant for our current objectives. This query will help streamline data retrieval processes, ensuring that educators and administrators have quick access to the information they need.

.. activecode:: integrated_5
   :language: sql

   # Select and view columns from the specified table
   SELECT student_id, name, grade
   FROM student_grades;

Related Plans:

.. plandisplay:: plans.jsonview_records_code
   :plan: View Records

* Click to go to the plan page for :doc:`view_records`


