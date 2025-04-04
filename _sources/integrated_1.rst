Integrated Example - 1
===============================

In Champaign-Urbana, a city known for its vibrant food scene, local residents and visitors alike are often on the lookout for the best dining experiences. To facilitate this, we aim to fetch restaurant ratings using an API that provides user reviews and ratings for eateries in the area. 

To achieve this, we will use a series of programming plans that integrate the process of setting up the API request, sending the request, and processing the response. This involves:

- Specifying the URL of the API that provides restaurant reviews.
- Setting the parameters to focus on reviews from Champaign-Urbana, with the type of information being ratings and a specific date of interest.
- Executing a GET request to the API using the specified URL and parameters.
- Checking the response code to ensure the request was successful before displaying the ratings.

The following table outlines the expected parameters and their values:

+------------+------------------+-----------+
| Parameter  | Value            | Purpose   |
+============+==================+===========+
| date       | 2023-10-01       | Filter by date |
+------------+------------------+-----------+
| location   | Champaign-Urbana | Focus on location |
+------------+------------------+-----------+
| type       | rating           | Specify data type |
+------------+------------------+-----------+

image[Map of Champaign-Urbana with highlighted restaurants]

By following this process, users can efficiently retrieve up-to-date ratings for restaurants in Champaign-Urbana, assisting them in making informed dining decisions.

.. activecode:: integrated_1
   :language: sql

   # Enter the URL for the API you will use.
   import requests
   target_url = 'https://api.restaurantreviews.com/v1/reviews'
   

   # Enter parameters that will affect the response from the API.
   my_params = {
       "date": "2023-10-01", "location": "Champaign-Urbana", "type": "rating",
   }

   # Call the API by making a GET request to the server.
   response = requests.get(target_url, params=my_params)
   

   # Check if response was successful, and show the data or the error message depending on the result.
   # Check the result of the request
   if response.status_code == 200:
       print(response.json())

This example uses the following programming plans:

.. toctree::
   :maxdepth: 1
   set_target_url
   set_parameters
   make_get_request
   show_result_if_successful

.. plandisplay:: plans.jsonset_target_url_code
   :plan: Set Target URL

.. plandisplay:: plans.jsonset_parameters_code
   :plan: Set Parameters

.. plandisplay:: plans.jsonmake_get_request_code
   :plan: Make GET Request

.. plandisplay:: plans.jsonshow_result_if_successful_code
   :plan: Show Result If Successful


