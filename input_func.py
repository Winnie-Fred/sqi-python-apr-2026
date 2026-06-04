# input("What is your name?: ")
# print(input("What is your name?: "))
# name = input("What is your name?: ")

# print(f"Hello {name}")


# name = input("What is your name?: ")

# print(f"Hello {name}")

# favorite_num = (input("Enter your favorite number: "))
# is_even = int(favorite_num) % 2 == 0
# print(f"It is {is_even} that {favorite_num} is even")


# Ask the user for their birth year, and tell them how old they are

# import datetime

# current_year = datetime.datetime.now().year

# from datetime import datetime

# current_year = datetime.now().year

# birth_year = input("Enter your birth year: ")
# age = current_year - int(birth_year)
# print(f"You are {age} years old")


# import getpass

# password = getpass.getpass("Enter your password: ")

# from getpass import getpass

# password = getpass("Enter your password: ")

# print(f"Your password is {password}")


# plural_noun_1 = input("Enter a plural noun: ")
# person_in_room_last_name_1 = input("Enter the last name of someone in the room: ")
# adjective_1 = input("Enter an adjective: ")
# noun_1 = input("Enter a noun: ")
# noun_2 = input("Enter another noun: ")
# part_of_the_body_1 = input("Enter a part of the body: ")
# part_of_the_body_2 = input("Enter another part of the body: ")
# plural_noun_2 = input("Enter a plural noun: ")
# noun_3 = input("Enter a noun: ")
# noun_4 = input("Enter another noun: ")
# exclamation = input("Enter an exclamation: ")
# noun_5 = input("Enter a noun: ")
# noun_6 = input("Enter another noun: ")
# noun_7 = input("Enter another noun: ")
# verb_1 = input("Enter a verb: ")
# noun_8 = input("Enter a noun: ")
# adjective_2 = input("Enter an adjective: ")
# noun_9 = input("Enter a noun: ")




# story = f"""
# A one-act play to be performed by two {plural_noun_1} in this room.
# PATIENT: Thank so very much for seeing me, Doctor {person_in_room_last_name_1}, on such {adjective_1} notice.
# DENTIST: What is your problem, young {noun_1}?
# PATIENT: I have a pain in my upper {noun_2}, which is giving me a severe {part_of_the_body_1} ache.
# DENTIST: Let me take a look. Open your {part_of_the_body_2} wide. Good, now I am going to tap your {plural_noun_2} with my {noun_3}.
# PATIENT: Shouldn't you give me a/an {noun_4} killer?
# DENTIST: It's not necessary yet. {exclamation}!. I think I see a/an {noun_5} in your upper {noun_6}.
# PATIENT: Are you going to pull my {noun_7} out?
# DENTIST: No, I am going to {verb_1} your tooth and put in a temporary {noun_8}
# PATIENT: When do I come back for the {adjective_2} filling?
# DENTIST: A day after I cash your {noun_9}.
# """

# print(story)



# 1. Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".

# name = input("Enter your name: ").strip()
# print(f"Hello, {name}!")

# 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.



# 3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.


# 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.


# text = input("Enter some text: ")

# is_palindrome = text.lower() == text[::-1].lower()

# print(f"It is {is_palindrome} that {text} is a palindrome.")


# text = input("Enter some text: ")
# lower_text = text.lower()

# is_palindrome = lower_text == lower_text[::-1]

# print(f"It is {is_palindrome} that {text} is a palindrome.")




# text = input("Enter some text: ")

# is_palindrome = text.lower().replace(" ", "") == text[::-1].lower().replace(" ", "")

# print(f"It is {is_palindrome} that {text} is a palindrome.")

# 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

# print(len("Deborah"))
# print(len(["Deborah", "Benjamin", "Tanwa", "Taiwo", "Abdulateef"]))
# print(len(["Deborah", "Benjamin", "Tanwa", "Taiwo", "Abdulateef"][-1]))

# password = input("Enter your password: ")
# is_valid = 8 <= len(password) <= 30
# is_valid = 8 <= len(password) and len(password) <= 30
# is_valid = len(password) >= 8 and len(password) <= 30



# 6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your weight in kg: "))

# bmi = round(weight / (height ** 2), 2)

# print(f"Your BMI is {bmi}")