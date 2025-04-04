Integrated Example - 3
===============================

In this example, we are demonstrating how to interact with the ChatGPT API to ask a question and get a response. The scenario involves sending a question to ChatGPT, which requires setting up a target URL for the API, providing authentication credentials, preparing the question as the content, making a POST request, and handling the response. 

To begin, you will need an access token from OpenAI to authenticate your request. Once authenticated, you can send a question to the ChatGPT API and receive a response. This example covers how to set each part of the request and handle the response to ensure you get the information you need.

Here is a simple table outlining the steps:

+--------------------------+----------------------------------------------+
| Step                     | Description                                  |
+==========================+==============================================+
| Set Target URL           | Define the API endpoint URL                  |
+--------------------------+----------------------------------------------+
| Set Authentication       | Provide necessary headers with credentials   |
+--------------------------+----------------------------------------------+
| Set Private Content      | Prepare the question as request content      |
+--------------------------+----------------------------------------------+
| Make POST Request        | Send the request with headers and content    |
+--------------------------+----------------------------------------------+
| Show Result If Successful| Process the response and display results     |
+--------------------------+----------------------------------------------+

By following these steps, you can successfully query the ChatGPT API to obtain answers to your questions.

.. activecode:: integrated_3
   :language: sql

   # Enter the URL for the API you will use.
   import requests
   target_url = 'https://api.chatgpt.com/v1/ask'
   

   # If the API requires a log in or a similar authentication, share your credentials
   headers = {
           'Content-Type': application/json,
           'Authorization': Bearer YOUR_GPT_ACCESS_TOKEN
       }

   # If you are calling an API on your data, send the data in the body of your message.
   body = {
       'content': 'my random content'
       }
   

   # Call the API with private data by making a POST request to the server.
   response = requests.post(target_url, headers=@@my_headers@@, json=@@my_body@@)
   

   # Check if response was successful, and show the data or the error message depending on the result.
   # Check the result of the request
   if response.status_code == 200:
       print(response.json())

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


