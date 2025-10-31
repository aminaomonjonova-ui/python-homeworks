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
# Function version
def sum_of_elements(lst):
    return sum(lst)

# Interactive version
def sum_of_elements_interactive():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Sum:", sum_of_elements(lst))


#task 3 
# Find the largest element in a list

my_list = [3, 7, 2, 9, 5]

maximum = max(my_list)

print("The largest element is:", maximum)

#task 4
# Find the smallest element in a list

my_list = [3, 7, 2, 9, 5]

minimum = min(my_list)

print("The smallest element is:", minimum) 

#task 5
my_list = [1, 2, 3, 4, 5]
element = int(input("enter an element to check"))

is_present = element in my_list
print("is the element in the list?", is_present)

#task 6 
my_list = [10, 20, 30]
print(my_list[0] if my_list else "List is empty")

#task 7 
my_list = [10, 20, 30]
print(my_list[-1] if my_list else "List is empty")
 

#task 8 
my_list = [1, 2, 3, 4, 5]
print(my_list[:3])

#task 9 
my_list = [1, 2, 3, 4, 5]
print(list(reversed(my_list)))

# Task 10: Sort the list
my_list = [5, 1, 4, 2, 3]
sorted_list = sorted(my_list)
print("Sorted list:", sorted_list)

# Task 11: Remove duplicates from a list
my_list = [1, 2, 2, 3, 3, 4]
unique_list = list(set(my_list))
print("List without duplicates:", unique_list)

# Task 12: Insert an element at a given index
my_list = [1, 2, 3]
index = int(input("Enter index: "))
element = input("Enter element: ")
my_list.insert(index, element)
print("Updated list:", my_list)

# Task 13: Find the index of an element
my_list = [10, 20, 30, 40]
element = int(input("Enter element: "))
if element in my_list:
    print("Index:", my_list.index(element))
else:
    print("Element not found in the list.")

# task 14 check if a list is empty
my_list = []
print("is the list empty?", len(my_list)==0)

# Task 15: Count even numbers in the list
my_list = [1, 2, 3, 4, 5, 6]
count = sum(1 for x in my_list if x % 2 == 0)
print("Number of even numbers:", count)

# Task 16: Count odd numbers in the list
my_list = [1, 2, 3, 4, 5, 6]
count = sum(1 for x in my_list if x % 2 != 0)
print("Number of odd numbers:", count)

# Task 17: Combine two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined list:", combined) 

# task 18 find sublist 
main_list = [1, 2, 3, 4, 5]
sub_list = [2, 3]
is_present = str(sub_list)[1:-1] in str(main_list)[1:-1]
print("is sublist present?", is_present)

# Task 19: Replace an element in the list
my_list = [1, 2, 3, 4]
old = int(input("Element to replace: "))
new = int(input("New element: "))
if old in my_list:
    my_list[my_list.index(old)] = new
print("Updated list:", my_list)


# Task 20: Find the second largest element
my_list = [10, 20, 4, 45, 99]
unique = list(set(my_list))
unique.sort()
print("Second largest:", unique[-2])


# Task 21: Find the second smallest element
my_list = [10, 20, 4, 45, 99]
unique = list(set(my_list))
unique.sort()
print("Second smallest:", unique[1])

#task 22 get only even numbers
my_list = [1, 2, 3, 4, 5]
evens = [x for x in my_list if x % 2 == 0]
print("even numbers:", evens) 

# Task 23: Get only odd numbers
my_list = [1, 2, 3, 4, 5, 6]
odds = [x for x in my_list if x % 2 != 0]
print("Odd numbers:", odds)


# Task 24: Find number of elements in list
my_list = [1, 2, 3, 4]
print("Number of elements:", len(my_list))


# Task 25: Copy a list
my_list = [1, 2, 3]
copy_list = my_list.copy()
print("Copied list:", copy_list)

# Task 26: Find the middle element(s)
my_list = [1, 2, 3, 4, 5, 6]
n = len(my_list)
if n % 2 == 0:
    print("middle elements:", my_list[n//2])
else:
    print("middle element:", my_list[n//2])

# Task 27: Find max in sublist
my_list = [1, 5, 3, 9, 7, 2]
start = int(input("Start index: "))
end = int(input("End index: "))
print("Maximum in sublist:", max(my_list[start:end]))

# Task 28: Find min in sublist
my_list = [1, 5, 3, 9, 7, 2]
start = int(input("Start index: "))
end = int(input("End index: "))
print("Minimum in sublist:", min(my_list[start:end]))

# Task 29: Remove an element by index
my_list = [10, 20, 30, 40]
index = int(input("Enter index: "))
if 0 <= index < len(my_list):
    my_list.pop(index)
print("Updated list:", my_list)

# Task 30: Check if list is sorted in ascending order
my_list = [1, 2, 3, 4, 5]
print("is list sorted?", my_list == sorted(my_list))

# Task 31: Repeat each element n times
my_list = [1, 2, 3]
n = int(input("Repeat count: "))
new_list = [x for x in my_list for _ in range(n)]
print("Repeated list:", new_list)

# Task 32: Merge two lists and sort
list1 = [3, 1, 4]
list2 = [2, 5]
merged = sorted(list1 + list2)
print("Merged and sorted list:", merged)

# Task 33: Find all indices of an element
my_list = [1, 2, 3, 2, 4, 2]
element = int(input("Element to find: "))
indices = [i for i, x in enumerate(my_list) if x == element]
print("Indices:", indices)

# Task 34: Rotate list to the right
my_list = [1, 2, 3, 4, 5]
k = int(input("rotate by:"))
k %=len(my_list)
rotated = my_list[-k:] + my_list[:-k]
print("rotated list:", rotated)

# Task 35: Create a list in a specific range
start = int(input("Start: "))
end = int(input("End: "))
print("Range list:", list(range(start, end + 1)))

# Task 36: Find sum of positive numbers
my_list = [-2, 3, -5, 7, 9, -1]
positive_sum = sum(x for x in my_list if x > 0)
print("Sum of positive numbers:", positive_sum)


# Task 37: Find sum of negative numbers
my_list = [-2, 3, -5, 7, 9, -1]
negative_sum = sum(x for x in my_list if x < 0)
print("Sum of negative numbers:", negative_sum)

# Task 38: Check if a list is palindrome
my_list = [1, 2, 3, 2, 1]
print("is palindrome?", my_list == my_list[::-1])

# Task 39: Create nested lists from main list
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
size = int(input("Sublist size: "))
nested = [my_list[i:i+size] for i in range(0, len(my_list), size)]
print("Nested list:", nested)

# Task 40: Get unique elements in order
my_list = [1, 2, 2, 3, 1, 4, 3, 5]
unique = []
for x in my_list:
    if x not in unique:
        unique.append(x)
print("Unique elements (in order):", unique)

#SET TASKS 
#task 1: union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)

#task 2: intersection of sets 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("intersection:", set1 & set2)

#task 3: difference of sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print("difference:", set1 - set2)

#task 4: check subset 
set1 = {1, 2}
set2 = {3, 4, 5}
print("is subset:", set1.issubset(set2))

#task 5: check element
set1 = {1, 2, 3, 4}
element = int(input("Enter element: "))
print(element in set1)

# task 6: set length 
set1 = {10, 20, 30, 40}
print("Number of elements:", len(set1))

#task 7: convert list to set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("Unique elements:", unique_set)

#task 8: remove element 
set1 = {1, 2, 3, 4}
set1.discard(3)
print("After removal:", set1)

#task 9: clear set
set1 = {1, 2, 3}
set1.clear()
print("Cleared set:", set1)

#task 10: check if set is empty 
set1 = set()
print("Is empty:", len(set1) == 0)

#task 11: symmetric difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Symmetric Difference:", set1 ^ set2)
 
#task 12: add element 
set1 = {1, 2, 3}
set1.add(4)
print("after adding:", set1)

#task 13: pop element 
set1 = {1, 2, 3, 4}
popped = set1.pop()
print ("popped element:", popped)
print("set after pop", set1)

#task 14: find max
set1 = {3, 7, 1, 9, 4}
print("Maximum:", max(set1))

#task 15 : find min 
set1 = {3, 7, 1, 9, 4}
print("Minimum:", min(set1))

#task 16: 
nums = {1, 2, 3, 4, 5, 6}
even_nums = {n for n in nums if n % 2 == 0}
print("Even numbers:", even_nums)

#task 17: filter odd numbers 
nums = {1, 2, 3, 4, 5, 6}
odd_nums = {n for n in nums if n % 2 != 0}
print("Odd numbers:", odd_nums)

#task 18 : create a set of a range 
nums = set(range(1, 11))
print("Set from 1 to 10:", nums)

#task 19: merge and deduplicate
list1 = [1, 2, 2, 3]
list2 = [3, 4, 4, 5]
merged_set = set(list1 + list2)
print("Merged unique set:", merged_set)

#task 20: check disjoint sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print ("are disjoints:", set1.isdisjoint(set2))

#task 21: remove duplicates from a list 
my_list = [1, 2, 2, 3, 3, 4]
unique_list = list(set(my_list))
print("List without duplicates:", unique_list)

#Task 22: count unique elements
my_list = [1, 2, 2, 3, 3, 4]
print("Count of unique elements:", len(set(my_list)))
 
#task 23: generate random set 
import random
rand_set = {random.randint(1, 50) for _ in range(5)}
print("Random set:", rand_set)

#TUPLE TASKS
#task 1 :Count Occurrences
my_tuple = (1, 2, 3, 2, 4, 2, 5)
element = int(input("Enter element to count: "))
print("Occurrences:", my_tuple.count(element))

#task 2: max element 
my_tuple = (3, 7, 2, 9, 5)
print("Max element:", max(my_tuple))
 
#task 3: min element
my_tuple = (3, 7, 2, 9, 5)
print("Min element:", min(my_tuple))

#task 4: check element 
my_tuple = (1, 2, 3, 4, 5)
element = int(input("Enter element to check: "))
print(element in my_tuple)
 
#task 5 : First Element 
my_tuple = (10, 20, 30)
if my_tuple:
    print("First element:", my_tuple[0])
else:
    print("Tuple is empty")

#task 6: Last Element
my_tuple = (10, 20, 30)
if my_tuple:
    print("Last element:", my_tuple[-1])
else:
    print("Tuple is empty")

#task 7: Tuple Length 
my_tuple = (1, 2, 3, 4, 5)
print("Length:", len(my_tuple))

#task 8 :Slice Tuple
my_tuple = (10, 20, 30, 40, 50)
print("First three elements:", my_tuple[:3])

#task 9: Concatenate Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Combined tuple:", combined)
 
#task 10:Check if Tuple is Empty
my_tuple = ()
print("Is empty:", len(my_tuple) == 0)

#task 11: Get All Indices of Element
my_tuple = (1, 2, 3, 2, 4, 2)
element = int(input("Enter element: "))
indices = [i for i, x in enumerate(my_tuple) if x == element]
print("Indices:", indices)

#task 12 :Find Second Largest
my_tuple = (3, 7, 1, 9, 4)
sorted_tuple = sorted(set(my_tuple))
print("Second largest:", sorted_tuple[-2])

#task 13 : Find Second Smallest
my_tuple = (3, 7, 1, 9, 4)
sorted_tuple = sorted(set(my_tuple))
print("Second smallest:", sorted_tuple[1])

#task 14: Create a Single Element Tuple
element = input("Enter an element: ")
single_tuple = (element,)
print("Single element tuple:", single_tuple)

#task 15:Convert List to Tuple
my_list = [1, 2, 3, 4]
converted = tuple(my_list)
print("Converted tuple:", converted)

#task 16: Check if Tuple is Sorted
my_tuple = (1, 2, 3, 4, 5)
print("Is sorted:", my_tuple == tuple(sorted(my_tuple)))

#task 17: Find Maximum of Subtuple 
my_tuple = (5, 3, 8, 1, 9, 2)
start, end = 1, 4
print("Max of subtuple:", max(my_tuple[start:end]))

#task 18: Find Minimum of Subtuple
my_tuple = (5, 3, 8, 1, 9, 2)
start, end = 1, 4
print("Min of subtuple:", min(my_tuple[start:end]))

#task 19 : Remove Element by Value
my_tuple = (1, 2, 3, 2, 4)
element = 2
new_tuple = tuple(x for x in my_tuple if x != element or (element := None))
print("After removal:", new_tuple)

#task 20 : Create Nested Tuple
my_tuple = (1, 2, 3, 4, 5, 6)
nested = (my_tuple[:3], my_tuple[3:])
print("Nested tuple:", nested)

#task 21: repeat elements 
my_tuple = (1, 2, 3)
times = int(input("Enter repeat count: "))
print("Repeated tuple:", my_tuple * times)

#task 22 : create range tuple 
range_tuple = tuple(range(1, 11))
print("Range tuple:", range_tuple)

#task23 : reverse tuple 
my_tuple = (1, 2, 3, 4, 5)
print("Reversed tuple:", my_tuple[::-1])

#task 24: check pelindrome 
my_tuple = (1, 2, 3, 2, 1)
print("Is palindrome:", my_tuple == my_tuple[::-1])

#task 25: get unique elements 
my_tuple = (1, 2, 2, 3, 3, 4, 5)
unique = []
for x in my_tuple: 
    if x not in unique:
        unique.append(x)
print("unique elements tuples:", tuple(unique))

#DICTIONARY TASKS
# 1. Get Value
def get_value(d, key):
    return d.get(key, "Key not found")

# 2. Check Key
def check_key(d, key):
    return key in d

# 3. Count Keys
def count_keys(d):
    return len(d)

# 4. Get All Keys
def get_all_keys(d):
    return list(d.keys())

# 5. Get All Values
def get_all_values(d):
    return list(d.values())

# 6. Merge Dictionaries
def merge_dicts(d1, d2):
    return {**d1, **d2}

# 7. Remove Key
def remove_key(d, key):
    d.pop(key, None)
    return d

# 8. Clear Dictionary
def clear_dict():
    return {}

# 9. Check if Dictionary is Empty
def is_empty(d):
    return len(d) == 0

# 10. Get Key-Value Pair
def get_pair(d, key):
    return (key, d[key]) if key in d else None

# 11. Update Value
def update_value(d, key, value):
    d[key] = value
    return d

# 12. Count Value Occurrences
def count_value_occurrences(d, value):
    return list(d.values()).count(value)

# 13. Invert Dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}

# 14. Find Keys with Value
def find_keys_with_value(d, value):
    return [k for k, v in d.items() if v == value]

# 15. Create a Dictionary from Lists
def dict_from_lists(keys, values):
    return dict(zip(keys, values))

# 16. Check for Nested Dictionaries
def has_nested_dict(d):
    return any(isinstance(v, dict) for v in d.values())

# 17. Get Nested Value
def get_nested_value(d, outer_key, inner_key):
    return d.get(outer_key, {}).get(inner_key, "Not found")

# 18. Create Default Dictionary
from collections import defaultdict
def create_default_dict(default_value):
    return defaultdict(lambda: default_value)

# 19. Count Unique Values
def count_unique_values(d):
    return len(set(d.values()))

# 20. Sort Dictionary by Key
def sort_by_key(d):
    return dict(sorted(d.items()))

# 21. Sort Dictionary by Value
def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# 22. Filter by Value
def filter_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

# 23. Check for Common Keys
def common_keys(d1, d2):
    return set(d1.keys()) & set(d2.keys())

# 24. Create Dictionary from Tuple
def dict_from_tuple(t):
    return dict(t)

# 25. Get the First Key-Value Pair
def first_pair(d):
    return next(iter(d.items())) if d else None
