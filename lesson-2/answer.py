#Number Data Type Questions
# task 1

number = float(input("введите число: ")) # читаем консоль, преобразуем в число
rounded_number = round(number, 2)
print("rounded number:", rounded_number)

#task 2
num1 = float(input("enter the first number: ")) # читаем число 1
num2 = float(input("enter the seccond number: ")) 
num3 = float(input("enter the third number: "))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("the largest number is:", largest)
print("the smallest number is:", smallest)

#task 3 
km = float(input("Enter distance in kilometers: "))

meters = km * 1000
centimeters = km * 100000

print("Meters:", meters)
print("Centimeters:", centimeters)

#task 4 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

integer_division = a // b
remainder = a % b

print("Integer division result:", integer_division)
print("Remainder:", remainder) 

#task 5 
celsius = float(input("enter temperature in Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("temperature in fahrenheit:", fahrenheit)

#task 6 
num = int(input("enter a number: "))
last_digit = abs(num) % 10
print("last digit:", last_digit)

#task 7 
num = int(input("enter a number:"))
if num % 2 == 0:
    print("the number is even")
else: 
    print("the number is odd")

#String Questions 
#task 1 
from datetime import datetime

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

current_year = datetime.now().year
age = current_year - year_of_birth

print(f"Hello {name}, you are {age} years old.")

#task 2 
txt = 'LMaasleitbtui'
cars = ['Lada', 'Mini', 'Seat', 'Audi', 'BMW', 'Fiat']

found = [car for car in cars if car.lower() in txt.lower()]
print("Found car names:", found)

#task 3 
text = input("Enter a string: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

#task 4 
string = input("Enter a string: ")

if string.lower() == string[::-1].lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

#task 5 
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

#task 6 
text = input("enter main string: ")
word = input("enter word to check")

if word in text: 
    print("yes, it contains the word.")
else:
    print("no, it does not contain the word.")

#task 7
sentence = input("Enter a sentence: ")
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")

new_sentence = sentence.replace(old, new)
print("New sentence:", new_sentence)

#task 8 
# Program to print first and last character of a string
text = input("Enter a string: ")

if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])
else:
    print("Empty string.")

#task 9 
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

#task 10 
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words)) 

#task 11
text = input("Enter a string: ")

if any(ch.isdigit() for ch in text):
    print("String contains digits.")
else:
    print("No digits found.")

#task 12
words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator (e.g. - or ,): ")
joined = separator.join(words)
print("Joined string:", joined)

#task 13 
text = input("Enter a string: ")
print("Without spaces:", text.replace(" ", ""))

#task 14 
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Strings are equal.")
else:
    print("Strings are not equal.")

#task 15 
sentence = input("Enter a sentence: ")
words = sentence.split()
acronym = "".join(word[0].upper() for word in words)
print("Acronym:", acronym)

#task 16 
text = input("Enter a string: ")
char = input("Enter a character to remove: ")

new_text = text.replace(char, "")
print("New string:", new_text)

#task 17 
text = input("Enter a string: ")
symbol = input("Enter a symbol (e.g. *): ")
vowels = "aeiouAEIOU"

for v in vowels:
    text = text.replace(v, symbol)

print("Result:", text)

#task 18 
text = input("enter a sentence: ")
start = input("starts with: ")
end = input("ends with: ")

if text.startswith(start) and text.endswith(end):
    print("yes, it starts and ends correctly.")
else: 
    print ("no, it does not match")

#Boolean Questions
#task 1 
username = input("enter username: ")
password = input ("enter password: ")
is_valid = username !="" and password !=""
print("are both username and password filledd?", is_valid)

#task 2 
a = float(input("enter first number: "))
b = float(input("nter second number: "))
are_equal = a == b 
print("are the numbers equal?", are_equal) 

#task 3 
num = int(input("Enter a number: "))

is_positive_even = num > 0 and num % 2 == 0

print("Is the number positive and even?", is_positive_even)

#task 4 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

all_different = a != b and b != c and a != c

print("Are all numbers different?", all_different) 

#task 5 
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

same_length = len(str1) == len(str2)

print("Do both strings have the same length?", same_length)

#task 6 
num = int(input("Enter a number: "))

divisible = num % 3 == 0 and num % 5 == 0

print("Is the number divisible by both 3 and 5?", divisible) 

#task 7 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

is_greater = (a + b) > 50

print("Is the sum greater than 50?", is_greater) 

#task 8 
num = float(input("enter a number: "))
in_range = 10 <= num <= 20
print ("is the number between 10 and 20 (inclusive)?", in_range)
