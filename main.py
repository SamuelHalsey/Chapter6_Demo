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
#
# # function that reports the current time
# # How does it actually work? We don't necessarily need to know through 'Abstraction'
# # We just need to know how to use it
#
# import  time
#
# # Prints your system time
# def whatTimeIsIt(): # Defines the function
#     """ Displays the system time""" # Docstring, this is optional
#     print(time.ctime()) # Function Body
#
#
# whatTimeIsIt() # Calling the function to get a result




"""
Receiving and Returning Values with our functions

Our functions provide ways to communicate with the rest of our code
This is done through receiving values through 'Parameters' 
We can return information to the caller of the method through a 'Return' value
"""

# Receive and Return
# Demonstrates parameters and return values


def display(message): # Our function takes one argument in the parameter defined as message
    print(message) # Data entered here will be accessible within the body of the function


def give_me_five(): # Function takes no arguments
    five = 5
    return five     # Returns the value of 'five' which is the integer '5'


def ask_yes_no(question):   # Takes 1 argument
    """Ask a yes or no question."""
    response = None     # No value set
    while response not in ("y", "n"):
        response = input(question).lower() # alters the value of response to exit the loop
    return response                        # the value of 'response' is 'Returned' to the caller


# main
display("Here's a message for you.\n")


number = give_me_five()
print("Here's what I got from give_me_five():", number)

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

input("\n\nPress the enter key to exit.")
