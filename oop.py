# OOP - Object Oriented Programming

# Class - 
# Object - 


# name = "Fred"
# name = name.lower()

# .lower -> string method

# method -> function inside a class

# print(type(name))


# class BankAccount:
#     def __init__(self, bank_name: str, account_number: str, account_balance: float, account_holder: str, is_savings: bool):
#         self.account_holder = account_holder
#         self.is_savings_account = is_savings
#         self.account_number = account_number
#         self.account_balance = account_balance
#         self.bank_name = bank_name

#         print("init running")

#     def account_details(self):
#         return f"""Account Number: {self.account_number}
# Account Holder: {self.account_holder}
# Account Balance: {self.account_balance}
# Account Type: {"Savings" if self.is_savings_account else "Current"}
# Bank Name: {self.bank_name}
# """
    
#     def deposit(self, amount):
#         self.account_balance += amount 
#         print("Deposit successful")
    


# ms_taiwo_acct = BankAccount("First Bank", "3114925311", 50_322_998.54, "Olaide Taiwo", False)
# ms_deborah = BankAccount("Access Bank", "9061519946", 100_234_788_100.12, "Adegboyega Deborah", False)



# print(ms_taiwo_acct.account_details())
# print(ms_deborah.account_holder)

# ms_taiwo_acct.deposit(60_000)
# print(ms_taiwo_acct.account_balance)


# ms_taiwo_acct = {
#     "bank_name": "First Bank",
#     "account_number": "3114925311",
#     "account_balance": 50_322_998.54,
#     "account_holder": "Olaide Taiwo",
#     "is_savings_account": False
# }

# ms_deborah_acct = {
#     "bank_name": "Access Bank",
#     "account_number": "9061519946",
#     "account_balance": 100_234_788_100.12,
#     "account_holder": "Adegboyega Deborah",
#     "is_savings_account": False
# }


# def account_details(acct):
#     return f"""Account Number: {acct["account_number"]}
# Account Holder: {acct["account_holder"]}
# Bank Name: {acct["bank_name"]}
# Account Balance: {acct["account_balance"]}
# Account Type: {"Savings" if acct["is_savings_account"] else "Current"}
# """

# def deposit(acct: dict, amount: float):
#     acct["account_balance"] += amount 
#     print("Deposit successful")


# # print(account_details(ms_taiwo_acct))


# print(ms_taiwo_acct["account_balance"])

# deposit(ms_taiwo_acct, 100_000)

# print(ms_taiwo_acct["account_balance"])



# A class is a template or blueprint for defining what the objects have and what the objects can do
# An object is an instance of a class

# from datetime import datetime

# class Book:
#     def __init__(self, title: str, author: str, number_of_pages: int, isbn: str, cost: float, year_published: int):
#         self.title = title
#         self.author = author
#         self.number_of_pages = number_of_pages
#         self.isbn = isbn
#         self.cost = cost
#         self.year_published = year_published

#     def show_book_details(self):
#         return f"The book {self.title} was written by {self.author} and published in {self.year_published}." 

#     def published_since(self):
#         return datetime.now().year - self.year_published

# things_fall_apart = Book("Things Fall Apart", "Chinua Achebe", 400, "233-28-182-94", 1000.34, 1994)
# print(things_fall_apart)
# print(things_fall_apart.title)
# print(things_fall_apart.author)
# print(things_fall_apart.show_book_details())
# print(things_fall_apart.number_of_pages)
# print(things_fall_apart.published_since())

# things_fall_apart.number_of_pages = 500

# print(things_fall_apart.number_of_pages)


# print(Book("And then there were None", "Agatha Christie", 400, "233-28-182-94", 1000.34, 1994).title)





# 1. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.



# Assignment


# 1. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.




# 2. Create a class called Laptop with the following attributes:
#    - brand
#    - ram (in GB)
#    - storage (in GB)
#    - price
#
#    The class should have two methods:
#    - upgrade_ram(extra_ram): increases the ram by extra_ram
#    - laptop_info(): returns "{brand} laptop with {ram}GB RAM and {storage}GB storage costs {price}."
#
#    After defining the class, create 2 different Laptop objects with different values.





# 3. Create a class called Employee with the following attributes:
#    - name
#    - position
#    - salary
#
#    The class should have two methods:
#    - give_raise(amount): increases salary by amount
#    - employee_info(): returns "{name} works as a {position} and earns {salary} per year."
#
#    After defining the class, create 3 different Employee objects with different values.





# 4. Create a class called Phone with the following attributes:
#    - brand
#    - model
#    - battery_percentage
#
#    The class should have two methods:
#    - charge(amount): increases battery_percentage by amount (do not exceed 100)
#    - phone_status(): returns "{brand} {model} battery is at {battery_percentage}%."
#
#    After defining the class, create 2 different Phone objects with different values.





# 5. Create a class called Product with the following attributes:
#    - name
#    - price
#    - quantity_in_stock
#
#    The class should have three methods:
#    - restock(amount): increases quantity_in_stock by amount
#    - sell(amount): decreases quantity_in_stock by amount
#    - inventory_value(): returns total value of stock (price * quantity_in_stock)
#
#    After defining the class, create 3 different Product objects with different values.





# 6. Create a class called Course with the following attributes:
#    - course_name
#    - instructor
#    - students (a list of student names)
#
#    The class should have two methods:
#    - add_student(name): adds a student to the students list
#    - total_students(): returns the number of students enrolled
#
#    After defining the class, create 2 different Course objects with different values.





# 7. Create a class called Circle with the following attributes:
#     - radius
#
#     The class should have two methods:
#     - area(): returns 3.14 * radius * radius
#     - circumference(): returns 2 * 3.14 * radius
#
#     After defining the class, create 3 different Circle objects with different values.



# 3. Create a class called Movie with the following attributes:
#    - title
#    - genre
#    - ratings (a list of integers)
#    - ticket_price
#
#    The class should have two methods:
#    - average_rating(): returns the average of all ratings
#    - is_hit_movie(): returns True if the average rating is >= 7, otherwise False
#
#    After defining the class, create 2 different Movie objects with different values.


# 5. Create a class called AirConditioner with the following attributes:
#    - brand
#    - temperature
#    - is_on
#
#    The class should have these methods:
#
#    - ac_info()
#      Returns:
#      "{brand} AC is set to {temperature} degrees and it is currently {is_on}."
#
#    - increase_temperature(amount)
#      Increases the temperature by the amount passed into the method.
#
#    - switch_ac(turn_on, new_temperature)
#      Changes is_on to turn_on
#      and changes the temperature to new_temperature.
#
#    After defining the class, create 2 different AirConditioner objects with different values.
#
#    Call all the methods using the objects.

# Sample execution
# ac1 = AirConditioner("LG", 18, False)
# ac2 = AirConditioner("Samsung", 22, True)

# print(ac1.ac_info())
# print(ac2.ac_info())

# ac1.increase_temperature(4)
# print(ac1.ac_info())

# ac2.switch_ac(False, 26)
# print(ac2.ac_info())

# Sample output:
# LG AC is set to 18 degrees and it is currently False.
# Samsung AC is set to 22 degrees and it is currently True.

# LG AC is set to 22 degrees and it is currently False.

# Samsung AC is set to 26 degrees and it is currently False.



# from datetime import datetime


# dunder method - double underscore
# class Book:
#     def __init__(self, title: str, author: str, number_of_pages: int, isbn: str, cost: float, year_published: int):
#         self.title = title
#         self.author = author
#         self.number_of_pages = number_of_pages
#         self.isbn = isbn
#         self.cost = cost
#         self.year_published = year_published

#     # def __str__(self):  # human-readable repr of the obj
#     #     return f"The book {self.title} was written by {self.author} and published in {self.year_published}." 
    
#     def __repr__(self):  # technical repr of the obj
#         return f'Book(title="{self.title}", author="{self.author}", number_of_pages={self.number_of_pages}, isbn="{self.isbn}", cost={self.cost}, year_published={self.year_published})'
    
#     def __len__(self):
#         return self.number_of_pages

#     def published_since(self):
#         return datetime.now().year - self.year_published

# things_fall_apart = Book("Things Fall Apart", "Chinua Achebe", 400, "233-28-182-94", 1000.34, 1994)
# # print(things_fall_apart)
# # print(str(things_fall_apart))
# # print(repr(things_fall_apart))
# print(len(things_fall_apart))



# class Animal:
#     def __init__(self, name: str, type: str, is_mammal: bool, has_wings: bool, has_tail: bool, sound: str, age: int):
#         self.name = name
#         self.type = type
#         self.is_mammal = is_mammal
#         self.has_wings = has_wings
#         self.has_tail = has_tail
#         self.sound = sound
#         self.age = age

#     def make_sound(self):
#         return f"The {self.type} named {self.name} makes a '{self.sound}' sound."
    
# # MOR -> Method Resolution Order
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         self.breed = breed
#         super().__init__(name, "dog", True, False, True, "bark", age)
    
#     def make_sound(self):
#         return super().make_sound() + f" Breed is {self.breed}"

# snake = Animal("Sir Hiss", "snake", False, False, True, "hiss", 2)

# remember = Dog("Remember", 3, "Rottweiler")
# fido = Dog("Fido", 3, "German Sherpherd")

# # print(snake.make_sound())
# # # print(remember.is_mammal)
# # print(remember.make_sound())
# # # print(fido.is_mammal)
# # print(fido.make_sound())


# animals = [snake, fido, remember]

# for animal in animals:
#     print(animal.make_sound())




# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

class GameCharacter:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def attack(self, target):
        if self == target:
            print(f"{self.name} cannot attack themself!")
            return
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}")
        print(f"{target.name}'s health is now {target.health}")
        

# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.


class Warrior(GameCharacter):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self, target):
        target.health -= 10
        super().attack(target)



# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".

class Mage(GameCharacter):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, target):
        if self.mana < 5:
            print("Not enough mana to attack")
            return
        
        self.mana -= 5
        super().attack(target)



# 3. Handle cases where the target is the same as the attacker.
# # SAMPLE EXECUTION 1
warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
warrior.attack(mage)
# Output:
# Thor attacks Merlin!
# Merlin's health is now 80
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 90
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 80
mage.attack(warrior)
# Output:
# Not enough mana to attack
print(warrior.health)  # 80
print(mage.health)  # 80
print(mage.mana)  # 0



# # SAMPLE EXECUTION 2
merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 80
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 90
gaius.attack(gaius)
# Output:
# Gaius cannot attack themself
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 80
merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 60
merlin.attack(gaius)
# Output:
# Not enough mana to attack

