# import re

# pattern = r"\bsentence\b"
# text = "A word in a sentence?"
# match = re.search(pattern, text)
# print(match)
# if match:
#     print("Match found:", match.group())  # Match found: word
# else:
#     print("no match found")
# # Match
# # matches


# pattern = r"\d+"
# text = "There are 123345 apples and 456oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']

# import re
# pattern = r"\s+"
# text = "This   is a test."
# new_text = re.sub(pattern, " ", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.



# text = "This   is a     test."
# print(text.replace("   ", " "))


# import re
# # Example 1: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}"
# text = "Contact us at support@example.combfjndfenfkenf for more info."
# match = re.search(pattern, text)
# if match:
#     print(f"Email found: {match.group()}")
# else:
#     print("No email found")


# import re
# # Example 2: Extract dates in YYYY-MM-DD format
# # pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# pattern = r"\b\d{2}-\d{2}-\d{4}\b"
# # text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# text = "The event is on 2026-02-29. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']


# import datetime
# date = "2026-02-29"

# try:
#     date = datetime.datetime.strptime(date, "%Y-%m-%d")
# except ValueError as e:
#     print(f"Invalid date entered: {e}")


import re
# Example 3: Validate a phone number (US format)
pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
phone_number = "(123) 456-7890"
if re.match(pattern, phone_number):
    print("Valid phone number")  # Valid phone number
else:
    print("Invalid phone number")

