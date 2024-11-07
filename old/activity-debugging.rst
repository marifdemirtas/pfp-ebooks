..  shortname:: Debugging
..  description:: Debugging activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: debugging-

Code debugging activity
:::::::::::::::::::::::::

Every week, a new cat or dog is |pet_of_the_week|. The code below is supposed to **get the pet of the week webpage, scrape the text of the title shown in the picture, and print it**.

.. |pet_of_the_week| raw:: html

        <a href="https://www.hshv.org/petsoftheweek/" target="_blank">the Ann Arbor’s 107one Pet-of-the-Week</a>


.. image:: _static/pet_of_the_week.png
    :scale: 70%
    :align: center
    :alt: The pet of the week from August 22, 2020 is Chester.

However, it doesn't work! Instead of printing the title text, it prints nothing.

Can you fix it? Here is the buggy code:

.. raw:: html

   <pre>Plan 1: Get a soup from a URL
   <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan2.html"><pre style="background-color:#FCF3CF;">
   <strong># Load libraries for web scraping</strong>
   from bs4 import BeautifulSoup
   import requests
   <strong># Get a soup from <mark>a URL</mark></strong> 
   url = <mark style="border:2px; border-style:solid; border-color:#1A5276; "background-color:#FCF3CF;">'https://www.humanesociety.org/petsoftheweek/'</mark>
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser')</pre></a></pre>

   <pre>Plan 4: Get info from a single tag
   <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan4.html"><pre style="background-color:#A9DFBF;">
   <strong># Get first tag of <mark>a certain type</mark> from the soup</strong>
   tag = soup.find(<mark style="border:2px; border-style:solid; border-color:#1A5276; "background-color:#FCF3CF;">'a', class_='pt-cv-none cvplbd'</mark>)
   <strong># Get <mark>info</mark> from tag</strong>
   info = tag.<mark style="border:2px; border-style:solid; border-color:#1A5276">get('href')</mark></pre></a></pre>

   <pre>Plan 5: Print the info
   <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan9.html"><pre style="background-color:#D6EAF8;">
   <strong># Print <mark>the info</mark></strong>
   print(<mark style="border:2px; border-style:solid; border-color:#1A5276">info</mark>)</pre></a></pre>

Try to fix the buggy code below. Run the code to save your progress.

.. activecode:: debug_code_1
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from a URL 
        url = 'https://www.hshv.org/petsoftheweek/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Get info from one tag
        # Get first tag of a certain type from the soup
        tag = soup.find('a', class_='pt-cv-none cvplbd')
        # Get info from tag
        info = tag.get('href')

        #Do something with the info
        # Print the info
        print(info)

.. reveal:: debug_code_cl_reveal_1
        :showtitle: After you've done the activity, click here.
        :hidetitle: Hide question.

        .. poll:: debug_code_cl_1
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

.. sidebar:: Links to plans

    |plan_2|

    |plan_3|

    |plan_5|

    |plan_4|

    |plan_9|

    .. |plan_2| raw:: html

        <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan2.html" target="_blank">Plan 1: Get a soup from a URL</a>

    .. |plan_3| raw:: html

        <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan3.html" target="_blank">Plan 2: Get a soup from multiple URLs</a> 

    .. |plan_5| raw:: html

        <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan5.html" target="_blank">Plan 3: Get info from all tags of a certain type</a> 

    .. |plan_4| raw:: html

        <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan4.html" target="_blank">Plan 4: Get info from a single tag</a>
   
    .. |plan_9| raw:: html

        <a href="https://runestone.academy/runestone/books/published/PurposeFirstWebScraping/plan9.html" target="_blank">Plan 5: Print info</a> 


