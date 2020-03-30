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
__website__ = "http://www.mywebsite.com"
__status__ = "Production/Development"
__deprecated__ = "True/False"
"""

"""
TODO:
    
    Get Copyright Info
    Get License Type
    Get License URL
    Get Status of project
        Production or Development
        Deprecated? 
    Get Version Number
    
"""

def getTodaysDate():
    """
    Get Todays Date
    """
    from datetime import date
    try:
        today=date.today()
        return today
    except ValueError as e:
        return Exception(f"Failed to get todays date. Failure was {e}")

def getAuthors():
    """
    Get Author Information
        Primary Author
        Additional Authors
        Additional Credits
    """
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
        if additional == ('yes' or 'Yes' or 'y' or 'Y'):
            aauthors = input("Who are the additional authors? Please list all of them on one line. ")
        else:
            aauthors = ""
            pass
    except ValueError as e:
        Errors.append = "Exception: Could not get additional authors. Error was {e}"

    try:
        acredits = input("Would you like to add additional credits? [yes|no] ")
        if acredits == ('yes' or 'Yes' or 'y' or 'Y'):
            credits = input("Who are the additional credits? Please list all of them on one line. ")
        else:
            credits = ""
    except ValueError as e:
        Errors.append = "Exception: Could not get additional credits. Error was {e}"

    if len(Errors) == 0:
        return Errors
    else:
        return (pauthor, aauthors, credits)

def getContactInfo():
    """
        Get Contact Info
            Contact
            Email
            Website
    """
    try:
        userName = input("What is your Name? ")
        if not userName:
            raise ValueError("Contact Name is required!")
    except ValueError as e:
        return Exception(f"Failed to get Contact Name. Failure was {e}")

    try:
        userEmail = input("What is your Email Address? ")
        if not userEmail:
            raise ValueError("Email Address is required!")
    except ValueError as e:
        return Exception(f"Failed to get Email Address. Failure was {e}")

    try:
        userWebsite = input("What is your Website? ")
        if not userWebsite:
            userWebsite = ""
    except ValueError as e:
        return Exception(f"Failed to get Website. Failure was {e}")

    return (userName, userEmail, userWebsite)

def getMaintainer():
    """"
    Get code Maintainer
    """
    try:
        maintainer = input("Who is the active Maintainer of this code? ")
        if not maintainer:
            raise ValueError("Maintainer is required!")
    except ValueError as e:
        return Exception(f"Failed to get Maintainer. Failure was {e}")
    return maintainer

def getCopyright():
    """
    Generate Copyright Info
    """
    from datetime import date
    year = str(date.today()).split("-")[0]

    try:
        org = input("What is the name of your company or organization? ")
        if not org:
            raise ValueError("Company or organization is required!")
    except ValueError as e:
        return Exception(f"Failed to get company or organization. Failure was {e}")
    return "copyright %s, %s. All rights reserved" % (year, org)




def main():
    date = getTodaysDate()
    (pauthor, aauthor, credits) = getAuthors()
    (userName, userEmail, userWebste) = getContactInfo()
    maintainer = getMaintainer()

##############
# MAIN LOGIC #
##############
#main()
