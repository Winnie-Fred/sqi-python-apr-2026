# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []

print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2
# waitlist.append("Ken")
# waitlist.append("Jack")
# waitlist.append("Ivy")

waitlist.extend(["Ken", "Jack", "Ivy"])

print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 3
waitlist.extend(["Noah", "Oliver"])
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 4
confirmed_guests.remove("Alice")
confirmed_guests.append(waitlist.pop(0))
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 5
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
charlie_on_waitlist = "Charlie" in confirmed_guests
print(f"It is {charlie_on_waitlist} that Charlie is in the guest list")

# Stage 6
confirmed_guests.remove("David")
confirmed_guests.remove("Eve")
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 7
# confirmed_guests.append(waitlist.pop(0))
# confirmed_guests.append(waitlist.pop(0))
confirmed_guests.extend([waitlist.pop(0), waitlist.pop(0)])
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 8
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 9
print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
last_3_confirmed = confirmed_guests[-3:]
print(f"Last three confirmed guests: {last_3_confirmed}")

# Stage 10
# waitlist.remove("Noah")
# confirmed_guests.append("Noah")
confirmed_guests.append(waitlist.pop(0))
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 11
print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"Number of confirmed guests: {len(confirmed_guests)}")

# Stage 12
print("\n\nStage 12")
confirmed_guests.sort()
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 13
confirmed_guests.remove("Grace")
confirmed_guests.remove("Noah")
confirmed_guests.append("Collins")
confirmed_guests.sort()
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 14
guest_list_for_caterer = confirmed_guests.copy()
print("\n\nStage 14")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"Guest list for caterer: {guest_list_for_caterer}")

# import copy

# my_list = [[1, 2, 3], [4, 5, 6]]
# # my_list = [1, 2, 3, 4, 5, 6]
# # my_list_copy = my_list.copy()
# # my_list_copy = copy.copy(my_list)
# my_list_copy = copy.deepcopy(my_list)

# my_list[0][0] = 11

# print(my_list)
# print(my_list_copy)

# print(id(my_list[0]))
# print(id(my_list_copy[0]))
# print(id(my_list[1]))
# print(id(my_list_copy[1]))


# print(id(my_list))
# print(id(my_list_copy))


# Stage 15
waitlist.clear()
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
