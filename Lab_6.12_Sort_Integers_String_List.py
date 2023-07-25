"""
This program takes an input of integers in string format with spaces (ex: 20 17 5 3),
and converts it to a list at the same time converting to integers to accomplish
mathematical expressions.
"""

user_input = input().split()  # input ex: 20 10 5 2 (turns into a list)
my_list = []

for num in user_input:  # loops through inputs
    my_list.append(int(num))  # adds the inputs to list and converts to int.

avg = sum(my_list) // len(my_list)
list_max = max(my_list)

print(avg, list_max)
