"""
This program prints a character in the following
format using a for loop.
Three solutions to solve below:
$
$ $
$ $ $
$ $ $ $
$ $ $ $ $
"""

triangle_char = "$"
triangle_height = 5
print()

# Solution One:
i = 1  # i is used as an iterator
for x in triangle_char:
    while i <= triangle_height:  # loop will run until i = triangle_height
        print(triangle_char + " ")
        triangle_char += " " + x
        i += 1  # iterator is incremented

# Solution Two: using a for loop
for i in range(triangle_height + 1):  # i is equal to # of iteration
    print(triangle_char * i)  # "$" is multiplied by "i"

# Solution Three: using a while loop
i = 1
while i <= triangle_height:
    print(triangle_char * i)
    i += 1
