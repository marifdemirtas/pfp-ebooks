..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan2
..  description:: Worked examples plus practice for Plan 2.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p2-


Plan 2: Example
====================================

Maybe we want to get information from the University of Michigan wikipedia page.

The first step in web scraping is getting information from a webpage.

Here is the code for preparing to get information from the University of Michigan wikipedia page. 


.. activecode:: umich_plan1
   :language: python
   :nocodelens:

   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests

   # Get a soup from a URL 
   url = 'https://en.wikipedia.org/wiki/University_of_Michigan'
   r = requests.get(url)
   soup = BeautifulSoup(r.content)

In this code, we get a **soup** from the **University of Michigan wikipedia page**. A soup is something that we can get information from using BeautifulSoup.

Plan 2: Outline
====================================

.. image:: _static/plan2outline.png
    :scale: 100%
    :align: center
    :alt: Plan 2 outline


What is a URL?
====================================

A URL is a web address, like you see in your web browser. It should be complete (starting with http:// or https://). 

In this plan, a URL should be surrounded by quotes (:code:`''`).


Plan 2: Exercises
====================================

What parts of this plan are changeable?

.. clickablearea:: umich_plan2_click
    :question: If you wanted to get a soup from the MDen website, which part(s) of the code below would you change?
    :iscode:
    :feedback: Check out the plan outline above to identify the slot.

    # Load libraries for web scraping
    :click-incorrect:from bs4 import BeautifulSoup:endclick:
    :click-incorrect:import requests:endclick:

    # Get a soup from a URL 
    :click-incorrect:url =:endclick: :click-correct:'https://en.wikipedia.org/wiki/University_of_Michigan':endclick:
    :click-incorrect:r = requests.get(url):endclick:
    :click-incorrect:soup = BeautifulSoup(r.content)::endclick:

.. fillintheblank:: plan2_fill

   Fill in the plan in order to get a soup from the Cottage Inn website.

   ``# Load libraries for web scraping``

   ``from bs4 import BeautifulSoup``

   ``import requests``

   ``# Get a soup from a URL`` 

   ``url =`` |blank|

   ``r = requests.get(url)``

   ``soup = BeautifulSoup(r.content)``


   -    :'https://cottageinn.com': Correct.  
        :https://cottageinn.com: Remember that URLs in this plan should have quotes around them.
        :.*: Use 5 in the second blank

.. parsonsprob:: plan2_parsons

   Choose the subgoals that achieve **Get a soup from a webpage**, and put them in the right order.
   -----
   # Load libraries for web scraping
   =====
   # Get a soup from a URL 
   =====
   # Get a soup from the University of Michigan wikipedia page #distractor


 
