"""
This program gets a list of integers from input, and outputs
non-negative integers in ascending order (lowest to highest).
"""

user_input = input().split()  # takes input and converts to list
my_list = []
new_list = []

for num in user_input:  # loops through input
    num = int(num)  # turns each num from string to integer
    if num >= 0:
        my_list.append(num)  # adds numbers greater than 0 to my_list
        my_list.sort()  # sorts the list because they are integers

for num in my_list:  # loops through my_list
    num = str(num)  # converts ints to strings
    new_list.append(num)  # adds the numbers to new_list

"""
Now that the inputs are back into a string format
we can use the join method to separate using spaces
which cant be done if the characters are integers.
The program converted the input to a integer so that
I can sort the list from lowest to highest and then needed
to reconvert them back to strings so that I can join them
back into a string with spaces in between.
"""
print(" ".join(new_list), end=" ")
