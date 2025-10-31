#question 2 Difference between continue and break

#break — полностью останавливает цикл.
#continue — пропускает текущую итерацию и переходит к следующей.
for i in range(5):
    if i == 2:
        continue   # пропускает 2
    if i == 4:
        break      # останавливает цикл
    print(i)
# Output: 0, 1, 3

#question 3 Difference between for and while

#for используется, когда известно количество повторений.
#while — когда повторяем, пока условие истинно.
for i in range(3):  # точно 3 раза
    print(i)

count = 0
while count < 3:    # пока условие
    print(count)
    count += 1

#question 4 Nested for loop example
for i in range(3):
    for j in range(2):
        print(i, j)

#HOMEWORK 
#1. return uncommon elements of lists
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

uncommon = [x for x in list1 if x not in list2] + [y for y in list2 if y not in list1]
print(uncommon)

#2. Squares less than n
n = int(input("Enter n: "))
for i in range(1, n):
    print(i**2)

#3. Underscore insertion rule
txt = input("enter text: ")
result = ""
for i in range(len(txt)):
    result += txt[i]
    if (i+1) % 3 == 0 and i !=len(txt) - 1: 
        if txt[i].lower() in "aeiou" or (i > 0 and result[-2] == "_"):
            continue
        result += "_"
print(result)

#4. number guessing game 
import random

while True:
    number = random.randint(1, 100)
    for attempt in range(10):
        guess = int(input("Guess the number (1-100): "))
        if guess == number:
            print("You guessed it right!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
    else:
        again = input("You lost. Want to play again? (yes/no): ").lower()
        if again not in ['y', 'yes', 'ok']:
            print("Goodbye!")
            break

#5. password checker 
password =  input("Enter password:")

if len(password) < 8 :
    print ("password is too short:() )")
elif not any(h.isupper() for h in password):
    print("password must contain an uppercase letter")
else: 
    print("password is strong")

#6.prime numbers 1-100
for num in range (2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)



    


