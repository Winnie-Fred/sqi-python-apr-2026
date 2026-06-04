my_name = "Subomi"
# docstring - documentation string
"""This module will teach students functions"""

# def -> define


# def greet():
#     print("Good afternoon!")


# greet()

# print("One thing")

# def greet(name):
#     print(f"Good afternoon, {name}!")

# print("Something")

# greet("Winnie")


# print("Another thing")


# Write a function called cube_num that takes in an integer `num` and prints the cube of num.

# def cube_num(num):
#     print(num ** 3)

# cube_num(8)


# def add_two_nums(num1, num2):
#     print(num1 + num2)

# add_two_nums(8, 3)
# add_two_nums(9, 12)


# Create a function called raise_to_power that accepts `base` and `exponent` and prints base raised to the power of expoennt

# Create a function called turn_to_upper that accepts a `name` and prints the uppercase version of the name




# print("Lorem ipsum dolor")  # 1

# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7 

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8




# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2 , 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()

# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12



# def add_two_nums(num1, num2):
#     print(num1 + num2)


# first_num = 12
# second_num = 0

# add_two_nums(first_num, second_num)

# add_two_nums(num2=second_num, num1=first_num)
# add_two_nums(num2=2, num1=1000)



# add_two_nums(8, 3)
# add_two_nums(9, 12)



# def add_two_nums(num1, num2):
#     return num1 + num2

# print(add_two_nums(8, 3))
# result = add_two_nums(4, 2)
# print(result)



# result = add_two_nums(4, 2)

# print(result % 4)


# name = "Freddie"
# print(name.upper())


# result = name.upper()
# print(result)



# def greet(name):
#     if name == "Winnie":
#         return "Hello, Winnie"
#     if name == "John":
#         return "Hello, John"
    
#     return "Hello stranger"
    
# print(greet("Winnie"))

# def greet(name):
#     if name == "Winnie":
#         print("Hello, Winnie")
#     elif name == "John":
#         print("Hello, John")
#     else:
#         print("Hello stranger")
    
# print(greet("Winnie"))



# 1. Write a function called multiply_nums that takes in `a` and `b` and RETURNS the product of a and b.





# 2. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]

# def turn_to_upper(names):
#     uppercase_names = []
#     for name in names:
#         uppercase_names.append(name.upper())
#     return uppercase_names

# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))

# statically typed
# dynamically typed - Python
# infer
# type hint or annotation

# def turn_to_upper(names: list[str]):
#     return [name.upper() for name in names]

# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))


# ------------------------------*ARGS AND **KWARGS---------------------------------
# *args - arbitrary (0 or more) number of arguments

# print("Yesterday", 8, True, 54, None, "Someone")
# print()

# def greet_everybody(*everyone):
#     print(type(everyone))
#     print(everyone)
#     for person in everyone:
#         print(f"Hello, {person}")


# # greet_everybody(["Taiwo", "Ben", "Debbie", "Abdulateef"])
# greet_everybody("Taiwo", "Ben", "Debbie", "Abdulateef")



# def add_all_nums(*numbers):
#     print(type(numbers))
#     print(numbers)
#     return sum(numbers)


# print(add_all_nums(8, 19, 4, 29, 92, 12, 3))
# # print(add_all_nums(8, 19, 4, 29, "Faith", 92, 12, 3))


# def greet_everyone_with_emojis(**everyone_with_emojis):
#     print(type(everyone_with_emojis))
#     print(everyone_with_emojis)
#     for person, emoji in everyone_with_emojis.items():
#         print(f"{person} is feeling {emoji}")
    

# greet_everyone_with_emojis(taiwo="💃", ben="💀", debbie="😴", abdulateef="🤓")

# everyone_with_emojis = {'taiwo Olaide': '💃', 'ben': '💀', 'debbie': '😴', 'abdulateef': '🤓'}

# greet_everyone_with_emojis(**everyone_with_emojis)

# ====================================ASSIGNMENT===========================================
# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.

# Test Data:
# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))

# Expected Output:
# 14
# 7

# def get_total_length(*words):
#     total_chars = 0
#     for word in words:
#         total_chars += len(word)
#     return total_chars

# def get_total_length(*words):
#     return sum([len(word) for word in words])
    
# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))



# 2. Create a function called multiply_first_two that returns the product of the first two numbers passed in.

# Test Data:
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# Expected Output:
# 15
# 20

# def multiply_first_two(*numbers):
#     return numbers[0] * numbers[1]


# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))
# ------------------------------ARGS AND KWARGS---------------------------------



# default args
# # def multiply_two_nums(number1=6, number2=1):
# def multiply_two_nums(number2=1, number1):
#     return number1 * number2

# # print(multiply_two_nums(5))
# print(multiply_two_nums(number2=5))


# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     return base * power(base, exponent - 1)  # Recursive call
    
# print(power(2, 1000))

# 2 * power(2, 2)

# 2 * 2 * power(2, 1)

# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1 -> 8



# ------------------------------SCOPE--------------------------------

# my_name = "Taiwo"

# def my_func():
#     """Details about my func"""
#     global my_name
#     my_name = "Winnie"
#     print("inside func", my_name)

# my_func()
# print("Outside func", my_name)

# def add(a: int, b: int) -> int:
#     """
#     Add two numbers and return the result.
#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.

#     Returns:
#     int, float: The sum of the two numbers.
#     """
#     return a + b

# ------------------------------SCOPE--------------------------------


# ------------------------------ASSIGNMENT CORRECTION--------------------------------



# 8. Create a function called average_score that returns the average of all scores passed in.

# def average_score(*scores):
#     return sum(scores) / len(scores)

# # Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0


# 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.


# def total_characters(**kwargs):
#     return sum(len(kwarg) for kwarg in kwargs.values())


# # Test Data:
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))

# Expected Output:
# 15
# 7

# # 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# def sum_scores_and_bonuses(*scores, **bonuses):
#     return sum(scores) + sum(bonuses.values())

# # Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# # Expected Output:
# # 50
# # 150

# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# def longest_word(*args, **kwargs):
#     words = list(args) + list(kwargs.values())
#     return max(words, key=len)

# ['cat', 'hippopotamus', 'giraffe', 'eagle']
# [3, 12, 7, 5]
# [3, 5, 7, 12]

# # Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))


# my_dict = {"pen": 50, "bag": 100, "shoe": 129, "basket": 10}

# print(min(my_dict, key=my_dict.get))

# {"pen": 50, "bag": 100, "shoe": 129, "basket": 10}
# 50, 100, 129, 10
# 10, 50, 100, 129
# {"basket": 10, "pen": 50, "bag": 100, "shoe": 129}

# nested_list = [
#     ["ten", 100], 
#     ["twenty", 200], 
#     ["one", 1]
# ]
# [100, 200, 1]
# [200, 100, 1]

# def get_second_item(my_list):
#     return my_list[1]

# print(max(nested_list, key=get_second_item))


# 2. Write a function is_even(n) that returns True if n is even and False if n is odd.

# def is_even(n):
#     return n % 2 == 0

# print(is_even(5))
# print(is_even(100))


# def starts_with_s(word: str):
#     return word.lower().startswith("s")


# # def starts_with_s(word: str):
# #     if word.lower().startswith("s"):
# #         return True
# #     else:
# #         return False
    

# print(starts_with_s("Suleiman"))
# print(starts_with_s("Bobby"))



# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# [1, 2, 4, 0, 0, 7, 5]

def spy_game(list_of_ints):
    nums = []
    for num in list_of_ints:
        if num == 0 or num == 7:
            nums.append(num)

    for i in range(len(nums) - 2):
        sliced = nums[i:i+3]
        print(sliced)
        if sliced == [0, 0, 7]:
            return True
        i += 1

    return False


# def spy_game(list_of_ints):
#     code = [0, 0, 7]
#     for num in list_of_ints:
#         if code and num == code[0]:
#             code.pop(0)


#     return not code    



# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0, 3, 1, 5, 6, 0, 3, 5, 2, 7]))
# [7, 0, 0, 0, 0, 0, 7]

# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

# 23

# 23/2
# 23/3
# 23/4
# 23/5
# ...
# 23/11
# 23/12
# 23/13
# ...
# 23/21
# 23/22



# 9
# 9/2
# 9/3=3.0


# def is_prime(n: int):

#     if n <= 1:
#         return False

#     for i in range(2, int(n ** (1/2)) + 1):
#         if n % i == 0:
#             return False
    
#     return True

# # print(is_prime(23))
# print(is_prime(4))

# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.


# ------------------------------ASSIGNMENT CORRECTION--------------------------------
