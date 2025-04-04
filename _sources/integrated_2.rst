Integrated Example - 2
===============================

In this example, we will integrate several programming plans to fetch a 5-day weather forecast for New York, NY using a paid API from weather.com. The goal is to demonstrate how to set up a basic API call with authentication and parameters to retrieve specific data. We will use a Bearer token for authentication, which is common for paid APIs that require user identification and authorization. The API will return weather data in JSON format, which we will check for successful retrieval before printing. This example is useful for developers who need to integrate weather data into their applications for features like weather widgets, alerts, or travel planning.

+----------------+---------------+-----------------+
| Parameter      | Value         | Description     |
+================+===============+=================+
| start_date     | 2023-10-01    | Start date for  |
|                |               | the forecast    |
+----------------+---------------+-----------------+
| location       | New York, NY  | Location for    |
|                |               | the forecast    |
+----------------+---------------+-----------------+
| units          | metric        | Measurement     |
|                |               | units for data  |
+----------------+---------------+-----------------+

We will walk through setting the target URL, parameters, authentication credentials, and making the GET request, followed by handling the API response.

.. activecode:: integrated_2
   :language: sql

   # Enter the URL for the API you will use.
   import requests
   target_url = 'https://api.weather.com/v3/wx/forecast/daily/5day'
   

   # If the API requires a log in or a similar authentication, share your credentials
   headers = {
           'Content-Type': 'application/json',
           'Authorization': 'Bearer YOUR_GPT_ACCESS_TOKEN'
       }

   # Enter parameters that will affect the response from the API.
   my_params = {
       "start_date": "2023-10-01", "location": "New York, NY", "units": "metric",
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
   set_authentication_credentials
   set_parameters
   make_get_request
   show_result_if_successful

.. plandisplay:: plans.jsonset_target_url_code
   :plan: Set Target URL

.. plandisplay:: plans.jsonset_authentication_credentials_code
   :plan: Set Authentication Credentials

.. plandisplay:: plans.jsonset_parameters_code
   :plan: Set Parameters

.. plandisplay:: plans.jsonmake_get_request_code
   :plan: Make GET Request

.. plandisplay:: plans.jsonshow_result_if_successful_code
   :plan: Show Result If Successful


