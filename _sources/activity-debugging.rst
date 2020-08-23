..  shortname:: Debugging
..  description:: Debugging activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: debugging-

Code debugging activity
:::::::::::::::::::::::::

Every week, a new cat or dog is the Ann Arbor’s 107one Pet-of-the-Week. The code below is supposed to *get the pet of the week webpage*, *scrape the text of the title shown in the picture*, and *print it*.

.. image:: _static/pet_of_the_week.png
    :scale: 70%
    :align: center
    :alt: The pet of the week from August 22, 2020 is Chester.

However, it doesn't work! Instead of printing the title text, it prints nothing.

Can you fix it? Here is the buggy code:

.. raw:: html

   <pre><strong>#Get the webpage</strong>
   <a href="/plan2.html"><pre style="background-color:#FCF3CF;">
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from <mark>a URL</mark> 
   url = <mark style="border:2px; border-style:solid; border-color:#1A5276; "background-color:#FCF3CF;">'https://www.hshv.org/petsoftheweek/'</mark>
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser')</pre></a></pre>

   <pre><strong># Get info from one tag</strong>
   <a href="/plan2.html"><pre style="background-color:#FCF3CF;">
   # Get first tag of <mark>a certain type</mark> from the soup
   tag = soup.find(<mark style="border:2px; border-style:solid; border-color:#1A5276; "background-color:#FCF3CF;">'a', class_='pt-cv-none cvplbd'</mark>)
   # Get <mark>link</mark> from tag
   info = tag.<mark style="border:2px; border-style:solid; border-color:#1A5276">get('href')</mark></pre></a></pre>

   <pre><strong>#Do something with the info</strong>
   <a href="/plan9.html"><pre style="background-color:#D6EAF8;">
   # Print <mark style="background-color:#ABEBC6">the info</mark>
   print(<mark style="border:2px; border-style:solid; border-color:#1A5276; background-color:#ABEBC6">info</mark>)</pre></a></pre>

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
        # Get link from tag
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
    
    :ref:`plan_2`

    :ref:`plan_3`

    :ref:`plan_4`

    :ref:`plan_5`

    :ref:`plan_9`

