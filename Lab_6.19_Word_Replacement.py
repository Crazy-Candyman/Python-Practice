"""
This program replaces words in a sentence. The input begins
with word replacement pairs (original and replacement).
The next line of input is the sentence where any word on
the original list is replaced.
"""

# Turn this into pairs
user_input = [
    "automobile",
    "car",
    "manufacturer",
    "maker",
    "children",
    "kids",
]
sentence = "The automobile manufacturer recommends car seats for children if the automobile doesn't already have one."

# The sentence should read:
# The car maker recommends car seats for kids if the car doesn't already have one.

for index, key in enumerate(user_input):  # enumerate used to have index variable
    if index % 2 == 0:  # dictacte if index odd or even to distinguish pairs
        # print("key: ", user_input[index])
        # print("value: ", user_input[index + 1])

        sentence = sentence.replace(user_input[index], user_input[index + 1])

print(sentence)
