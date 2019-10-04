'''
Lab 3: Grading
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Concepts Covered
input, print
type conversion (str to int)
comparisons (< <= > >=)
if, elif, else
Instructions
Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''
#variables
letter = ""

print("Welcome to Grading app!\n")
grade = int(input("Enter a grade from 1 to 100: "))
if 90 <= grade <= 100:
    letter = "A"
elif 80 <= grade < 90:
    letter = "B"
elif 70 <= grade < 80:
    letter = "C"
elif 60 <= grade < 70:
    letter = "D"
elif 0 <= grade <60:
    letter = "F"
else:
    print("That number is out of range. Try again!")

print(f"Your grade is {letter}.")
