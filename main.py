# Mr. Jones
# This is a sample Python script Based on CH.6 material
# ASCII text generated with http://www.network-science.de/ascii/
# Donte Jones jones_donte@dublinschools.net
# IT Academy @ Emerald Campus
#
# Notes PYCHARM users: Use 'CTRL+/' keys to uncomment or comment any selected lines of code




import random

"""
Functions 

Functions allow you to breakup your code into more managable chunks 
Programs that implement functions are easier to create and manage
Functions should do a specific task to keep them organized

*Functions in Python always need to be defined before they can be called! 
"""
#
# # Functions begin with a definition
# def anAmazingFunction():
#     """ This is referred to as a Docstring it is optional but can help explain the function """
#     print("This is the body of the method")
#     print("The individual tasks your function should preform go here")
#
# # The Method can be used or 'Called' by using its name followed by parenthesis
# anAmazingFunction()



"""
Abstraction

By using and creating functions you are practicing one of the concepts 
of OOP or Object Oriented Programming 
You are proacticing what is known as Abstraction

Abstraction is not needing to know the details of creation but only needing to 
know how to use it
"""

# function that reports the current time
# How does it actually work? We don't necessarily need to know through 'Abstraction'
# We just need to know how to use it

import  time

# Prints your system time
def whatTimeIsIt(): # Defines the function
    """ Displays the system time""" # Docstring, this is optional
    print(time.ctime()) # Function Body


whatTimeIsIt() # Calling the function to get a result