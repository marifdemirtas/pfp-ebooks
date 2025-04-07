..  shortname:: show_result_if_successful

..  description:: Check if response was successful, and show the data or the error message depending on the result.


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan 4: Show Result If Successful
===================================

.. plandisplay:: plans.jsonshow_result_if_successful_code
   :plan: Show Result If Successful

This is a plan to check the response from the API. The response might indicate a successful operation (code 200), or might indicate some type of error.

Plan 4 - When to use this plan?
--------------------------------
This plan is used when you want to handle cases where the request to the API may fail.

Plan 4 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, look up the HTML error codes, and replace the status code with the code you need to watch out for. Then, you can process the result by printing it directly (if there are no errors), or by showing an error message.

Plan 4 - Exercises
--------------------
.. mchoice:: show_result_if_successful_q1
   :random: 
   :answer_a: 200
   :feedback_a: Correct!
   :answer_b: 404
   :feedback_b: 404 indicates that the requested resource could not be found, so you should handle this as an error.
   :answer_c: 500
   :feedback_c: 500 indicates that there is a server error, thus the response is unsuccessful and should be treated as an error.
   :correct: a

   You are repeatedly sending requests to an API that has been not working for the past hour. You want to automatically print the data when the API is working again and your request is successfully completed. Which status code should you check for to ensure that the response was successful, allowing you to process and display the JSON data received?

.. mchoice:: show_result_if_successful_q2
   :random: 
   :answer_a: 404
   :feedback_a: Correct!
   :answer_b: 200
   :feedback_b: 200 indicates a successful response, but your response would have the "Not Found" error as the mistyped URL does not point to an existing resource.
   :answer_c: 500
   :feedback_c: 500 indicates an error due to the server, but in your case the error would be caused from requesting an address that cannot be found.
   :correct: a

   You want to send a request to "api.weather.com/forecast", but you made a typo while writing the target URL, resulting in the incorrect URL "api.weather.com/forcast", which does not exist. Which status code would you need to look for to notice this error?

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    