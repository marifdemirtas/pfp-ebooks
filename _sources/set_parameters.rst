..  shortname:: set_parameters

..  description:: Enter parameters that will affect the response from the API.


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan 2: Set Parameters
========================

.. plandisplay:: plans.jsonset_parameters_code
   :plan: Set Parameters

This plan lists the parameters that will be shared with the API you are calling.

Plan 2 - When to use this plan?
--------------------------------
This plan is used when you need to call an API with a set of parameters that do not contain private information. If you want to share private information with the API, you will need to use more secure methods that we will explore soon.

Plan 2 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, check the documentation of the API to see what type of information is required to send a request. Then, add each piece of information according to the format described. You can Google for an API's documentation to see which parameters they accept.

Plan 2 - Exercises
--------------------
.. mchoice:: set_parameters_q1
   :random: 
   :answer_a: "days": "yesterday"
   :feedback_a: Correct!
   :answer_b: "days": 5
   :feedback_b: This is a valid option for the number of days of forecast required, which must be between 1 and 14.
   :answer_c: "q": "Champaign"
   :feedback_c: This is a valid option for the query parameter, as it is a city name.
   :answer_d: "q": 61820
   :feedback_d: This is a valid option for the query parameter, as it is an US zip code.
   :correct: a

   Look at the "request parameters" for a weather API in their documentation: https://www.weatherapi.com/docs/ 
   According to the documentation, which one of the options would be an incorrect parameter to provide?

.. mchoice:: set_parameters_q2
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: By providing multiple pairs of keys and values, you can pass many parameters to the API in the same call.
   :correct: a

   You can provide multiple parameters in the same API call.

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    