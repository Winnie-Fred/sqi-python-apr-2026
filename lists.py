# shopping_list = ["rice", "green beans", "carrots", "onions", "seasoning", "lettuce", "turkey"]
# print(shopping_list)
# print(shopping_list[3])
# shopping_list[-1] = "fish"

# print(shopping_list)

# shopping_list.append("palm oil")
# print(shopping_list)
# shopping_list.insert(3, "palm oil")

# print(shopping_list)
# shopping_list.remove("lettuce")
# print(shopping_list)
# print("carrots" in shopping_list)
# print(shopping_list[:3])

# shopping_list = ["rice", "green beans", "carrots", "onions", "carrots", "seasoning", "lettuce", "turkey"]
# shopping_list.append("rice")

# print(shopping_list)

# Lists are ordered
# Lists are mutable
# Lists are indexed
# Lists allow duplicates


# Create a list called `means_of_transportation` containing "plane", "jet", "boat", "camel", "train"
# 1. Print the last 4 means of transportation
# 2. Add a new means of transportation to the end called "helicopter"
# 3. Add "ship" in between "jet" and "boat"
# 4. Change "plane" to "aeroplane"
# 5. Print the 3rd means of transportation
# 6. Remove "camel" from the list
# 7. Check if "boat" is in the list, True or False.




#                               Ordered         Indexed             Allows Duplicates           Mutable
# List                            Yes             Yes                   Yes                       Yes


this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(this_list[-5:-2])



# this_list[2] = "cashew"


# this_list[2:4] = ["cashew"]
# print(this_list)


# this_list[2:3] = ["cashew"]
# print(this_list)


# numbers = [1, 8, 12, 78, 0]

# "45"

# numbers[2:4] = ["45"]
# numbers[2:4] = "45"

# print(numbers)


# numbers = [1, 8, 12, 78, 0]

# numbers[2] = '10'

# print(numbers)


# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# this_list[2:4] = ["cashew", "guava", "mango"]

# print(this_list)

# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(type(this_list))


# mixed_list = ["banana", 8, 2.9, True, False, "string", None]


# musical_instruments = ("Trumpet", "Guitar", "Piano", "Xylophone", "Drums", "Cello", "Flute")
# print(musical_instruments)
# print(type(musical_instruments))

# musical_instruments = list(musical_instruments)

# print(musical_instruments)
# print(type(musical_instruments))


# del musical_instruments


# musical_instruments = ("Trumpet", "Guitar", "Piano", "Xylophone", "Drums", "Cello", "Flute")
# musical_instruments_list = list(musical_instruments)
# print(type(musical_instruments))
# print(type(musical_instruments_list))


# musical_instruments = ("Trumpet", "Guitar", "Piano", "Xylophone", "Drums", "Cello", "Flute")
# print(id(list(musical_instruments)))
# print(id(musical_instruments))



# ---------------------------------EXTEND----------------------------------------

# musicians = ["Beautiful Nubia", "Kizz Daniel", "Taylor Swift"]
# other_musicians = ["Tye Tribett", "Louren Spencer", "Celine Dion"]

# # all_musicians = musicians + other_musicians

# # print(all_musicians)

# name = "WINNIE"
# lower_name = name.lower()
# print(lower_name)

# musicians = musicians.extend(other_musicians)

# print(musicians)

# musicians.extend(other_musicians)

# print(musicians)
# print(other_musicians)


# other_musicians.extend(musicians)

# print(musicians)
# print(other_musicians)

# list methods work in place, string methods do not.


# water_brands = ["Aquafina", "Nestle", "CWay", "H2O", "Bigi", "Mr. V"]
# other_water_brands = ["Eva", "Aqua", "Nirvana", "Toperimo"]

# ["Aquafina", "Nestle", "CWay", "H2O", "Bigi", "Mr. V", "Eva", "Aqua", "Nirvana", "Toperimo"]

# # water_brands.append(other_water_brands)
# water_brands.append("Eva", "Aqua", "Nirvana", "Toperimo")
# water_brands.extend(("Eva", "Aqua", "Nirvana", "Toperimo"))
# # water_brands.extend("Eva")
# print(water_brands)



# water_brands = "Aquafina",

# print(type(water_brands))
# print(list(water_brands))

# other_water_brands = ["Eva", "Aqua", "Nirvana", "Toperimo"]


# ---------------------------------EXTEND----------------------------------------



# ---------------------------------REMOVING FROM A LIST----------------------------------------

# phone_brands = ["Samsung", "Oppo", "Apple", "Huawei", "Motorola", "Xiaomi", "Nothing", "Motorola", "Google"]
# 1. .remove()
# phone_brands.remove("Motorola")
# phone_brands.remove("Motorola")

# print(phone_brands)

# 2. del
# del phone_brands

# print(phone_brands)

# del phone_brands[4]
# del phone_brands[-2]
# del phone_brands[2]

# print(phone_brands)


# del phone_brands[100]

# print(phone_brands)

# phone_brands.remove("MOTOROLA")


# 3. .pop()


# phone_brands = ["Samsung", "Oppo", "Apple", "Huawei", "Motorola", "Xiaomi", "Nothing", "Motorola", "Google"]
# # phone_brands.pop(-4)
# # phone_brands.pop(5)
# # popped_item = phone_brands.pop()
# # print(popped_item)

# # popped_item = phone_brands.pop(3)
# # print(popped_item)
# phone_brands.pop(3)
# print(phone_brands)

# ---------------------------------REMOVING FROM A LIST----------------------------------------


# ---------------------------------CLEARING A LIST----------------------------------------
# phone_brands = ["Samsung", "Oppo", "Apple", "Huawei", "Motorola", "Xiaomi", "Nothing", "Motorola", "Google"]

# print(id(phone_brands))
# # phone_brands = []
# phone_brands.clear()

# print(id(phone_brands))

# ---------------------------------CLEARING A LIST----------------------------------------



# ---------------------------------SORTING A LIST----------------------------------------

# domestic_animals = ["goat", "hen", "rabbit", "rat", "dog", "parrot"]

# # domestic_animals.sort()
# domestic_animals.sort()
# print(domestic_animals)
# domestic_animals.sort(reverse=True)

# print(domestic_animals)


# # Keyword arg
# # positional arg
# print("hello", "hey", "hi", sep=";")


# domestic_animals = ["goat", "hen", "rabbit", "rat", "Dog", "Parrot"]
# domestic_animals.sort(key=str.lower)
# print(domestic_animals)


# 103, 104, 114, 114, 68, 80

# 68, 80, 103, 104, 114
# ---------------------------------SORTING A LIST----------------------------------------



# ---------------------------------REVERSING A LIST----------------------------------------


# python_builtins = ["print", "max", "sum", "input", "len", "type", "list", "str"]
# # python_builtins = python_builtins[::-1]
# # print(python_builtins)

# python_builtins.reverse()
# print(python_builtins)

# ---------------------------------REVERSING A LIST----------------------------------------



# ---------------------------------COPYING A LIST----------------------------------------

# original = ["one", "two", "three"]
# print(id(original))
# # copy = original.copy()
# copy = original
# print(id(copy))


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix[1][1] = matrix[1][0] + matrix[1][2]

# print(matrix)

# ---------------------------------COPYING A LIST----------------------------------------


# print([1, 3, 4, 5, 1, 9, 1].count(1))
# print(["Ken", "Caleb", "Ken", "Catherine"].count("Ken"))

# 21. Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.

# words = ["Apple", "banana", "Orange"]
# words.sort()
# print(words)



# numbers = ["10", "7", "9"]
# numbers.sort(key=int)
# print(numbers)


# numbers = ["france", "hippo", "cappucino"]
# # numbers.sort()
# numbers.sort(key=len)
# print(numbers)


# numbers = ["france", "house", "hippo", "cappucino"]
# # numbers.sort()
# numbers.sort(key=lambda x: (len(x), None))
# print(numbers)

