# name = "Taiwo"

# i = 0

# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1

# name = "Taiwo"

# for char in name:
#     print(char)

# names = ["Taiwo", "Ben", "Abdulateef", "Deborah"]

# for name in names:
#     print(name)

# instruments = ("Guitar", "Xylophone", "Piano", "Organ", "Flute")

# for instrument in instruments:
#     print("john")



# states_and_capitals = {"Ondo": "Akure", "Osun": "Osogbo", "Oyo": "Ibadan", "Ogun": "Abeokuta"}

# print(states_and_capitals.items())
# print(list(states_and_capitals.items())[1])


# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")


# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")


# for capital in states_and_capitals.values():
#     print(capital)
# for state in states_and_capitals.keys():
#     print(state)
# for state in states_and_capitals:
#     print(state)


# print(list(range(0, 10)))

# all even numbers between 10 and 33

# for num in range(10, 33):
#     if num % 2 == 0:
#         print(num)


# for num in range(10, 33, 2):
#     print(num)

# i = 0

# for num in range(10, 33):
#     print(num)
#     i += 1

# print(i)


# actions = ["stand", "walk", "run", "jump", "stop", "sit"]

# # for action in actions:
# #     if action == "stop":
# #         break
# #     print(action)


# for action in actions:
#     if action == "jump":
#         continue
#     print(action)


# actions = ["stand", "walk", "run", "jump", "stop", "sit"]

# i = 1

# for action in actions:
#     print(f"{i}. {action}")
#     i += 1

# for i in range(len(actions)):
#     action = actions[i]
#     print(f"{i+1}. {action}")



# print(list(enumerate(actions, start=2989)))

# for i, action in (enumerate(actions, start=2989)):
#     print(i)
#     print(action)


# for action in actions -> use normal for loop
# for i, action in enumerate(actions) -> use enumerate
# for i in range(len(actions)) -> use range len


# print(list(enumerate(actions, start=100)))

# for index, action in enumerate(actions, start=1):
#     print(index)
#     print(action)

# for index, action in enumerate(actions, start=1):
#     print(f"{index}. {action}")


# 1. stand
# 2. walk
# 3. run
# 4. jump
# 5. stop
# 6. sit



# stand
# walk
# run
# jump
# stop
# sit



# actions = {"stand", "walk", "run", "jump", "stop", "sit"}
# actions = {}

# for action in actions:
#     print(action)
#     if action == "stop":
#         break
# else:
#     print("Loop ended")


# actions = {"stand", "walk", "run", "jump", "sit"}

# for action in actions:
#     print(action)
#     if action == "stop":
#         break
# else:
#     print("Loop ended")


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]


# for adjective in adjectives:
#     for animal in animals:
#         print(f"{adjective} {animal}")


# animals = ["giraffe", "lion", "zebra", "cheetah", "jaguar", "elephant"]

# for animal in animals:
#     print(animal)
#     for char in animal:
#         print(char)

# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin", "hare"]

# print(list(zip(adjectives, animals)))


# for adjective, animal in zip(adjectives, animals):
#     print(f"{adjective} {animal}")


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin", "hare"]

# shortest_list = min([adjectives, animals], key=len)

# for i in range(len(shortest_list)):
#     adjective = adjectives[i]
#     animal = animals[i]
#     print(f"{adjective} {animal}")



# Print numbers that are multiples of 3 and 5 using a for loop netween 11 and 56


# for num in range(11, 56):
#     # if num % 3 == 0 and num % 5 == 0:
#     if num % 15 == 0:
#         print(num)


# hippoppotamus -> HiPpOpOtAm U  s
# hippoppotamus -> 0123456789 10 11
# 0246 10
# 13579 11


# something -> SoMeThInG

# word = input("Enter a word: ")

# chars = []

# for i in range(len(word)):
#     char = word[i]
#     if i % 2 == 0:
#         chars.append(char.upper())
#     else:
#         chars.append(char.lower())

# chars = "".join(chars)
# print(chars)

# word = input("Enter a word: ")

# chars = []

# to_upper = True

# for i in range(len(word)):
#     char = word[i]
#     if to_upper:
#         chars.append(char.upper())
#     else:
#         chars.append(char.lower())
#     to_upper = not to_upper
#     print(char)
#     print(to_upper)

# chars = "".join(chars)
# print(chars)



# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60


# table_number = int(input("Enter the multiplication table number: "))

# for i in range(1, 13):
#     print(f"{table_number} X {i} = {table_number * i}")




# ----------------------------------LIST COMPREHENSION----------------------------------

# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]

# cities_copy = cities.copy()

# print(id(cities))
# print(id(cities_copy))


# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]
# cities_upper = []

# for city in cities:
#     cities_upper.append(city.upper())

# print(cities)
# print(cities_upper)
# print(id(cities))
# print(id(cities_upper))


# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]

# cities_upper = [city.upper() for city in cities]
# print(cities_upper)


# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]

# [5, 5, 4, 6, 10]

# cities_len = [len(city) for city in cities]
# cities_len = [10 for city in cities]
# cities_len = [city for city in cities]

# print(cities_len)


# means_of_transport = ["plane", "lorry", "car", "train", "jet", "ship", "Airplane"]

# a_in_transport = [transport.count("a") for transport in means_of_transport]
# [1, 0, 1, 1, 0, 0]


# means_of_transport = ["PLANE", "lorry", "car", "train", "jet", "ship", "Airplane"]

# endswith_vowel = []
# vowels = ("a", "e", "i", "o", "u")
# for transport in means_of_transport:
#     endswith_vowel.append(transport.lower().endswith(vowels))

# print(endswith_vowel)


# means_of_transport = ["PLANE", "lorry", "car", "train", "jet", "ship", "Airplane"]

# endswith_vowel = [transport.lower().endswith(vowels) for transport in means_of_transport]

# print(endswith_vowel)

# [True, False, False, False, False, False, True]


# nums = [3, 9, 10, 44, 8, 100]

# [False, False, True, True, True, True]


# numbers = [3, 9, 10, 44, 8, 100]

# numbers greater than or equal to 10

# numbers = [3, 9, 10, 44, 8, 100]

# greater_or_equal_10 = [number for number in numbers if number >= 10]

# print(greater_or_equal_10)

# only the numbers greater than or equal to 10
# [False, False, True, True, False, True]

# [10, 44, 100]


# Transformation
# Filtering
# countries = ["Japan", "Nigeria", "USA", "Ghana", "Denmark", "Uganda", "Russia", "France", "South Korea", "China"]

# developed_countries = ["Japan", "USA", "Denmark", "Russia", "France", "South Korea", "China"]

# developing_countries = [country for country in countries if country not in developed_countries]

# print(developing_countries)

# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# newlist = ['hello' for x in languages]
# print(newlist)

# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# all_except_c_plus_plus = []



# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# languages_upper = (language.upper() for language in languages)

# print(list(languages_upper))



# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# languages_upper = {language.upper() for language in languages}
# print(languages_upper)



# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# {"Python": 6, "Java": 4, "C++": 3, "JavaScript": 10, "Ruby": 4}

# len_languages = {language: len(language) for language in languages}
# print(len_languages)



# numbers = [3, 9, 10, 44, 8, 100]
# # [False, False, True, True, False, True]

# greater_or_eq_10 = (number >= 10 for number in numbers)

# print(all(greater_or_eq_10))
# print(any(greater_or_eq_10))

# print(all([True, True, False, False, True]))
# print(all(["John", "Kenny", "Sam", "Benji", "Susan"]))
# print(all(["John", "Kenny", "", "Benji", "Susan"]))
# print(all(["John", "Kenny", "Jack", 0, "Susan"]))


# print(any([True, True, False, False, True]))
# print(any(["John", "Kenny", "Sam", "Benji", "Susan"]))
# print(any(["John", "Kenny", "", "Benji", "Susan"]))
# print(any(["", "", "", "", 0, False, 28]))


# ----------------------------------LIST COMPREHENSION----------------------------------


# ms taiwo - 6
# mr ben - 8, 9, 
# mr lateef - 7, 18


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]

# names_with_a_exist = ["a" in name.lower() for name in names]

# print(any(names_with_a_exist))

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# uppercase_letters = [greeting.isupper() for greeting in greetings]

# print(all(uppercase_letters))


# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
# names = ["Alice", "Bob", "Charlie", "DAVID"]

# names_starting_with_upper = [name[0].isupper() for name in names]

# print(all(names_starting_with_upper))


# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]


# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]



