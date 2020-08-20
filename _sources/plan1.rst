..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Plan1
..  description:: Worked examples plus practice for Plan 1.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p1-
   

.. _plan_1:

Plan 1: Scrape webpage(s)
#####################################


Plan 1: Example
====================================

Let's say that you want to make a list of all the Cottage Inn Pizza locations. When you go to their website, it turns out that there are a *lot* of locations. 

.. image:: _static/cottageinn_scroll.gif
    :scale: 70%
    :align: center
    :alt: Scrolling around the Cottage Inn locations page to see that there are a lot of locations

If only you could write a little Python to easily collect them all... 

It turns out that you can! Run the code below to see what it collects.

.. activecode:: cottage_inn_example
   :language: python3
   :nocodelens:

   #Get the webpage
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from a URL 
   url = 'https://web.archive.org/web/20200427175705/https://cottageinn.com/pick-a-location/'
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser')

   #Extract info from the page
   # Get all tags of a certain type from the soup
   tags = soup.find_all('h3')
   # Collect info from the tags
   collect_info = []
   for tag in tags:
       # Get text from tag
       info = tag.text
       collect_info.append(info)

   #Do something with the info
   # Print the info
   print(collect_info)

This code probably seems a bit complicated. In this ebook, we will break down web scraping into a few common "plans". Here is the first one:

Plan 1: Outline
====================================

.. image:: _static/plan1outline.png
    :scale: 90%
    :align: center
    :alt: Plan 1 outline

Plan 1: Exercises
====================================

.. clickablearea:: plan1_click
    :question: Which parts of the example are a part of Plan 1's Slot 2? Click on those parts of the code.
    :iscode:
    :feedback: Check out the plan outline above to identify the slot.

    :click-incorrect:#Get the webpage:endclick:
    :click-incorrect:# Load libraries for web scraping:endclick:
    :click-incorrect:from bs4 import BeautifulSoup:endclick:
    :click-incorrect:import requests:endclick:
    :click-incorrect:# Get a soup from a URL:endclick:
    :click-incorrect:url = 'https://cottageinn.com/pick-a-location/':endclick:
    :click-incorrect:r = requests.get(url):endclick:
    :click-incorrect:soup = BeautifulSoup(r.content, 'html.parser'):endclick:

    :click-incorrect:#Extract info from the page:endclick:
    :click-correct:# Get all tags of a certain type from the soup:endclick:
    :click-correct:tags = soup.find_all('h3'):endclick:
    :click-correct:# Collect info from the tags:endclick:
    :click-correct:collect_info = []:endclick:
    :click-correct:for tag in tags::endclick:
        :click-correct:# Get text from tag:endclick:
        :click-correct:info = tag.text:endclick:
        :click-correct:collect_info.append(info):endclick:

    :click-incorrect:#Do something with the info:endclick:
    :click-incorrect:# Print the info:endclick:
    :click-incorrect:print(collect_info):endclick:


.. parsonsprob:: plan1_order

   Choose the subgoals that achieve Plan 1's goal, **Scrape a webpage**, and put them in the right order.
   -----
   # Get the webpage
   =====
   # Extract info from the page 
   =====
   # Do something with the info
   =====
   # Soup the tags#distractor
   =====
   # Copy the info#distractor



