Example 1: Looking for Restaurant Ratings in Champaign-Urbana
===============================

Champaign and Urbana are two cities known for their vibrant food scene. Local residents and visitors alike are on the lookout for the best dining experiences in Champaign-Urbana. To facilitate this, we aim to fetch top ranking restaurants using an API that rates eateries in the area. 

To achieve this, we will send a request to an API that returns the restaurant rankings in an area. You can think of this API to be similar to Google Maps or Yelp. However, for this example, we are using a custom API: 

For Google Maps or Yelp, we would look for the **documentation** of the API by searching for "Google Maps API" or "Yelp API". The documentation of an API provides us with the necessary information on how to use the API, including:
- the **endpoint URL**, which is the URL that we will send a request to,
- its **parameters**, which is a list of values that we can share with the API to explain our request,
- and its **response**, which is what we get from the API after sending a request.

For our restaurant API, the endpoint is: https://one02-api-fastapi.onrender.com/api/restaurants.

Our API accepts the following parameters:

+------------+------------------+---------------------------------------------------------+
| Parameter  | Example Value    | Explanation                                             |
+============+==================+=========================================================+
| location   | 'champaign'      | Specify the location that you will request ratings for  |
+------------+------------------+---------------------------------------------------------+
| count      | 5                | Specify how many of the top restaurants will be shown   |
+------------+------------------+---------------------------------------------------------+

Based on this information, we can send a GET request to the API to get the restaurant ratings in Champaign-Urbana.

.. activecode:: integrated_1
   :language: python3

   # Enter the URL for the API you will use.
   import requests
   target_url = 'https://one02-api-fastapi.onrender.com/api/restaurants'
   

   # Enter parameters that will affect the response from the API.
   my_params = {
       "count": 5, 
       "location": "champaign"
   }

   # Call the API by making a GET request to the server.
   response = requests.get(target_url, params=my_params)
   

   # Check if response was successful, and show the data or the error message depending on the result.
   # Check the result of the request
   if response.status_code == 200:
       print(response.json())
   if response.status_code == 404:
       print("Error 404 (Not Found): ", response.json())


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


