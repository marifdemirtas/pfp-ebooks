..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Debugging
..  description:: Debugging activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: debugging-

Code debugging activities
:::::::::::::::::::::::::

.. sidebar:: Links to plans
    
    :ref:`plan_1`
   
    :ref:`plan_2`

    :ref:`plan_3`

    :ref:`plan_4`

    :ref:`plan_5`

    :ref:`plan_6`

    :ref:`plan_7`

    :ref:`plan_8`

    :ref:`plan_9`

    :ref:`plan_10`
                
Activity 1
**********************

This code is supposed to scrape links for all the dining halls from the dining halls webpage. However, it doesn't work! Instead, it scrapes the names of all the dining halls.

Can you fix it?

Below the code is a GIF that shows the relevant tags on the dining halls webpage.

.. activecode:: debug_code_1
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from a URL 
        url = 'https://dining.umich.edu/menus-locations/dining-halls'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Extract info from the webpage
        # Get first tag of a certain type from the soup
        first_tag = soup.find('div', class_='medium-7 columns')
        # Get all tags of a certain type from the first tag
        tags = first_tag.find_all('a')
        # Collect info from the tags
        collect_info = []
        for tag in tags:
            # Get text from tag
            info = tag.text
            collect_info.append(info)

        #Do something with info
        # Print the info
        print(collect_info)


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
        

Relevant tags
**********************

.. image:: _static/dining_halls.gif
    :scale: 90%
    :align: center
    :alt: Relevant tags on the dining hall webpage


Activity 2
**********************

This code is supposed to scrape links for all the dining halls from the dining halls webpage. However, it doesn't work! Instead, it scrapes the *last* link on the page. 

Can you fix it?

.. activecode:: debug_code_2
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from a URL 
        url = 'https://dining.umich.edu/menus-locations/dining-halls'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Extract info from the webpage
        # Get first tag of a certain type from the soup
        first_tag = soup.find('div', class_='medium-7 columns')
        # Get all tags of a certain type from the first tag
        tags = first_tag.find_all('a')
        # Collect info from the tags
        collect_info = []
        for tag in tags:
            # Get link from tag
            info = tag.get('href')
            collect_info.append(info)

        #Do something with info
        # Print the info
        print(info)


.. reveal:: debug_code_cl_reveal_2
        :showtitle: After you've done the activity, click here.
        :hidetitle: Hide question.

        .. poll:: debug_code_cl_2
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

Activity 3
**********************

This code is supposed to scrape links for all the dining halls from the dining halls webpage. However, it doesn't work! Instead, it scrapes *every* link on the page. 

Can you fix it?

.. activecode:: debug_code_3
        :language: python3
        :nocodelens:

        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from a URL 
        url = 'https://dining.umich.edu/menus-locations/dining-halls'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Extract info from the webpage
        # Get first tag of a certain type from the soup
        first_tag = soup.find('div', class_='medium-7 columns')
        # Get all tags of a certain type from the first tag
        tags = soup.find_all('a')
        # Collect info from the tags
        collect_info = []
        for tag in tags:
            # Get link from tag
            info = tag.get('href')
            collect_info.append(info)

        #Do something with info
        # Print the info
        print(collect_info)


.. reveal:: debug_code_cl_reveal_3
        :showtitle: After you've done the activity, click here.
        :hidetitle: Hide question.

        .. poll:: debug_code_cl_3
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

