#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script should be able to generate the following data

__date__ = "Date Last Updated"
__author__ = "Primary Author of Script"
__authors__ = "Additional Authors"
__copyright__ = "Copyright 2007, Company or Organization Name"
__credits__ = ["Usually the same as Authors but can call out other people"]
__contact__ = "Contact Information"
__license__ = "GPL2/GPL3/MIT/New BSD/ISC/LGPL"
__license_url__ = "HTML Link to License"
__version__ = "1.0.1"
__maintainer__ = "firstName lastName"
__email__ = "someone@someplace.org"
__status__ = "Production/Development"
__deprecated__ = "True/False"
"""

"""
TODO:
    
    Get Authors
    Get Additional Credits
    Get Copyright Info
    Get License Type
    Get License URL
    Get Contact Info
        Contact
        Name
        Email
        Website
    Get Status of project
        Production or Development
        Deprecated? 
    Get Version Number
    
"""

def getTodaysDate():
    from datetime import date
    try:
        today=date.today()
        return today
    except ValueError as e:
        return Exception(f"Failed to get todays date. Failure was {e}")

def getAuthors():
    Errors = ""
    try:
        pauthor = input("Who is the primary author of this script? (Required) ")
        if not pauthor:
            raise ValueError("Primary Author is required!")
    except ValueError as e:
        Errors.append = "Exception: Could not get primary author. Error was {e}"
        return Errors

    try:
        additional = input("Are there any additional authors of this script? [yes|no] ")
        if additional == 'yes' or 'Yes' or 'y' or 'Y':
            aauthors = input("Who are the additional authors? Please list all of them on one line. ")
        else:
            aauthors = ""
            pass
    except ValueError as e:
        Errors.append = "Exception: Could not get additional authors. Error was {e}"

    try:
        acredits = input("Would you like to add additional credits? [yes|no] ")
        if acredits == 'yes' or 'Yes' or 'y' or 'Y':
            credits = input("Who are the additional credits? Please list all of them on one line. ")
        else:
            credits = ""
    except ValueError as e:
        Errors.append = "Exception: Could not get additional credits. Error was {e}"

    if len(Errors) == 0:
        return Errors
    else:
        return (pauthor, aauthors, credits)

print(getAuthors())