# weather = "STORMY"

# if weather == "sunny":
#     print("Enjoy the sunshine")
# elif weather == "windy":
#     print("It is windy outside")
# elif weather == "stormy":
#     print("Remain indoors!")
# else:
#     print("Get an umbrella")


# number1 = 19
# number2 = 19

# if number1 > number2:
#     print("number1 is greater")
# elif number1 < number2:
#     print("number1 is less than number2")
# else:
#     print("number1 is equal to number2")


# is_male = True

# if is_male == True:  # ❌ not pythonic
#     print("Pronoun is 'he'")
# else:
#     print("Pronoun is 'she'")


# is_male = True

# if is_male:  # pythonic
#     print("Pronoun is 'he'")
# else:
#     print("Pronoun is 'she'")


# male = None

# if male is not None:  # pythonic
#     print("Pronoun is 'he'")
# else:
#     print("Pronoun is 'she'")




# 1. Ask the user for a number. Print 'It is even' if the number is even. otherwise, print "It is odd"

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print('It is even')
# else:
#     print("It is odd")




# 2. Ask the user for their name. Print 'It starts with 'A'' if their name starts with 'A', otherwise print 'It does not start with 'A''

# name = input("Enter your name: ").strip()
# name = input("Enter your name: ").strip()


# # if name.lower().startswith("a"):
# if name[0].lower() == "a":
#     print("It starts with 'A'")
# else:
#     print("It does not start with 'A'")



# 3. Create a integer `temperature`. If it is 0 degrees or below, print "It is freezing". If it is between 1 and 100, Print "It is hot", If it is above 100, print "It is very hot".

# temperature = int(input("Enter the temperature: "))

# if temperature <= 0:
#     print("it is freezing")
# elif 1 <= temperature <= 100:
#     print("It is hot")
# else:
#     print("it is very hot")


# Ask the user for their score
# and tell them their grade

# "A" - any grade 90-100, inclusive
# "B" - any grade 80-89, inclusive
# "C" - any grade 70-79, inclusive
# "D" - any grade 60-69, inclusive
# "F" - any grade <60


# has_umbrella = True
# has_raincoat = False

# # # If the person has either an umbrella or a raincoat, print "You are protected from the rain"
# # # If they have both an umbrella and a raincoat, "You have double protection from the rain"
# # # If they have none of the two, "You are NOT protected from the rain"


# if has_umbrella and has_raincoat:
#     print("you have double protection from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print("You are NOT protected from the rain")

# if has_umbrella:
#     print("You are protected from the rain")
# elif has_raincoat:
#     print("You are protected from the rain")
# elif has_umbrella == has_raincoat:
#     print("You have double protection from the rain")
# elif has_umbrella != has_raincoat:
#     print("You are NOT protected from the rain")
# else:
#     print("Rain will beat you")



# truthy and falsy

# name = input("What is your name? ").strip()


# if name:
#     print(f"Hello, {name}")
# else:
#     print("Your name is required.")



# if not name: 
#     print("Your name is required.")


# ternary operator
# is_male = False
# gender = "He" if is_male else "She"
# print(gender)


# age = 12
# is_male = True

# if is_male:
#     if age < 18:
#         print("You are male but cannot vote")
#     else:
#         print("You are male and can vote")
# else:
#     print("Women are not allowed to vote at any age")

# age = 12
# if age < 18:
#     pass
# print("End of file")



# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# name = "John"
# name = name.lower()



# Assignment correction Q1 - Q4

# Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.

# is_at_least_120cm = int(input("Enter height: ")) >= 120

# with_adult = input("With adult? ") == "yes"

# if is_at_least_120cm:
#     print("Allowed")
# elif with_adult:
#     print("Allowed")
# else:
#     print("Not allowed")

# Example input/output executions:
#
# Enter height: 130
# With adult? no
# Output: Allowed
#
# Enter height: 110
# With adult? yes
# Output: Allowed
#
# Enter height: 110
# With adult? no
# Output: Not allowed
#
# Enter height: 119
# With adult? yes
# Output: Allowed
#
# Enter height: 100
# With adult? no
# Output: Not allowed
#
# Enter height: 150
# With adult? no
# Output: Allowed



# Exercise 2
# An exam grading system with retake rule:
# The user enters exam score and retake status ("yes" or "no").
# - If score is at least 50, print "Pass".
# - If score is less than 50 but retake is "yes", print "Retake allowed".
# - If score is less than 50 and no retake, print "Fail".

# at_least_50 = int(input("Enter score: ")) >= 50
# retake = input("Retake? ") == "yes"

# if at_least_50:
#     print("Pass")
# elif retake:
#     print("Retake allowed")
# else:
#     print("Fail")


# Example input/output executions:
#
# Enter score: 42
# Retake? yes
# Output: Retake allowed
#
# Enter score: 42
# Retake? no
# Output: Fail
#
# Enter score: 50
# Retake? no
# Output: Pass
#
# Enter score: 75
# Retake? yes
# Output: Pass
#
# Enter score: 10
# Retake? no
# Output: Fail


# Exercise 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".


# distance = int(input("Enter distance: "))
# balance = int(input("Enter wallet balance: "))
# cost = distance * 200

# if balance >= cost:
#     print("Trip confirmed")
# elif balance >= (cost / 2):
#     print("Add funds")
# else:
#     print("Trip denied")


# Example input/output executions:
#
# Enter distance: 10
# Enter wallet balance: 800
# Output: Trip denied
# Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# 800 < 1000 (less than half), so "Trip denied".
#
# Enter distance: 10
# Enter wallet balance: 2000
# Output: Trip confirmed
# Reasoning: cost = 2000; balance = 2000.
# balance >= cost, so "Trip confirmed".
#
# Enter distance: 10
# Enter wallet balance: 1000
# Output: Add funds
# Reasoning: cost = 2000; half = 1000; balance = 1000.
# not enough (1000 < 2000) but balance >= half, so "Add funds".
#
# Enter distance: 10
# Enter wallet balance: 400
# Output: Trip denied
# Reasoning: cost = 2000; half = 1000; balance = 400.
# balance < half, so "Trip denied".
#
# Enter distance: 5
# Enter wallet balance: 500
# Output: Add funds
# Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# not enough (500 < 1000) but exactly half, so "Add funds".



# Exercise 4
# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".


# has_boarding_pass = input("Boarding pass? ") == "yes"
# has_passport = input("Passport? ") == "yes"

# if has_boarding_pass and has_passport:
#     print("Proceed to boarding")
# elif not has_boarding_pass and not has_passport:
#     print("Denied entry")
# elif has_boarding_pass:
#     print("No passport")
# else:
#     print("no boarding pass")





# Example input/output executions:
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass
#
# Boarding pass? yes
# Passport? no
# Output: No passport
#
# Boarding pass? no
# Passport? no
# Output: Denied entry
#
# Boarding pass? yes
# Passport? yes
# Output: Proceed to boarding
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass




# Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")


# Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# 9, 8, 4
# 10, 10, 6
# 5, 9, 10
# 5, 9,10
# 5,9,10
# 5,9,  10

# numbers = input("Enter three numbers separated by commas: ").split(",")
# x, y, z = numbers
# x, y, z = int(x), int(y), int(z)
# print(x)
# print(y)
# print(z)
# if x > y > z:
#     print("Decreasing order")
# elif x < y < z:
#     print("Increasing order")
# else:
#     print("Neither")



# Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.



# Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = float(input("Enter angle 1: "))
# angle2 = float(input("Enter angle 2: "))
# angle3 = float(input("Enter angle 3: "))

# if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 == 180):
#     print("valid triangle")
# else:
#     print("invalid triangle")


# You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.

# import string

# alphabets = string.ascii_lowercase



# ch = input("Enter a single alphabet character: ").lower()
# vowels = ("a", "e", "i", "o", "u")



# # if ch in vowels:
# #     print("Vowel")
# # elif ch in alphabets:
# #     print("Consonant")
# # else:
# #     print("Not an alphabet")

# if len(ch) > 1:
#     print("Not a single character")
# elif ch not in alphabets:
#     print("Not an alphabet")
# elif ch in vowels:
#     print("Vowel")
# else:
#     print("Consonant")



# Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".

# color1, color2, color3 = input("Enter 3 comma-separated colors: ").split(",")
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()

# primary_colors = ("red", "blue", "yellow")

# if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# color1, color2, color3 = input("Enter 3 comma-separated colors: ").split(",")
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
# colors = {color1, color2, color3}

# primary_colors = {"red", "blue", "yellow"}


# if colors == primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# color1, color2, color3 = input("Enter 3 comma-separated colors: ").split(",")
# color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
# colors = [color1, color2, color3]

# primary_colors = ["red", "blue", "yellow"]


# if sorted(colors) == sorted(primary_colors):
#     print("All primary colors")
# else:
#     print("Not all primary colors")



# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".


# Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# python gotcha - beginner trap

# message = input("Enter a message: ").lower()

# # if ("urgent") or ("important") or ("immediate" in message):
# if "urgent" in message or "important" in message or "immediate" in message:
#     print("High priority message")
# else:
#     print("Normal message")


# 10. You have two variables, status1 and status2, provided through user input, each of 
# which can be "active", “inactive", or "pending". Write an if statement to print 
# "Both active" if both statuses are "active", "One active" if exactly one is "active",
# and "None active" if neither is "active".
# 11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# print "Not an image file".



# 12. 	You have a variable `access_level` provided through user input which can be "admin",
# "user", or "guest". Write an if statement that prints "Full access" if access_level is
# "admin", "Limited access" if it is "user", and "No access" if it is "guest".


# 13. 	Given a string `email` collected from the user, write an if statement to check if the
# email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# print "Invalid email".

# email = input("Enter email address: ")

# if "@" in email and "." in email:
# # if "@" and "." in email:
#     print("valid email")
# else:
#     print("invalid email")



# 14. 	You have a variable `day` provided by user input which can be any day of the week 
# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# import calendar

# days_of_the_week = list(calendar.day_name)

# print(days_of_the_week)


# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# input from the user and prints the greatest number. Use conditional statements
# to determine which number is the greatest. Bonus point if you can do it without `else` 
# statements.

# 3, 8, 4

# num1, num2, num3 = input("Enter 3 numbers separated by commas: ").split(",")

# num1, num2, num3 = int(num1), int(num2), int(num3)

# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the greatest")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the greatest")
# else:
#     print(f"{num3} is the greatest")


num1, num2, num3 = input("Enter 3 numbers separated by commas: ").split(",")

num1, num2, num3 = int(num1), int(num2), int(num3)
# 6, 0, 2
# 2, 0, 6 



greatest = num1

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

print(f"{greatest} is the greatest")
