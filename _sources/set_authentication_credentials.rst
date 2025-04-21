..  shortname:: set_authentication_credentials

..  description:: If the API requires a log in or a similar authentication, share your credentials


.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-

Plan 5: Set Authentication Credentials
========================================

.. plandisplay:: plans.jsonset_authentication_credentials_code
   :plan: Set Authentication Credentials

This is a plan to authenticate yourself to an API. This is done by sharing an access token (also called API key).

Plan 5 - When to use this plan?
--------------------------------
This plan is used when you want to "log in" to an API. Since we do not have a login interface when working with APIs, we use these tokens or keys to let the API know who we are. In many cases, you might need to login to a website, pay for these access tokens, and then use them to authenticate your requests in your code.

Plan 5 - What parts can be customized to use this plan?
-------------------------------------------------------
To use this plan, provide the access token you received from the API provider. In our examples, we use 'ACCESS_CS102_GPT', but this can change depending on the API you are using.

.. note:: 
      
      .. raw:: html

       <a href="/index.html" >Click here to go back to the main page</a>
    