..  shortname:: Writing
..  description:: Writing activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: writing1-


Code writing activity part 1
:::::::::::::::::::::::::::::

On this page, you will complete an activity to write code that:

**Scrapes all the comments on the Rate My Professor page for Prof. Ericson and Prof. Oney**

Here is `the link to Prof. Ericson's Rate My Professor page <https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2454833>`_.
Here is `the link to Prof. Oney's Rate My Professor page <https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2239751>`_. 

You can see that both the pages have the same layout.

.. image:: _static/rate_my_prof_ericson.png
    :scale: 50%
    :align: center
    :alt: Prof. Ericson's Rate My Professor page

.. image:: _static/rate_my_prof_oney.png
    :scale: 50%
    :align: center
    :alt: Prof. Ericson's Rate My Professor page

The comments all have the same tag name. Here's what it looks like when you inspect Prof. Ericson's page:

.. image:: _static/rate_my_prof_tags.png
    :scale: 65%
    :align: center
    :alt: Inspecting the tags on the Rate My Professor page

The ``'div'`` tag with ``class='Comments__StyledComments-dzzyvm-0 dvnRbr'`` is not used anywhere else on the page besides for students' comments.


.. sidebar:: Links to plans
   
    :ref:`plan_2`

    :ref:`plan_3`

    :ref:`plan_4`

    :ref:`plan_5`

    :ref:`plan_9`



.. parsonsprob:: write_code_order_plans_goals
   
   Choose which of the following plans you will use, and put them in the correct order.
   
   -----
   Plan #3: Get a soup from multiple webpages
   =====
   Plan #2: Get a soup from a webpage#paired
   =====
   Plan #5: Get info from all tags of a certain type
   =====
   Plan #4: Get info from a single tag#paired
   =====
   Plan #6: Get info from all tags of a certain type, within another tag#paired
   =====
   Plan #9: Print info
   =====
   Plan #10: Store info in a json file#paired

.. reveal:: write_code_cl_reveal_1
        :showtitle: After you've done the activity, click here.
        :hidetitle: Hide question.

        .. poll:: write_code_cl_1
           :option_1: Very, very low mental effort
           :option_2: Very low mental effort
           :option_3: Low mental effort
           :option_4: Rather low mental effort
           :option_5: Neither low nor high mental effort
           :option_6: Rather high mental effort
           :option_7: High mental effort
           :option_8: Very high mental effort
           :option_9: Very, very high mental effort
           :results: instructor
           
           In solving the preceding problem I invested:



