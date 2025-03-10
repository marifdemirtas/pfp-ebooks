Integrated Example - Remove Null Values
================================================

This example demonstrates the integration of multiple programming plans from the "Remove Null Values" group.

.. activecode:: integrated_remove_null_values
   :language: python

   # Remove Null
   DELETE FROM @@table@@
   WHERE @@column_to_check@@ IS NULL;

Related Plans:

.. plandisplay:: plans.jsonremove_null_code
   :plan: Remove Null

* :doc:`remove_null` - Remove records where a column value does not exist


