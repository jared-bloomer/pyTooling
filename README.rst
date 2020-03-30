.. image:: https://www.codefactor.io/repository/github/jared-bloomer/pytooling/badge
   :target: https://www.codefactor.io/repository/github/jared-bloomer/pytooling
   :alt: CodeFactor

=========
pyTooling
=========

*********************
What am I looking at?
*********************
This is a github repository of various python tooling scripts to aim in better more standardized python development

***********************************
Why should I care or use this repo?
***********************************
These scripts are designed to help automate and aid in the development of proper Python scripts using a uniform standardized set of structure and best practices.

******************
How do I use this?
******************
The best thing is to find a script that meets your needs and just run it. Each script is a stand alone tool that does not require any other script to be executed. Many of the scripts are small and focus on 1 specific thing. For example, you are starting with a blank slater script. Allyou have in your ``.py`` file is ::

     #!/usr/bin/env python3
     # -*- coding: utf-8 -*-

Next you want to generate script metadata to add before you begin your actual code development. Well there is a script for that in this repo. just run ``generate_script_headers.py`` and
it will run you through a series of prompts and provide you the correct metadata headers to add to your codes so you end up with something like this ::

  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-

  __date__ = "2020-03-30"
  __author__ = "Jared Bloomer"
  __authors__ = "None"
  __copyright__ = "copyright 2020, Jared Bloomer. All rights reserved"
  __credits__ = ["None"]
  __contact__ = "Jared Bloomer"
  __license__ = "New BSD"
  __license_url__ = "https://opensource.org/licenses/BSD-3-Clause"
  __version__ = "0.0.1"
  __maintainer__ = "Jared Bloomer"
  __email__ = "jared@tuxknolwedge.com"
  __website__ = "http://www.jaredbloomer.com"
  __status__ = "Production"
  __deprecated__ = "False"
  __description__ = """ """

From here you can begin to structure you code and develop your ``TODO`` list. This wipes out the time to remember and manually type out all of this and provides basic metadata information in the header of your script.