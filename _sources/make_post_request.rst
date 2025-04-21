..  shortname:: make_post_request

..  description:: Call the API with private data by making a POST request to the server.


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan 7: Make POST Request
===========================

.. plandisplay:: plans.jsonmake_post_request_code
   :plan: Make POST Request

This is a plan when you want to make a POST request to an API to obtain information. Sending a POST request is different than the GET request, as you may communicate with the API by sending a message body, rather than just providing parameters.

Plan 7 - When to use this plan?
--------------------------------
This plan is used when your goal is to modify information on the server side (e.g. processing the data you sent). You can use it if you want to make a request to the API where you want to share potentially sensitive information, like private messages.

Plan 7 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, provide the target url you set earlier, provide any headers that you want to share such as your authorization credentials, and provide the body of the message that contains the information you would like to share with the API.

Plan 7 - Exercises
--------------------
.. mchoice:: make_post_request_q1
   :random: 
   :answer_a: my_body
   :feedback_a: Correct!
   :answer_b: my_headers
   :feedback_b: Incorrect. 'my_headers' is used to specify the headers of the request, which might include authentication information.
   :answer_c: target_url
   :feedback_c: Incorrect. 'target_url' specifies the endpoint to which the request is being sent.
   :answer_d: requests.post
   :feedback_d: Incorrect. 'requests.post' is the method used to send the POST request, but it does not specify the request body.
   :correct: a

   In the context of sending a JSON payload to an API endpoint that requires authentication, which part of the following code template is responsible for specifying the data being sent in the request body?
   response = requests.post(target_url, headers=my_headers, json=my_body)

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    