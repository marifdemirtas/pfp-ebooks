..  shortname:: set_private_content

..  description:: If you are calling an API on your data, send the data in the body of your message.


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan 6: Set Private Content
=============================

.. plandisplay:: plans.jsonset_private_content_code
   :plan: Set Private Content

This is a plan to send sensitive content to an API. Instead of sending it as a parameter, which is visible in the URL, you send it in the body of the request. 

Plan 6 - When to use this plan?
--------------------------------
This plan is used when you want to send sensitive information to an API. For example, if you are sending a message to a chatbot or a private message to a friend, you would use this plan. If you submit a form on a website, you would also use this plan.

Plan 6 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, provide the content you want to send in the body of the request. In our examples, we send the data as 'message', but this tag can change depending on the API you are using.

Plan 6 - Exercises
--------------------
.. mchoice:: set_private_content_q1
   :answer_a: True
   :feedback_a: Correct!
   :answer_b: False
   :feedback_b: No, you would use this plan as it prevents the message from being visible in the URL.
   :correct: a

   To send a message to a chatbot using a POST request, you would use the 'Set Private Content' plan that holds the message in the body of the request.


.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    