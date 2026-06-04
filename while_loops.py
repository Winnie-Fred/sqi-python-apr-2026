# # print("Hello John")
# # print("Hello John")
# # print("Hello John")
# # print("Hello John")
# # print("Hello John")
# # print("Hello John")



# # while loop

# # while this, do that

# i = 1

# no_of_times = int(input("Enter how many times you want to greet John: "))

# while i <= no_of_times:
#     print("Hello John")
#     i += 1


# print("loop ended")



# 10
# 9
# ...
# 0

# i = 10

# while i >= 0:
#     # print("London")
#     print(i)
#     i -= 2


# # 1. Count from 19 to 38 i.e. 19, 20, 21, ..., 36, 37, 38

# i = 19

# while i <= 38:
# # while i < 39:
#     print(i)
#     i += 1


# # 1. Count from 50 to 36 i.e 50, i.e. 50, 48, 46, 44, ..., 40, 38, 36

# i = 50

# while i >= 36:
#     print(i)
#     i -= 2


# 3. Print all multiples of 5 between 20 and 67 i.e. 20, 25, 30, 35, 40, 45, 50, 55, 60, 65
# But do not use += 5

# i = 20

# while i <= 67:
#     print(i)
#     i += 5


# i = 20

# while i <= 67:
#     if i % 5 == 0:
#         print(i)
#     i += 1


# 1 - 50

# "1, 2, 3, 4, 5, 6, ..., 47, 48, 49, 50"


# i = 1

# numbers = []

# while i <= 50:
#     numbers.append(str(i))
#     i += 1



# numbers = ", ".join(numbers)

# print(numbers)
# nums = ["2", "8", "9"]
# print(", ".join(nums))


# numbers = ""
# i = 1
# while i <= 50:
#     numbers += str(i)
#     if i != 50:
#         numbers += ", "
#     i += 1

# print(numbers)


# i = 1

# while i <= 17:
#     print(i)
#     if i == 12:
#         break
#     i += 1


# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17

# i = 0

# while i < 17:
#     i += 1
#     if i == 12:
#         continue
#     print(i)



# i = 5

# while i < 10:
#     i += 1
#     if i == 8:
#         continue
#     print(i)


# 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19

# i = 3

# while i < 20:
#     i += 1
#     if i % 5 == 0:
#         continue
#     print(i)


# i = 678
# while i <= 50:
#     print(i)
#     i += 1
# else:
#     print("Loop has ended")

# 6. Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****

# no_of_times = int(input("Enter the length of the square: "))

# i = 1

# while i <= no_of_times:
#     print("*" * no_of_times)
#     i += 1




# -------------------------------------ASSIGNMENT CORRECTION---------------------------------------
# Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5
# Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello
# Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10
# Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1

#  5. Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 1

# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1





#  6. 	Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


#  7.	Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****
#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#  9. 	Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111

# i = 1

# ones= []

# while i <= 10:
#     ones.append("1")
#     i += 1

# print("".join(ones))



# 10.  Print a list of the first 12 multiples of 3 starting from 3

# i = 1

# while i <= 12:
#     print(3 * i)
#     i += 1


# i = 1

# multiples_of_12 = []

# while len(multiples_of_12) != 12:
#     if i % 3 == 0:
#         multiples_of_12.append(i)
#     i += 1

# print(multiples_of_12)


# Write a program that uses a while loop to print numbers from 1 to 10.


# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. g if n is 5, do 1+2+3+4+5 (15).

# total = 0
# result = []

# n = int(input("Enter the value of n: "))
# i = 1
# while i <= n:
#     total += i
#     result.append(str(i))
#     i += 1

# result = "+".join(result)
# result = f"{result}={total}"
# print(result) 
# # 15
# # 1+2+3+4+5=15

# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.
# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.



# 5. Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.



# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

# result = 1

# i = 1

# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# while i <= exponent:
#     # result *= base
#     result = result * base
#     i += 1

# print(f"{base} raised to the power of {exponent} is {result}")

# # 5^6 -> 5 X 5 X 5 X 5 X 5 X 5




# -------------------------------------ASSIGNMENT CORRECTION---------------------------------------


# iterables -> lists, strings, tuples, dicts, sets

# iterate -> to iterate means to loop



# name = "Taiwo"

# # T
# # a
# # i
# # w
# # o


# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
# # print(name[5])


# i = 0

# while i < len(name):
# # while i <= len(name) - 1:
#     print(name[i])
#     i += 1



# animals = ["giraffe", "lion", "zebra", "cheetah", "jaguar", "elephant"]


# 1. giraffe
# 2. lion
# 3. zebra
# 4. cheetah
# 5. jaguar
# 6. elephant


# animals = ["giraffe", "lion", "zebra", "cheetah", "jaguar", "elephant"]

# i = 0
# while i < len(animals):
#     animal = animals[i]
#     print(animal)
    
#     j = 0

#     while j < len(animal):
#         print(animal[j])
#         j += 1

#     i += 1


# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350


# balance = int(input("Enter your balance: "))

# while True:
#     withdrawal_amt = int(input("Enter withdrawal amount: "))
#     if withdrawal_amt <= balance:
#         balance -= withdrawal_amt
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Insufficient funds")

#     another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").lower().strip() == "yes"

#     if not another_withdrawal:
#         print(f"Final balance: {balance}")
#         break


# balance = int(input("Enter your balance: "))

# main_loop = True

# while main_loop:
#     withdrawal_amt = int(input("Enter withdrawal amount: "))
#     if withdrawal_amt <= balance:
#         balance -= withdrawal_amt
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Insufficient funds")

    
#     while True:
#         another_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").lower().strip()

#         if another_withdrawal == "no":
#             print(f"Final balance: {balance}")
#             main_loop = False
#             break

#         if another_withdrawal == 'yes':
#             break

#         print("Invalid response, enter yes or no")

    

# CORRECT_NAME = "John"


# while True:
#     name = input("Enter your name: ")
#     if name != CORRECT_NAME:
#         print("Name is not correct")
#         continue
#     break

# while True:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         print("Age must be 0 or more")
#         continue
#     break


# vowels = ("a", "e", "i", "o", "u")
# while True:
#     word = input("Enter a word to count the number of vowels: ").lower()

#     if word == "stop":
#         break

#     no_of_vowels = 0
#     i = 0
    
#     while i < len(word):
#         char = word[i]
#         if char in vowels:
#             no_of_vowels += 1
#         i += 1

#     print(f"No of vowels in {word} is {no_of_vowels}")

# DSA - Data Structures and Algorithms



# Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48


# total = 0.0

# while True:
#     price = float(input("Enter item price: "))

#     total += price


#     not_another_item = input("Enter another item? (yes/no): ").strip().lower() != "yes"
#     if not_another_item:
#         print(f"Total cost: {total}")
#         break



    # another_item = input("Enter another item? (yes/no): ").strip().lower() == "yes"
    # if another_item:
    #     continue

    # print(f"Total cost: {total}")
    # break





# Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

# while True:
#     password = input("Enter password: ").strip()

#     if 8 <= len(password) <= 25:
#         print("Password accepted.")
#         break

#     print("Password must be at least 8 characters long and have a maximum of 25 characters.")


# while True:
#     password = input("Enter password: ").strip()

#     if not(8 <= len(password) <= 25):
#         print("Password must be at least 8 characters long and have a maximum of 25 characters.")
#         continue

#     print("Password accepted.")
#     break

# password = ''

# while not(8 <= len(password) <= 25):
#     password = input("Enter password: ")
#     if not(8 <= len(password) <= 25):
#         print("Password must be at least 8 characters long and have a maximum of 25 characters.")
#         continue
# else:
#     print("Password accepted.")
    



# 5. Write a program that tracks the inventory of items in a store. The user should be able 
# to add or remove items and the program should display the current inventory after each
# operation. The program stops when the user decides to exit.
# The current store inventory is {'eggs': 40, 'fish': 200, ‘bread': 343, ‘yam':2}
# Sample Input and Output:
# Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

# refactoring

# inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam':2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()
    
#     if operation == "exit":
#         print("Goodbye")
#         break
    
#     if operation not in ["add", "remove"]:
#         print("Invalid operation")
#         continue

#     item = input("Enter item: ").strip().lower()
    # quantity = int(input("Enter quantity: "))

    # if operation == "add":

    #     if item in inventory:
    #         inventory[item] += quantity
    #     else:
    #         inventory[item] = quantity

    #     print(f"Current inventory: {inventory}")
    # elif operation == "remove":
    #     if item in inventory:
    #         inventory[item] -= quantity
    #     else:
    #         print(f"{item} not in inventory")

    #     print(f"Current inventory: {inventory}")
    


# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.

# import random

# secret_number = random.randint(1, 50)

# attempts = 5

# while attempts >= 1:
#     guess = int(input("Guess the secret number: "))

#     if guess == secret_number:
#         print("Congratulations!!! 🥳. You guessed the secret number correctly.")
#         break

#     if guess < secret_number:
#         print("You guessed too low")
#     else:
#         print("You guessed too high")

#     attempts -= 1

#     print(f"You have {attempts} attempts left")

# else:
#     print(f"You used up all your attempts. The secret number is {secret_number}")




# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# CORRECT_PASSWORD = 'secret'

# while True:
#     password = input("Enter password: ").strip()

#     if password == CORRECT_PASSWORD:
#         print("Password accepted.")
#         break

#     print("Invalid password. Try again")



# 10. Write a program that takes comma-separated integers from the user, converts that
# to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
# Use the min() function.

# numbers = tuple(input("Enter comma-separated integers: ").split(","))
# print(type(numbers))

# i = 1

# smallest = int(numbers[0])

# while i < len(numbers):
#     number = int(numbers[i])

#     if number < smallest:
#         smallest = number
#     i += 1

# print(f"{smallest} is the smallest")


# 11. Write a program that takes a string input from the user and uses a while loop to count
# the occurrences of each character, storing the counts in a dictionary.
# Sample Input:
# Enter a string: Hello
# Sample Output:
# {‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# hippoppotamus


# h -> 1
# i -> 1
# p -> 4
# o -> 2
# t -> 1
# a -> 1
# m -> 1
# u -> 1
# s -> 1

# occurences = {}

# i = 0

# text = input("Enter some text: ").strip().lower()

# while i < len(text):
#     char = text[i]

#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1
#     i += 1
# print(occurences)




