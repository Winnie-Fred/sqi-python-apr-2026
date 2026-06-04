# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# DO NOT USE REGEX.


# password = "P@ssw0rd123"


# has_at_least_8_chars = len(password) >= 8
# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)
# has_digit = any(char.isdigit() for char in password)

# special_chars = "!@#$%^&*()"

# has_special_char = any(char in special_chars for char in password)
# print(has_at_least_8_chars, has_upper, has_lower, has_digit, has_special_char)
# is_strong_password = all([has_at_least_8_chars, has_upper, has_lower, has_digit, has_special_char])
# print(is_strong_password)


# def password_strength_check(password):

#     has_at_least_8_chars = len(password) >= 8

#     has_special_char = False
#     has_upper = False
#     has_lower = False
#     has_digit = False


#     special_chars = "!@#$%^&*()"

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_chars:
#             has_special_char = True
        

#     is_strong_password = has_at_least_8_chars and has_upper and has_lower and has_digit and has_special_char
#     return is_strong_password

# password1 = "p@ssW0rd123"
# password2 = "12345678"
# password3 = "Pass123!"

# print(password_strength_check(password1))
# print(password_strength_check(password2))
# print(password_strength_check(password3))


# DRY -> Don't Repeat Yourself

# def square(x):
#     return x ** 2


# print(square(12))
