Exercise: Guess the Number!
===============================

In this exercise, you will play a game with an API: the API has a secret number, and you will try to guess it. The API will tell you if your guess is too high or too low. The number is between 1 and 50.

The endpoint for the API is: https://one02-api-fastapi.onrender.com/api/guess

This endpoint will process your guess, so you will need to POST a request to it. Your guess should be in the body of the request, not in the URL.


Try to plan your solution below.

.. parsonsprob:: exercise_1_q1

   Drag and drop the plans to send your guess using the correct request to the API and print the result.

   -----

   Set Target URL
   =====
   Set Private Content
   =====
   Make POST Request
   =====
   Show Result If Successful
   =====
   Set Authentication Credentials #distractor
   =====
   Make GET Request #distractor
   =====
   Set Parameters #distractor
   


Optional: If you want, you can write the code for these plans by copy pasting the code from the plans! Let's see if you can guess the number!

The body of your response should contain two values: a "guess" and a "netid". For example, this could be the body for guessing 25: {"guess": 25, "netid": "katcun"}.

.. activecode:: exercise_1
   :language: python3

   # Copy and paste code from the plans to send a request to the API and print the result


Here is a list of all programming plans you have learned today:

.. plandisplay:: plans.jsonset_target_url_code
   :plan: Set Target URL

.. plandisplay:: plans.jsonset_parameters_code
   :plan: Set Parameters

.. plandisplay:: plans.jsonset_authentication_credentials_code
   :plan: Set Authentication Credentials

.. plandisplay:: plans.jsonset_private_content_code
   :plan: Set Private Content

.. plandisplay:: plans.jsonmake_get_request_code
   :plan: Make GET Request

.. plandisplay:: plans.jsonmake_post_request_code
   :plan: Make POST Request

.. plandisplay:: plans.jsonshow_result_if_successful_code
   :plan: Show Result If Successful


.. highlightedtextbox::
   :title:
   :color: #f4e36e
   :highlight-color: #ffe53e
   :highlight-on-load:

   Click on the arrow on the bottom right to continue.