# with -> context manager

# with open("index.html", "r") as f:
#     contents = f.read()

# print(contents)


# with open("lists.py", "r") as f:
#     contents = f.read()


# print(contents)


# with open("index.html", "r") as f:
#     lines = f.readlines()

# print(lines)


# # Write to a file, create it if it does not exist, replaces what is there with the new content if it already exists.
# with open("about-me.txt", "w") as f:
#     f.write("""This is some info about me.
# My name is Winnie.
# I teach Python at SQI.
# I love to eat, read and sleep.    
# """)


# with open("about-me.txt", "a") as f:
#     f.write("This is a newly added line.\n")





# f = open("my_file.txt")

# f.read()

# f.close()




# Line 1: This is a story about a boy.
# Line 2: He went to London to see the queen.
# Line 3: He loves to sing.

# with open("example.txt", "r") as f:
#     lines = f.readlines()


# for i, line in enumerate(lines, start=1):
#     print(f"Line {i}: {line}")


# PSL = Python Standard Library

# from datetime import datetime

# fourteenth_feb = datetime(2026, 2, 14, 14, 30)
# current_date = datetime.now()
# print(current_date)
# print(fourteenth_feb)

# days_since_fourteenth_feb = current_date - fourteenth_feb
# print(days_since_fourteenth_feb)


# import datetime

# import re

# import json



# four_days = datetime.timedelta(days=4)

# print(four_days)

# four_days_from_today = current_date + four_days
# print(four_days_from_today)


# 2026/05/30 12:53

# strptime -> str parse time
# strftime -> str format time

# print(four_days_from_today.strftime("%Y/%m/%d, %H:%M"))
# four_days_from_today_str = four_days_from_today.strftime("%d-%m-%Y, %H:%M")
# print(four_days_from_today_str)


# # Sep 15, 2026

# sept_15_2025 = datetime.datetime.strptime("Sep 15, 2026", "%b %d, %Y")

# print(sept_15_2025)
# print(type(sept_15_2025))


# 9 March
# 12 January

# import datetime

# birth_date = input("Enter your birth date in the form (9 March): ").strip()
# current_date = datetime.datetime.now()
# current_year = current_date.year

# birth_date += " " + str(current_year)

# print(birth_date)

# birth_date = datetime.datetime.strptime(birth_date, "%d %B %Y").date()

# print(birth_date)

# current_date = current_date.date()

# if current_date > birth_date:
#     print("Belated happy birthday")
# elif current_date < birth_date:
#     print("Your birthday is coming....")
# else:
#     print("Happy birthday to youuu 🎉🥳")



# import math


# print(math.sqrt(25))

# print(math.log10(1000))

# angle = 60

# angle_in_radians = math.radians(angle)

# print(angle_in_radians)

# print(math.cos(angle_in_radians))

# print(math.pi)



# PyPI - Python Package Index


# Virtual environment

# requirements.txt

# pip - package manager
# pip installs python - recursive acronym
# apk (linux), npm (js), chocaletey, homebrew


# 1. Create a folder for the project with `mkdir`
# 2. Enter the folder with `cd`
# 3. Create a virtual environment:
# a. Mac/Linux - python3 -m venv .venv
# b. Windows - python -m venv .venv
# 4. Activate the virtual environment:
# a. Mac/Linux - source .venv/bin/activate
# b. Windows - .venv\Scripts\activate
# 5. pip install requests bs4
# 6. Run the code e..g python scraper.py
# 7. Deactivate with `deactivate`


# import string


# pip - package manager for python

# PyPI - Python Package Index


