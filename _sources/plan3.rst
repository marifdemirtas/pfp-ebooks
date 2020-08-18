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


Plan 3: Example
====================================

Maybe we want to get information from the UMSI course  wikipedia page.

The first step in web scraping is getting information from a webpage.

Here is the code for preparing to get information from the University of Michigan wikipedia page. 

.. activecode:: umich_plan3
   :language: python
   :nocodelens:

   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests

   # Get a soup from multiple URLs 
   base_url = ________________________________________________
   endings = ________________________________________________
   for ending in endings:
       url = base_url + ending 
       r = requests.get(url) 
       soup = BeautifulSoup(r.content, 'html.parser')

In this code, we get a **soup** from the **University of Michigan wikipedia page**. A soup is something that we can get information from using BeautifulSoup.

Plan 3: Outline
====================================

.. image:: _static/plan3outline.png
    :scale: 100%
    :align: center
    :alt: Plan 3 outline


What are URL endings?
====================================

A URL is a web address, like you see in your web browser. It should be complete (starting with http:// or https://). 

In this plan, a URL should be surrounded by quotes (:code:`''`).

MC about endings

https://www.si.umich.edu/programs/courses?title=&page=0
https://www.si.umich.edu/programs/courses?title=&page=1
https://www.si.umich.edu/programs/courses?title=&page=2
https://www.si.umich.edu/programs/courses?title=&page=3

What is the base_url?

What is the endings?

.. fillintheblank:: url_endings_fill

   If these are the URLs you want to scrape, what should the base_url and the 
   ``https://www.si.umich.edu/programs/courses?title=&page=0``
   ``https://www.si.umich.edu/programs/courses?title=&page=1``
   ``https://www.si.umich.edu/programs/courses?title=&page=2``
   ``https://www.si.umich.edu/programs/courses?title=&page=4``



   ``# Load libraries for web scraping``

   ``from bs4 import BeautifulSoup``

   ``import requests``

   ``# Get a soup from a URL`` 

   ``url =`` |blank|

   ``r = requests.get(url)``

   ``soup = BeautifulSoup(r.content, 'html.parser')``


   -    :'https://cottageinn.com': Correct.  
        :https://cottageinn.com: Remember that URLs in this plan should have quotes around them.
        :.*: Use 5 in the second blank



Plan 3: Exercises
====================================

What parts of this plan are changeable?

.. clickablearea:: umich_plan3_click
    :question: If you wanted to get a soup from a few different wikipedia pages, which part(s) of the code below would you change?
    :iscode:
    :feedback: Check out the plan outline above to identify the slot.

    # Load libraries for web scraping
    :click-incorrect:from bs4 import BeautifulSoup:endclick:
    :click-incorrect:import requests:endclick:

    # Get a soup from multiple URLs 
    :click-incorrect:url =:endclick: :click-correct:'https://en.wikipedia.org/wiki/University_of_Michigan':endclick:
    :click-incorrect:r = requests.get(url):endclick:
    :click-incorrect:soup = BeautifulSoup(r.content)::endclick:

.. fillintheblank:: plan3_fill

   Fill in the plan in order to get a soup from the University of Michigan wikipedia page.

   ``# Load libraries for web scraping``

   ``from bs4 import BeautifulSoup``

   ``import requests``

   ``# Get a soup from a URL`` 

   ``url =`` |blank|

   ``r = requests.get(url)``

   ``soup = BeautifulSoup(r.content, 'html.parser')``


   -    :'https://cottageinn.com': Correct.  
        :https://cottageinn.com: Remember that URLs in this plan should have quotes around them.
        :.*: Use 5 in the second blank


.. parsonsprob:: plan3_subgoal_order

   Choose the subgoals that achieve **Get a soup from a webpage**, and put them in the right order.
   -----
   # Load libraries for web scraping
   =====
   # Get a soup from multiple URLs 
   =====
   # Get a soup from a URL#distractor
   =====
   # Get a tag from a soup#distractor


