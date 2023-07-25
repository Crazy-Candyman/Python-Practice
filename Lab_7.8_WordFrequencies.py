import csv

my_list = []
new_list = []

with open("input1.csv", 'r') as my_file:
    contents = csv.reader(my_file, delimiter=',')

    for row in contents:
        for word in row:
            my_list.append(word)

new_list = list(dict.fromkeys(my_list))

for word in new_list:
    print(word, my_list.count(word))