..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


..  shortname:: Plan8
..  description:: Worked examples plus practice for Plan 8.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: p8-

.. _plan_8:

Plan 8: Get link from tag
###########################

One type of tag, the ``a`` tag, holds a link. 

Plan 8: Example
====================================

Here is the tag that creates the name of one of the Cottage Inn Pizza locations. The tag is surrounded by the blue rectangle. It is an h3 tag.

.. image:: _static/cottage_inn_h3_text.png
    :scale: 90%
    :align: center
    :alt: h3 tag example

By using the code below, we can get the **text** of the tag. The text is what is in-between the start and end tag (between the ``<h3>`` and ``</h3>``. For the image above, the text is **Ann Arbor Broadway St.**


.. activecode:: plan8_example
    :language: python3
    :nocodelens:

    info = tag.get('href')


Plan 8: Outline
====================================

.. image:: _static/plan8outline.png
    :scale: 90%
    :align: center
    :alt: Plan 8 outline



Plan 8: Exercises
====================================

.. mchoice:: get_link_mc_1
    :random:

    What is the text of the tag below?

    .. image:: _static/dining_h2_text.png
        :align: center
        :alt: h2 tag on dining page
    
    -   Today's Menu

        +   Correct! This text is between the <h2> and </h2>

    -   h2

        -   No, h2 is the tag name.

    -   menuTitle

        -   No

    -   class

        -   No, class is an attribute


.. mchoice:: get_link_mc_2
    :random:

    Which tag in the picture below has text?

    .. image:: _static/dining_span_text.png
        :align: center
        :alt: span tag on dining page

    -   h2

        -   No, there is no h2 tag in this image.

    -   span

        +   Correct! The text starts with "With its chandeliers and dramatically vaulted ceiling..."

    -   p

        -   No, this tag contains the span tag.

    -   style

        -   No, style is an attribute

