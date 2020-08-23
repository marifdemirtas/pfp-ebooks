..  shortname:: Writing 2
..  description:: Writing activity 2.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: writing3-


Code writing activity part 3
:::::::::::::::::::::::::::::

On this page, you will complete the final activity to write code that:

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

    
Here is the code that you assembled from the plans. You can click on each plan to go to the page where you learned about it.

.. raw:: html

        <pre>#Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from multiple URLs
        base_url = _______________________________________________________
        endings = [___________________]
        for ending in endings:
            url = base_url + ending
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            #Extract info from the page
            # Get first tag of a certain type from the soup
            tag = soup.find(______________________________________________)
            # Get link from tag
            info = tag.text  

        <pre><strong>#Do something with the info</strong>
        <a href="/plan9.html"><pre style="background-color:#D6EAF8;">
        # Print the info
        print(____________)</pre></a></pre>

Now that you've assembled the correct plans, fill in the blanks to complete the code.

.. activecode:: write_code_fill_in
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from multiple URLs
        base_url = _______________________________________________________
        endings = [_____________________]
        for ending in endings:
           url = base_url + ending
           r = requests.get(url)
           soup = BeautifulSoup(r.content, 'html.parser')

           #Extract info from the page
           # Get first tag of a certain type from the soup
           tag = soup.find(____________________________________________)
           # Get info from tag
           info = tag.______ 

           #Do something with the info
           # Print the info
           print(______)


Here's the picture of the tags again:


.. reveal:: write_code_cl_reveal_3
        :showtitle: After you've done the activity, click here.
        :hidetitle: Hide question.

        .. poll:: write_code_cl_3
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



