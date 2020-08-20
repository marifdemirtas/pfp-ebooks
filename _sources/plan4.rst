..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan4
..  description:: Worked examples plus practice for Plan 4.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p4-

.. _plan_4:

Plan 4: Get info from a single tag
#####################################


Plan 4: Example
====================================

.. activecode:: plan4_example
   :language: python3
   :nocodelens:

   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from a URL 
   url = 'https://mgoblue.com/sports/football/roster'
   r = requests.get(url)
   soup = BeautifulSoup(r.content)

   # Get all tags of a certain type from the soup
   first_tag = soup.find('div', class_='sidearm-roster-players-container')
   tags = first_tag.find_all('span', class_='sidearm-roster-player-hometown')
   # Collect info from the tags
   collect_info = []
   for tag in tags:
       # Get text from tag
       info = tag.text
       collect_info.append(info)


   # Do something with info
   # Print the info
   print(collect_info)

Which tag should I choose?
====================================


Plan 4: Outline
====================================

.. image:: _static/plan4outline.png
    :scale: 90%
    :align: center
    :alt: Plan 4 outline



Plan 4: Exercises
====================================


