Programming Plans Tutorial
==============================

Goal of this Tutorial
------------------------------

This tutorial introduces you to common programming plans - reusable code patterns that help solve specific programming tasks. Each plan comes with examples, explanations, and interactive exercises to help you master its usage.

.. activecode:: cottage_inn_example
   :language: sql
   :nocodelens:
   :dburl: /_static/Chinook_Sqlite.sqlite

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
       # Get info from tag
       info = tag.text
       collect_info.append(info)

   #Do something with the info
   # Print the info
   print(collect_info)


.. admonition:: Learning Approach
   :class: note

   Each programming plan is presented with:
   * A clear explanation of its purpose and when to use it
   * Code examples showing how to implement it
   * Interactive exercises to practice applying the plan
   * Common variations and edge cases to consider

Integrated Examples
::::::::::::::::::::::::::::::

.. toctree::
   :maxdepth: 2

   integrated_3.rst
   integrated_2.rst
   integrated_4.rst
   integrated_1.rst
