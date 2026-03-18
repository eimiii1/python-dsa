# Problem 1: List Manipulation

# Given this list:
numbers = [3, 7, 1, 9, 2, 5, 8]
even_numbers = []

# Algorithm
# 1. Removes all odd numbers
# 2. Doubles the remaining even numbers
# 3. Sort them in descending order

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i * 2)

print(sorted(even_numbers, reverse=True))