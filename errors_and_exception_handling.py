

# # try....except....else....finally
# try:
#     num1 = int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("num1 and num2 must be numbers")
# except Exception:
#     print("Something went wrong!")
# else:
#     print(result)
# finally:
#     print("this will always run")

# LBYL - Look Before You Leap
# EAFP - Easier to Ask for Forgiveness than Permission



# Ask the user for their age.
# If they enter a non-number, print "Age must be a number"
# If they enter a negative number, print "Age cannot be negative"
# In both of these cases, keep asking until you get a valid input
# When it is valid, print their birth year e.g. "You were born in 1990"

# from datetime import datetime

# # happy path
# while True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError as e:
#         print(f"Age must be a number: {e}")
#         # print(e)
#     else:
#         if age < 0:
#             print("Age cannot be negative")
#         else:
#             current_year = datetime.now().year

#             birth_year = current_year - age
#             print(f"You were born in {birth_year}")
#             break

class NameMustBeWinnieError(Exception):
    def __init__(self, invalid_name, *args):
        self.invalid_name = invalid_name
        super().__init__(*args)


def check_name_valid(name):
    if name != "Winnie":
        raise NameMustBeWinnieError(name, "name must be 'Winnie'")

# import logging

# try:
#     check_name_valid("John")
# except NameMustBeWinnieError as e:
#     print(f"Invalid name: {e.invalid_name}")
#     print(e)
# except:
#     print("Something went wrong")


# print("Hello")

# check_name_valid("John")

# print("End of file")

# try:
#     i = 0
#     while True:
#         print(i)
#         i += 1
# except KeyboardInterrupt:
#     print("Program terminated")