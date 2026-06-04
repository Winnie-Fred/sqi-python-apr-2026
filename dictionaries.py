# phone_book = {"Deborah": "08111625520", "Taiwo": "09056781552", "Benjamin": "09068031356", "Abdulateef": "09154329970"}

# print(phone_book)
# print(len(phone_book))

# print(phone_book["Deborah"])
# print(phone_book["Taiwo"])
# # print(phone_book["David"])

# phone_book["Deborah"] = "09030556590"
# print(phone_book)


# phone_book["Winnie"] = "09030556805"
# print(phone_book)

# del phone_book["Abdulateef"]

# print(phone_book)

# # phone_book.clear()

# # print(phone_book)

# # empty_dict = {}

# print("Benjamin" in phone_book)
# print("09068031356" in phone_book)

# # print(phone_book.keys())
# # print(list(phone_book.keys()))
# # print(type(phone_book.keys()))

# print(phone_book.values())
# print(list(phone_book.values()))
# print(type(phone_book.values()))

# print("09068031356" in phone_book.values())

# print(phone_book.items())
# print(list(phone_book.items()))

# print(phone_book)

# Oyo -> Ibadan
# Ondo -> Akure
# Ogun -> Abeokuta
# Anambra -> Awka

# 1. Create a dict with these states and capitals
# 2. Print the length of the dict
# 3. Add a new entry Ekiti -> Adoekiti
# 4. Change the capital of Oyo to IB
# 5. Remove Anambra from the dict
# 6. Print the keys of the dict as a list
# 6. Print the values of the dict as a list
# 7. Change the capital of Ogun to its uppercased version without using "ABEOKUTA" or "Abeokuta"


# states_and_capitals = {"Oyo": "Ibadan", "Ondo": "Akure", "Ogun": "Abeokuta", "Anambra": "Awka"}

# states_and_capitals["Ogun"] = states_and_capitals["Ogun"].upper()

# print(states_and_capitals)


# ------------------------------ACCESSING DICT ITEMS------------------------------

states_and_capitals = {"Oyo": "Ibadan", "Ondo": "Akure", "Ogun": "Abeokuta", "Anambra": "Awka"}
# print(states_and_capitals["Ogun"])  # square bracket notation
# print(states_and_capitals["Ekiti"])

# print(states_and_capitals.get("Ogun"))  # .get()
# print(states_and_capitals.get("Ekiti"))
# print(states_and_capitals.get("Ekiti", "Adoekiti"))
# print(states_and_capitals)


# print(states_and_capitals.setdefault("Ekiti"))
# print(states_and_capitals)
# print(states_and_capitals.setdefault("Ekiti", "Adoekiti"))
# print(states_and_capitals)
# print(states_and_capitals.setdefault("Ondo"))
# print(states_and_capitals)
# print(states_and_capitals.setdefault("Ondo", "Default for Ondo"))
# print(states_and_capitals)

# ------------------------------ACCESSING DICT ITEMS------------------------------



# ------------------------------CHANGING DICT VALUES------------------------------


# ms_taiwo_dream_car = {
#     "brand": "Lamborghini",
#     "year_manufactured": 2026,
#     "is_electric": False,
#     "color": "White"
# }

# print(ms_taiwo_dream_car)
# # ms_taiwo_dream_car["year_manufactured"] = 2027
# # ms_taiwo_dream_car.update({"year_manufactured": 2027})
# # ms_taiwo_dream_car.update({"speed_mph": 221})

# ms_taiwo_dream_car.update(speed_mph=221, year_manufactured=2027)

# print(ms_taiwo_dream_car)

# ------------------------------CHANGING DICT VALUES------------------------------



# ------------------------------REMOVING FROM A DICT------------------------------

# mr_taiwo_dream_job = {
#     "title": "Cybersecurity Analyst",
#     "salary_in_dollars": 175_000,
#     "is_remote": True
# }

# print(mr_taiwo_dream_job)
# # del mr_taiwo_dream_job["title"]
# # print(mr_taiwo_dream_job.pop("title"))
# print(mr_taiwo_dream_job.popitem())
# print(mr_taiwo_dream_job)


# ms_deborah_dream_husband = {
#     "complexion": "dark",
#     "height_in_ft": "6′3″",
#     "age": 35,
#     "has_money": True,
# }

# print(len(ms_deborah_dream_husband))
# print(type(ms_deborah_dream_husband))


# numbers = ["one", "twenty", "forty two", "six"]
# numbers = [("one", 1), ("twenty", 20), ("forty two", 42), ("six", 6)]
# numbers = [["one", 1], ["twenty", 20], ["forty two", 42], ["six", 6]]

# print(dict(numbers))

# print(dict(one=1, twenty=20, forty_two=42, six=6))


# ------------------------------REMOVING FROM A DICT------------------------------

# Given this dictionary, change the "math" score to 95.
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }
# student["scores"]["math"] = 95
# print(student)



# Assignment correction

# Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# into the list of students.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 70}},
#  {'name': 'Eve', 'scores': {'math': 88, 'english': 92}}]


# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]


# students.append({"name": "Eve", "scores": {"math": 88, "english": 92}})

# print(students)


# Q10. In this shop cart, add a new product "Notebook" with price 200.
# cart = {
#     "items": [
#         {"name": "Pen", "price": 10},
#         {"name": "Book", "price": 50}
#     ],
#     "owner": "Alice"
# }
# Expected Output:
# {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
#  'owner': 'Alice'}



# cart["items"].append({'name': 'Notebook', 'price': 200})

# print(cart)