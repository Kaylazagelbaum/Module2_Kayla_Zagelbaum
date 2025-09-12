"""
Kayla Zagelbaum
Module 2: Homework 2A: minutes to hours and minutes
This function will convert minuutes to hours and minutes
The user will tell you how many minutes
Pseudocode:
    1. call the function minutes_to_hours_and_minutes()
    2. in function minutes_to_hours_and_minutes():
        A. Ask the user how many minutes
        B. convert minutes to integers
        C. Divide minutes by 60 and return the remainder, store this value
        D. Tell my user how many hours and minutes it is

"""
 #this names the function
def minutes_to_hours_and_minutes():   
    question = "How many minutes"    #this asks the user how many minutes
    answer = int(input(question))    #this converts the answer from a string into and integer and labels it answer
    hours = answer // 60    #this divides the answer by 60 and saves it as hours
    minutes = answer % 60    #this divides the answer by 60, provides the remainder, and saves the remainder as minutes
     #this prints the answer that the user will see
    print("That is equivalent to", hours, "hours and", minutes, "minutes") 

#this calls the function so that it will be executed
minutes_to_hours_and_minutes()    
          
