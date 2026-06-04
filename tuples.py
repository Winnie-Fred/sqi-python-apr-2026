#                               Ordered             Mutable             Allow Duplicates        Indexed
# Lists                         Yes                 Yes                     Yes                 Yes
# Tuples                        Yes                 No                      Yes                 Yes


# my_tuple = (1, 2, 3)
# print(my_tuple)
# print(type(my_tuple))


# # my_tuple[1] = 12

# names_of_places = "church", "school", "farm", "hospital"
# other_names_of_places = "airport", "bank", "market", "bank", "police station"

# all_names_of_places = names_of_places + other_names_of_places


# print(names_of_places)
# print(other_names_of_places)
# print(all_names_of_places)


# print(names_of_places[2])

# print(other_names_of_places[:4])


# names_of_places = "church", "school", "farm", "hospital"
# print(len(names_of_places))


# coor1 = (4, 7)
# coor2 = (-5, 8)



# kitchen_utensils = ("bottle", "spoon", "plate", "cup", "blender", "knife")
# print(kitchen_utensils * 5)


# kitchen_utensils = ["bottle", "spoon", "plate", "cup", "blender", "knife"]
# print(kitchen_utensils * 5)


# print("hello" * 7)


# kitchen_utensils = ["bottle", "spoon", "plate", "cup", "blender", "knife"]
# kitchen_utensils_times_5 = kitchen_utensils * 5
# print(kitchen_utensils_times_5)

# fruits = "apple", "banana", "cherry"
# green, yellow, red = fruits

# print(green)
# print(yellow)
# print(red)


# *some_musicians, obo, taylor, burna = "Davido", "Wizkid", "Kizz Daniel", "Taylor Swift", "Burna Boy"
# print(some_musicians)



# *_, burna = "Davido", "Wizkid", "Kizz Daniel", "Taylor Swift", "Burna Boy"
# # print(some_musicians)

# print(_)
# print(burna)


# print(_)



# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. 
# Print the extracted age and the first department.

# record = ("Jane", (32, "Manager"), ["HR", "Finance"])

# name, age_position, depts = record

# age, position = age_position

# dept1, dept2 = depts

# print(age)
# print(dept1)


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (dept1, dept2) = record
# print(age)
# print(dept1)
# print(f"The {position} is {name}. She manages {dept1} and {dept2} and she is {age} years old.")


# Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.

info = ("product123", ("Electronics", 299.99), (20, 5, 2022))


