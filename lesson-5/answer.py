#task 1 temperature.py 
def convert_cel_to_far(celsius):
    return celsius * 9 / 5 + 32


def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Main program
f = float(input("Enter a temperature in degrees F: "))
celsius = convert_far_to_cel(f)
print(f"{f} degrees F = {round(celsius, 2)} degrees C\n")

c = float(input("Enter a temperature in degrees C: "))
fahrenheit = convert_cel_to_far(c)
print(f"{c} degrees C = {round(fahrenheit, 2)} degrees F")


#task 2 invest.py
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")


# Main program
principal = float(input("Enter the initial amount: "))
rate = float(input("Enter the annual rate (as %): ")) / 100
years = int(input("Enter the number of years: "))

invest(principal, rate, years)

#task 3 factors.py 
number = int(input("Enter a positive integer: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")

#task 4 universities.py 
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(data):
    students = [item[1] for item in data]
    tuition = [item[2] for item in data]
    return students, tuition


def mean(values):
    return sum(values) / len(values)


def median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]


# Main program
students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: ${total_tuition:,}\n")
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}\n")
print(f"Tuition mean: ${mean(tuition):,.2f}")
print(f"Tuition median: ${median(tuition):,}")
print("******************************")


#task 5 is_prime.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # check divisibility up to √n
        if n % i == 0:
            return False
    return True


# Example test
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
 
