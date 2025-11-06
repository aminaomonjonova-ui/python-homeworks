#Farm Model 
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Moo")


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Baa")


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Cluck")


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to the farm.")

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()

# bank app 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive!")
            return
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds!")
            return
        self.balance -= amount
        print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")


# Example
acc1 = BankAccount("Alice", 100)
acc1.deposit(50)
acc1.withdraw(30)
acc1.withdraw(200)
