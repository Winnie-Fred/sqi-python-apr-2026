#                           Ordered             Indexed                 Allow Duplicates               Mutable
# Lists                      Yes                  Yes                       Yes                         Yes
# Tuples                     Yes                  Yes                       Yes                         No
# Dictionaries          Yes from Py 3.9+    Yes, but with keys      Duplicate values, not dupe keys     Yes
# Sets                      No                    No                        No                          Yes



# my_set = {"boy", "girl", "man", "woman", "lady", "boy", "child"}

# print(my_set)

# my_set[0]
# my_set[0:3]

# my_set = {1, "Hello", "me", True, "yours", True}
# print(my_set)
# my_set = {0, 1, "Hello", "me", True, False, "yours", True}
# print(my_set)

# print(len(my_set))

# print(type(my_set))

# word = "hello"
# print(set(word))

# print("".join(set(word)))

# print("boy" in my_set)

# my_set = {}
# my_set = set()
# print(type(my_set))

# ----------------------------------------SET METHODS----------------------------------------------

# anime = {"Demon Slayer", "Death Note", "AOT", "JJK", "SAO", "One Punch Man", "Naruto", "One Piece"}

# anime.add("Solo Leveling")

# print(anime)

# anime = {"Demon Slayer", "Death Note", "AOT", "JJK", "SAO"}
# others = {"One Punch Man", "Naruto", "One Piece"}
# more = {"Tokyo Revengers", "Monster", "Kaiji", "Kaiju No. 8"}
# anime.update(others)
# anime.update(more)
# print(anime)

# anime = {"Demon Slayer", "Death Note", "AOT", "JJK", "SAO"}
# others = {"One Punch Man", "Naruto", "One Piece"}
# more = {"Tokyo Revengers", "Monster", "Kaiji", "Kaiju No. 8"}

# anime = anime.union(others)
# all = anime.union(others).union(more)
# print(anime)
# print(others)
# print(more)
# print(all)


# anime = {"Demon Slayer", "Death Note", "AOT", "JJK", "SAO"}
# others = ["One Punch Man", "Naruto", "One Piece"]
# more = ("Tokyo Revengers", "Monster", "Kaiji", "Kaiju No. 8")
# all = anime.union(others).union(more)

# print(all)

# anime = {"Demon Slayer", "Death Note", "AOT", "JJK", "SAO"}
# others = {"One Punch Man", "Naruto", "One Piece"}
# more = {"Tokyo Revengers", "Monster", "Kaiji", "Kaiju No. 8"}

# all = anime | others | more

# print(all)

# caveat - exception / special rule

# anime = {"Demon Slayer", "Death Note", "AOT", "JJK", "SAO"}
# others = {"One Punch Man", "Naruto", "One Piece"}
# more = ("Tokyo Revengers", "Monster", "Kaiji", "Kaiju No. 8")
# all = anime | others | more


# soups = {"Abula", "Okra", "Efo riro", "Egusi"}
# more_soups = {"Ofe nsala", "Okra", "Ogbono", "Fisherman soup", "Abula", "Oha"}
# other_soups = {"Edikang Ikong", "Afaang", "Black Soup", "Abula"}

# intersection = soups.intersection(more_soups)
# intersection = soups.intersection(more_soups).intersection(other_soups)

# print(intersection)

# soups.intersection_update(more_soups)
# print(soups)

# intersection = soups & more_soups
# print(intersection)

# intersection = soups & more_soups
# print(intersection)


# 7 - 2
# |||||||

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1 = set1.difference(set2)
# # set1.difference_update(set2)
# print(set1)

# soups = {"Abula", "Okra", "Efo riro", "Egusi"}
# more_soups = {"Ofe nsala", "Okra", "Ogbono", "Fisherman soup", "Abula", "Oha"}
# other_soups = {"Edikang Ikong", "Afaang", "Black Soup", "Abula"}

# print(soups - more_soups - other_soups)

# soups = {"Abula", "Okra", "Efo riro", "Egusi"}
# more_soups = {"Ofe nsala", "Okra", "Ogbono", "Fisherman soup", "Abula", "Oha"}
# other_soups = {"Edikang Ikong", "Afaang", "Black Soup", "Abula"}


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# soups = {"Abula", "Okra", "Efo riro", "Egusi"}
# more_soups = {"Ofe nsala", "Okra", "Ogbono", "Fisherman soup", "Abula", "Oha"}
# print(more_soups.symmetric_difference(soups))

# soups.symmetric_difference_update(more_soups)
# print(soups)

# print(soups ^ more_soups)


# ^ - caret
# & - ampersand
# | - pipe


# other_soups = {"Edikang Ikong", "Afaang", "Black Soup", "Abula"}
# # other_soups.remove("Afaang")
# # other_soups.remove("Oha")
# # other_soups.discard("Afaang")
# other_soups.discard("Oha")
# print(other_soups)


# numbers = {1, 9, 4, 8, 2, 3, 7}
# setA = {9, 7, 5}
# setB = {4, 1, 9}

# print(setA.issubset(numbers))

# print(setA.isdisjoint(numbers))

# setC = {0, 5, 6}

# print(setC.isdisjoint(numbers))

# print(setB.issubset(numbers))
# print(setA.issubset(setA))


# # ----------------------------------------SET METHODS----------------------------------------------