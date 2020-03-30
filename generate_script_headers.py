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
__description__ = """ 
This script should be able to generate the following data

__date__ = "Date Last Updated"
__author__ = "Primary Author of Script"
__authors__ = "Additional Authors"
__copyright__ = "Copyright 2007, Company or Organization Name"
__credits__ = ["Usually the same as Authors but can call out other people"]
__contact__ = "Contact Information"
__license__ = "GPL2/GPL3/MIT/New BSD/ISC/LGPL/other"
__license_url__ = "HTML Link to License"
__version__ = "1.0.1"
__maintainer__ = "firstName lastName"
__email__ = "someone@someplace.org"
__website__ = "http://www.mywebsite.com"
__status__ = "Production/Development"
__deprecated__ = "True/False"
__description__ = """ """
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
    try:
        pauthor = input("Who is the primary author of this script? (Required) ")
        if not pauthor:
            raise ValueError("Primary Author is required!")
    except ValueError as e:
        return Exception(f"Failed to get Primary Author. Failure was {e}")

    try:
        additional = input("Are there any additional authors of this script? [yes|no] ").lower()
        if additional == 'yes' or  additional == 'y':
            aauthors = input("Who are the additional authors? Please list all of them on one line. ")
        else:
            aauthors = "None"
    except ValueError as e:
        return Exception(f"Failed to get additional authors. Failure was {e}")

    try:
        acredits = input("Would you like to add additional credits? [yes|no] ").lower()
        if acredits == 'yes' or  acredits == 'y':
            credits = input("Who are the additional credits? Please list all of them on one line. ")
        else:
            credits = "None"
    except ValueError as e:
        return Exception(f"Failed to get additional credits. Failure was {e}")

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
            userWebsite = "None"
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

def getLicense():
    """
    Find out what License this code is Licensed Under and generate URL to License. Options are

    GPL v2
    GPL v3
    MIT
    AGPL v3
    Mozillia Public License 2.0
    Apache License 2.0
    Boost Software License 1.0
    The Unlicense
    New BSD
    ISC
    LGPL v3
    Other
    """
    try:
        from pick import pick
        title = "Please choose which License you are using: "
        options = ['GPL v2', 'GPL v3', 'MIT', 'AGPL v3', 'Mozillia Public License 2.0', 'Apache License 2.0', 'Boost Software License 1.0', 'The Unlicense', 'New BSD', 'ISC', 'LGPL v3', 'Other']
        option, index = pick(options, title)
    except Exception as e:
        return Exception(f"There was an Error. Failure was {e}")

    try:
        if option == "Other":
            license_url = input("What is the URL to the Other License? ")
            if not license_url:
                raise ValueError("License URL is required!")
        elif option == "GPL v2":
            license_url = "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html"
        elif option == "GPL v3":
            license_url = "https://www.gnu.org/licenses/gpl-3.0.html"
        elif option == "MIT":
            license_url = "https://mit-license.org/"
        elif option == "AGPL v3":
            license_url = "https://www.gnu.org/licenses/agpl-3.0.en.html"
        elif option == "Mozillia Public License 2.0":
            license_url = "https://www.mozilla.org/en-US/MPL/2.0/"
        elif option == "Apache License 2.0":
            license_url = "https://www.apache.org/licenses/LICENSE-2.0.html"
        elif option == "Boost Software License 1.0":
            license_url = "https://www.boost.org/users/license.html"
        elif option == "The Unlicense":
            license_url = "https://unlicense.org/"
        elif option == "New BSD":
            license_url = "https://opensource.org/licenses/BSD-3-Clause"
        elif option == "ISC":
            license_url = "https://www.isc.org/licenses/"
        elif option == "LGPL v3":
            license_url = "https://www.gnu.org/licenses/lgpl-3.0.en.html"

    except ValueError as e:
        return Exception(f"Failed to get License URL. Failure was {ValueError}")

    return option, license_url

def getStatus():
    """
    Get Status of project
        Production or Development
        Deprecated?
    Get Version Number
    """
    try:
        from pick import pick
        title = "What is the status of this Project? "
        statusoptions = ['Production', 'Development']
        status, index = pick(statusoptions, title)
    except Exception as e:
        return Exception(f"There was an Error. Failure was {e}")

    try:
        version = input("what is the version of this code? ")
        if not version:
            raise ValueError("Version is required!")
    except ValueError as e:
        return Exception(f"Failed to get version. Failure was {e}")

    try:
        deprecated = input("Is this project deprecated? [True|False]")
        if deprecated == ('T' or 't' or 'true' or 'True'):
            deprecated = "True"
        else:
            deprecated = "False"
        if not deprecated:
            raise ValueError("deprecated status is required!")
    except ValueError as e:
        return Exception(f"Failed to get deprecated status. Failure was {e}")

    return status, version, deprecated

def main():
    date = getTodaysDate()
    (pauthor, aauthor, credits) = getAuthors()
    (userName, userEmail, userWebsite) = getContactInfo()
    maintainer = getMaintainer()
    copy = getCopyright()
    (licenseType, licenseURL) = getLicense()
    (status, version, deprecated) = getStatus()

    print('__date__ = "%s"' % date)
    print('__author__ = "%s"' % pauthor)
    print('__authors__ = "%s"' % aauthor)
    print('__copyright__ = "%s"' % copy )
    print('__credits__ = ["%s"]' % credits )
    print('__contact__ = "%s"' % userName )
    print('__license__ = "%s"' % licenseType )
    print('__license_url__ = "%s"' % licenseURL )
    print('__version__ = "%s"' % version )
    print('__maintainer__ = "%s"' % maintainer )
    print('__email__ = "%s"' % userEmail )
    print('__website__ = "%s"' % userWebsite )
    print('__status__ = "%s"' % status )
    print('__deprecated__ = "%s"' % deprecated )
    print('__description__ = """ """')

##############
# MAIN LOGIC #
##############
main()
