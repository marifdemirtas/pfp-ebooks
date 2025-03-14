Integrated Example - update min
========================================

In this scenario, we are managing a database of products that includes a variety of items, such as albums from various artists. We want to focus specifically on albums by Taylor Swift. Our task is to identify the album with the lowest price (the 'best' value in this context being the minimum price) and then update the product database to remove any discounts on this album, as it is already being sold at the lowest possible price. The database table 'products' has columns such as 'price' and 'discount'.

To achieve this, we will first retrieve the minimum price of Taylor Swift albums using the `Get Best Value` plan. Once we have the minimum price, we will use it as a condition to update the discounts for those albums using the `Update Values Conditionally` plan.

Here is an example of the 'products' table:

+------------+------------+-----------+
| Product ID | Price      | Discount  |
+============+============+===========+
| 1          | 15.99      | 5         |
+------------+------------+-----------+
| 2          | 12.99      | 0         |
+------------+------------+-----------+
| 3          | 9.99       | 3         |
+------------+------------+-----------+

In this case, if Product ID 3 is a Taylor Swift album, we would identify 9.99 as the minimum price and set its discount to 0.

.. activecode:: integrated_update_min
   :language: python

   # Retrieve the 'best' value based on a metric from a specific column and label it as 'max_value'
   SELECT MIN(price) AS best_value
   FROM products;

   # Update the value of a column in all records meeting a condition
   UPDATE products
   SET discount = @@new_value@@
   WHERE price = min_val;

Related Plans:

.. plandisplay:: plans.jsonget_best_value_code
   :plan: Get Best Value

* Click to go to the plan page for :doc:`get_best_value`

.. plandisplay:: plans.jsonupdate_values_conditionally_code
   :plan: Update Values Conditionally

* Click to go to the plan page for :doc:`update_values_conditionally`


