..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Explaining
..  description:: Explaining activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: explaining-

Code explaining activity
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


Look at the code below, and try to determine what it does. 

There is a GIF below the code that shows relevant tags in the first website.

.. image:: _static/umsi_faces_code.png
    :scale: 30%
    :align: center
    :alt: Code that you are asked to explain


Relevant tags
**********************

.. image:: _static/umsi_faces.gif
    :scale: 90%
    :align: center
    :alt: UMSI faces website

.. reveal:: explain_run_code
    :showtitle: If you need a hint, click here.

     You can run the code below and see what happens.

    .. activecode:: explain_code
       :language: python3
       :nocodelens:


        #Get the webpage
        # Load libraries for web scraping
        from bs4 import BeautifulSoup
        import requests
        # Get a soup from a URL 
        url = 'https://www.si.umich.edu/people/faces-umsi'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Extract info from the webpage
        # Get the first tag of a certain type from the soup
        first_tag = soup.find('div', class_='body wysiwyg-content')
        # Get all tags of a certain type from the first tag
        tags = first_tag.find_all('a')
        # Collect info from the tags
        collect_info = []
        for tag in tags:
          # Get link from tag
          info = tag.get('href')
          collect_info.append(info)

        #Do something with info
        # Get a soup from multiple URLs 
        base_url = 'https://www.si.umich.edu/'
        endings = collect_info
        for ending in endings:
            url = base_url + ending 
            r = requests.get(url) 
            soup = BeautifulSoup(r.content, 'html.parser')

            # Get all tags of a certain type from the soup
            tags = soup.find_all('p')
            # Collect info from the tags
            collect_info = []
            for tag in tags:
                # Get text from tag
                info = tag.text
                collect_info.append(info)
            
            # Print the info
            print(collect_info)

.. reveal:: explain_code_cl_reveal_1
        :showtitle: After you've done the activity, click here.
        :hidetitle: Hide question.

        .. poll:: explain_code_cl_1
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

