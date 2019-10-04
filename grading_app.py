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

Version 2
Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.

Version 3
Extract the logic used to determine the grade and its qualifier ('+', '-', or ' ') into functions. Additionally, use a while loop to repeatedly ask the user if they'd like to compute another grade after each computation.
'''
#functions
def sign_func(grade):
    if grade < 60:
        return ""
    remainder = grade % 10
    if 0 <= remainder < 5 and grade != 100:
        sign = "-"
    elif 5 < remainder or grade == 100 :
        sign = "+"
    else:
        sign = ""
    return sign

#variables
letter = ""
sign = ""
compute_again = True

print("Welcome to Grading app!\n")

while compute_again is True:
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
    sign = sign_func(grade)
    print(f"Your grade is {letter+sign}.")

    response_play_again = input("\nDo you like to calculate another grade (yes/no)? ").lower()
    if response_play_again in ["yes", "y"]:
        compute_again = True
    else:
        compute_again = False

print("\n***Thank you for using this app!***")
