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
To use this plan, provide the content you want to send in the body of the request. In our examples, we send the data as 'content', but this tag can change depending on the API you are using.

Plan 6 - Exercises
--------------------
.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    