Example 2: Talking to your own ChatGPT 
===============================

In this example, we will see how we can talk to ChatGPT using the API to ask a question and get a response. 

To achieve this, you would need to buy an **access token** from OpenAI to authenticate your request. For today, you will use a custom large language model that we are providing to you, using the following endpoint URL: https://one02-api-fastapi.onrender.com/api/chat.

The access token for this API is: ACCESS_CS102_GPT

To use the API, you will need to send your message in the body of your request, as "message". Once authenticated, you can send a question to the ChatGPT API and receive a response. This example covers how to set each part of the request and print the response.

.. activecode:: integrated_3
   :language: python3

   # Enter the URL for the API you will use.
   import requests
   target_url = 'https://one02-api-fastapi.onrender.com/api/chat'
   

   # If the API requires a log in or a similar authentication, share your credentials
   headers = {
           'Authorization': ACCESS_CS102_GPT
   } 

   # If you are calling an API on your data, send the content in the body.
   body = {
       'message': 'Hello! How are you ChatGPT?'
   }
   

   # Call the API with private data by making a POST request to the server.
   response = requests.post(target_url, headers=headers, json=body)


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
   set_authentication_credentials
   set_private_content
   make_post_request
   show_result_if_successful

.. plandisplay:: plans.jsonset_target_url_code
   :plan: Set Target URL

.. plandisplay:: plans.jsonset_authentication_credentials_code
   :plan: Set Authentication Credentials

.. plandisplay:: plans.jsonset_private_content_code
   :plan: Set Private Content

.. plandisplay:: plans.jsonmake_post_request_code
   :plan: Make POST Request

.. plandisplay:: plans.jsonshow_result_if_successful_code
   :plan: Show Result If Successful


