# Mr. Jones
# This is a sample Python script Based on CH.6 material
# ASCII text generated with http://www.network-science.de/ascii/
# Donte Jones jones_donte@dublinschools.net
# IT Academy @ Emerald Campus
#
# Notes PYCHARM users: Use 'CTRL+/' keys to uncomment or comment any selected lines of code




import random
import jones


"""
8888888888                         888    d8b                            
888                                888    Y8P                            
888                                888                                   
8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b  
888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K      
888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b. 
888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88 
888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P' 
                                                     

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
       d8888 888               888                              888    d8b                   
      d88888 888               888                              888    Y8P                   
     d88P888 888               888                              888                          
    d88P 888 88888b.  .d8888b  888888 888d888  8888b.   .d8888b 888888 888  .d88b.  88888b.  
   d88P  888 888 "88b 88K      888    888P"       "88b d88P"    888    888 d88""88b 888 "88b 
  d88P   888 888  888 "Y8888b. 888    888     .d888888 888      888    888 888  888 888  888 
 d8888888888 888 d88P      X88 Y88b.  888     888  888 Y88b.    Y88b.  888 Y88..88P 888  888 
d88P     888 88888P"   88888P'  "Y888 888     "Y888888  "Y8888P  "Y888 888  "Y88P"  888  888 

By using and creating functions you are practicing one of the concepts 
of OOP or Object Oriented Programming 
You are practicing what is known as Abstraction

Abstraction is not needing to know the details of creation but only needing to 
know how to use it
"""

# function that reports the current time
# How does it actually work? We don't necessarily need to know through 'Abstraction'
# We just need to know how to use it

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
8888888b.           888                              
888   Y88b          888                              
888    888          888                              
888   d88P  .d88b.  888888 888  888 888d888 88888b.  
8888888P"  d8P  Y8b 888    888  888 888P"   888 "88b 
888 T88b   88888888 888    888  888 888     888  888 
888  T88b  Y8b.     Y88b.  Y88b 888 888     888  888 
888   T88b  "Y8888   "Y888  "Y88888 888     888  888 

Receiving and Returning Values

Our functions provide ways to communicate with the rest of our code
This is done through receiving values through 'Parameters' 
We can return information to the caller of the method through a 'Return' value
"""
#
# # Receive and Return
# # Demonstrates parameters and return values
#
#
# def display(message): # Our function takes one argument in the parameter defined as message
#     print(message) # Data entered here will be accessible within the body of the function
#
#
# def give_me_five(): # Function takes no arguments
#     five = 5
#     return five     # Returns the value of 'five' which is the integer '5'
#
#
# def ask_yes_no(question):   # Takes 1 argument
#     """Ask a yes or no question."""
#     response = None     # No value set
#     while response not in ("y", "n"):
#         response = input(question).lower() # alters the value of response to exit the loop
#     return response                        # the value of 'response' is 'Returned' to the caller
#
#
# # main
# display("Here's a message for you.\n")
#
#
# number = give_me_five()
# print("Here's what I got from give_me_five():", number)
#
# answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
# print("Thanks for entering:", answer)
#
# input("\n\nPress the enter key to exit.")



#
# # Birthday Wishes
# # Demonstrates keyword arguments and default parameter values
#
#
# # positional parameters
# def birthday1(name, age):
#     print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")
#
#
# # parameters with default values
# def birthday2(name = "Jackson", age = 1):
#     print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")
#
#
# birthday1("Jackson", 1)
# birthday1(1, "Jackson")
# birthday1(name = "Jackson", age = 1)
# birthday1(age = 1, name = "Jackson")
#
# birthday2()
# birthday2(name = "Katherine")
# birthday2(age = 12)
# birthday2(name = "Katherine", age = 12)
# birthday2("Katherine", 12)
#
# input("\n\nPress the enter key to exit.")




"""
8888888888                                                       888          888    d8b                   
888                                                              888          888    Y8P                   
888                                                              888          888                          
8888888    88888b.   .d8888b  8888b.  88888b.  .d8888b  888  888 888  8888b.  888888 888  .d88b.  88888b.  
888        888 "88b d88P"        "88b 888 "88b 88K      888  888 888     "88b 888    888 d88""88b 888 "88b 
888        888  888 888      .d888888 888  888 "Y8888b. 888  888 888 .d888888 888    888 888  888 888  888 
888        888  888 Y88b.    888  888 888 d88P      X88 Y88b 888 888 888  888 Y88b.  888 Y88..88P 888  888 
8888888888 888  888  "Y8888P "Y888888 88888P"   88888P'  "Y88888 888 "Y888888  "Y888 888  "Y88P"  888  888 
                                      888                                                                  
                                      888                                                                  
                                      888    

Understanding Visibility & Encapsulation 

By default Python does not make you specify the visibility of variables 
The first thing we must know is any variable created outside of a loop, or function is considered to be 
in the 'Global' scope this variable can be accessed and changed from anywhere

'Encapsulation' is a way of hiding the details much in the same way we hide
variables in functions from the rest of the program

No variable including parameters of a function can be accessed outside of a function

"""


# # Global Reach
# # Demonstrates global variables
#
# def read_global():
#     print("From inside the local scope of read_global(), value is:", money)
#
#
# def shadow_global():
#     money = -10
#     print("From inside the local scope of shadow_global(), value is:", money)
#
#
# def change_global():
#     global money
#     money = -10
#     print("From inside the local scope of change_global(), value is:", money)
#
#
# def change_global_and_return_it():
#     global money
#     money *= 100
#     return money
#
#
# # main
# # value is a global variable because we're in the global scope here
# money = 10
# print("In the global scope, value has been set to:", money, "\n")
#
# read_global()
# print("Back in the global scope, value is still:", money, "\n")
#
# shadow_global()
# print("Back in the global scope, value is still:", money, "\n")
#
# change_global()
# print("Back in the global scope, value has now changed to:", money)
#
#
# change_global_and_return_it()
# newMoney = change_global_and_return_it() # Catching the results returned from a function and
#                                          # storing them in a variable 'newMoney'
# print("This is the value returned by the 'change_global_and_return_it()' function: ", newMoney)
#
# input("\n\nPress the enter key to exit.")





"""
888b     d888               888          888                   
8888b   d8888               888          888                   
88888b.d88888               888          888                   
888Y88888P888  .d88b.   .d88888 888  888 888  .d88b.  .d8888b  
888 Y888P 888 d88""88b d88" 888 888  888 888 d8P  Y8b 88K      
888  Y8P  888 888  888 888  888 888  888 888 88888888 "Y8888b. 
888   "   888 Y88..88P Y88b 888 Y88b 888 888 Y8b.          X88 
888       888  "Y88P"   "Y88888  "Y88888 888  "Y8888   88888P' 


Software Reuse & Creating Modules

By creating our own functions we can reuse code across projects
We can also create our own modules to store/ organize functions we commonly use

Once a module is imported it becomes an object in our code therefore we use the 
same '.' dot notation as with any other object see example below
"""
#
# import jones # This is another python file named jones.py
#              # It has several functions defined in it I would like to use
#
# jones.hello() # Dot notation tells the interpreter where to find the 'hello()' function
#
# # Catching the returned results in the 'average' variable for use by the main application
# average = jones.getAverage2()
#
# # Main application using the results returned by the 'getAverage2()' function
# print(average)
#
# jones.countDownTimers()   # Uses default value defined in the function definition
# jones.countDownTimers(10) # Uses value passed as an argument by the user






