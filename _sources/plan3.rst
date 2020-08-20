..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan3
..  description:: Worked examples plus practice for Plan 3.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p3-

.. _plan_3:

Plan 3: Get a soup from multiple URLs
#####################################


Plan 3: Example
====================================

Sometimes we want to get information from multiple web pages that have the same layout. For example, all of the UMSI faculty pages have the same general design.

.. image:: _static/barbara-ericson.png
    :scale: 50%
    :align: center
    :alt: Plan 3 outline

.. image:: _static/steve-oney.png
    :scale: 50%
    :align: center
    :alt: Plan 3 outline

Maybe we are interested in getting information about mutliple UMSI professors: Dr. Barb Ericson, Dr. Steve Oney, and Dr. Paul Resnick. 

Their webpages are:

``https://www.si.umich.edu/people/barbara-ericson``

``https://www.si.umich.edu/people/steve-oney``

``https://www.si.umich.edu/people/paul-resnick``

.. activecode:: plan3
   :language: python
   :nocodelens:

   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests

   # Get a soup from multiple URLs 
   base_url = 'https://www.si.umich.edu/people/'
   endings = ['barbara-ericson', 'steve-oney', 'paul-resnick']
   for ending in endings:
       url = base_url + ending 
       r = requests.get(url) 
       soup = BeautifulSoup(r.content, 'html.parser')

In this code, we get a **soup** from multiple **UMSI faculty pages**.

Plan 3: Outline
====================================

.. image:: _static/plan3outline.png
    :scale: 100%
    :align: center
    :alt: Plan 3 outline


Plan 3: Exercises
====================================


.. fillintheblank:: url_endings_fill

   If these are the URLs you want to scrape, what should the base_url and the endings be? 
   
   ``https://www.si.umich.edu/programs/courses?title=&page=0``
   ``https://www.si.umich.edu/programs/courses?title=&page=1``
   ``https://www.si.umich.edu/programs/courses?title=&page=2``
   ``https://www.si.umich.edu/programs/courses?title=&page=3``

   Fill in the code below

   ``# Load libraries for web scraping``

   ``from bs4 import BeautifulSoup``

   ``import requests``

   ``# Get a soup from multiple URLs`` 

   ``base_url =`` |blank|

   ``endings =`` |blank|

   ``for ending in endings:``

       ``url = base_url + ending``

       ``r = requests.get(url)``

       ``soup = BeautifulSoup(r.content, 'html.parser')``


   -    :'https://www.si.umich.edu/programs/courses?title=&page=': Correct.  
        :https://www.si.umich.edu/programs/courses?title=&page=: Remember that URLs in this plan should have quotes around them.
        :.*: Check out the section above for help.

   -    :['0', '1', '2', '3']: Correct.  
        :[0, 1, 2, 3]:: Remember that endings in this plan should have quotes around each ending.
        :.*: Check out the section above for help.


.. clickablearea:: umich_plan3_click
    :question: Right now this code helps you scrape three different wikipedia pages. If you also wanted to scrape the University of Minnesota's wikipedia page, which part(s) of the code below would you change? Click on the code to select your answer.
    :iscode:
    :feedback: Check out the plan outline above to identify the slot.

    # Load libraries for web scraping
    :click-incorrect:from bs4 import BeautifulSoup:endclick:
    :click-incorrect:import requests:endclick:

    # Get a soup from multiple URLs 
    :click-incorrect:base_url =:endclick: :click-incorrect:'https://en.wikipedia.org/wiki/':endclick:
    :click-incorrect:endings =:endclick: :click-correct:['University_of_Michigan', 'Ohio_State_University', 'Michigan_State_University']:endclick:
    :click-incorrect:for ending in endings::endclick:
        :click-incorrect:url = base_url + ending:endclick:
        :click-incorrect:r = requests.get(url):endclick:
        :click-incorrect:soup = BeautifulSoup(r.content, 'html.parser')::endclick:

.. parsonsprob:: plan3_subgoal_order

   Choose the subgoals that achieve **Get a soup from multiple webpages**, and put them in the right order.
   -----
   # Load libraries for web scraping
   =====
   # Get a soup from multiple URLs 
   =====
   # Get a soup from a URL#distractor
   =====
   # Get a tag from a soup#distractor


