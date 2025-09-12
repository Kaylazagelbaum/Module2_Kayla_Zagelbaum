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
def minutes_to_hours_and_minutes():
    question = "How many minutes"
    answer = int(input(question))
    hours = answer // 60
    minutes = answer % 60
    print("That is equivalent to", hours, "hours and", minutes, "minutes")

minutes_to_hours_and_minutes()
          
