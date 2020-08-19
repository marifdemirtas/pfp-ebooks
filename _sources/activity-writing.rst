..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Writing
..  description:: Writing activity.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: writing-

Please complete this activity


Code writing activity
:::::::::::::::::::::::::

.. parsonsprob:: write_code_order_plans_goals
   
   The goal you are trying to achieve goes here.
   
   -----
   Plan #2: Get a soup from a webpage
   =====
   Plan #3: Get a soup from multiple webpages#paired
   =====
   Plan #4: Get info from a single tag
   =====
   Plan #5: Get info from all tags of a certain type#paired
   =====
   Plan #6: Get info from all tags of a certain type, within another tag#paired
   =====
   Plan #9: Print info
   =====
   Plan #10: Store info in a json file#paired


.. parsonsprob:: write_code_order_plans_code

   The goal you are trying to achieve goes here.
   
   -----
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from a URL 
   url = _________________________
   r = requests.get(url)
   soup = BeautifulSoup(r.content, 'html.parser')   
   =====
   # Load libraries for web scraping
   from bs4 import BeautifulSoup
   import requests
   # Get a soup from multiple URLs 
   base_url = ___________________________________
   endings =  ___________________________________
   for ending in endings:
       url = base_url + ending 
       r = requests.get(url) 
       soup = BeautifulSoup(r.content, 'html.parser')#paired
   =====
   # Get first tag of a certain type from the soup
   tag = soup.find(___________)
   # Get info from the tag
   _____________________________________________
   =====
   # Get all tags of a certain type from the soup
   tags = soup.find_all(___________)
   # Collect info from the tags
   collect_info = []
   for tag in tags:
       _______________________________________
       collect_info.append(info)#paired
   =====
   # Get first tag of a certain type from the soup
   first_tag = soup.find(___________)
   # Get all tags of a certain type from the first tag
   tags = first_tag.find_all(____________)
   # Collect info from the tags
   collect_info = []
   for tag in tags: 
       ________________________________________
       collect_info.append(info)#paired
   =====
   # Print the info
   print(____________)
   =====
   # Load library for json files
   import json
   # Put info into file
   f = open(____________, 'w')
   json.dump(____________, f)
   f.close()#paired
   

.. reveal:: write_code_fill_in_reveal
    :showtitle: After you've tried this activity, you can click here.

    .. activecode:: write_code_fill_in
       :language: python3
       :nocodelens:


        #Get the webpage

