'''
This is the first lab of EE363.

Purpose:
The purpose of this function is to familiarize ourselves with using Python's f-strings to format and print strings dynamically with different parameters.

Procedure:
1. Define a function that takes three parameters: name, major, and gender.
2. Use an f-string to format a sentence that includes the parameter values.
3. Call the function with example inputs and display the result using the print function.

Author: Nathnael Minuta
Student ID: 15778991
Date: 01/21/2025
'''

# Define the Introduction function
def Introduction(name, major, gender):
    return f"Hi! My name is {name}, my major is {major}, and I am a {gender}."

# Example inputs
name = "Nathnael"
major = "Electrical and Computer Engineering"
gender = "male"

# Call the function and print the result
print(Introduction(name, major, gender))
