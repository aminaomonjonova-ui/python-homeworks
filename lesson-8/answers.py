#Farm Model 
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.sound = "Some sound"

    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self, hours):
        print(f"{self.name} sleeps for {hours} hours.")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cow", age)
        self.sound = "Moo"


class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Sheep", age)
        self.sound = "Baa"


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Chicken", age)
        self.sound = "Cluck"


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to the farm.")

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()

#bank 
import random
import json
import os

class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def __str__(self):
        return f"Account {self.account_number} | Owner: {self.owner} | Balance: {self.balance}"


class Bank:
    def __init__(self, filename="accounts.json"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def generate_account_number(self):
        while True:
            num = random.randint(1000, 9999)
            if num not in self.accounts:
                return num

    def create_account(self, owner, initial_deposit=0):
        account_number = self.generate_account_number()
        account = Account(account_number, owner, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created! Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found!")

    def save_to_file(self):
        data = {num: {"owner": acc.owner, "balance": acc.balance} for num, acc in self.accounts.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for num, info in data.items():
                    self.accounts[int(num)] = Account(int(num), info["owner"], info["balance"])



