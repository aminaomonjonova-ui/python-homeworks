#List Tasks
#task1 
# 1. Count Occurrences
def count_occurrences(lst, element):
    return lst.count(element)
#main part
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
element = int(input("Enter the number to count: "))
print("Occurrences:", numbers.count(element))

    


#task2
# 2. Sum of Elements
def sum_of_elements():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Sum:", sum(numbers))
