'''
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons)

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating multiple TV shows associated with the same key with a semicolon (;). Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.
'''

my_dict = {}
tv_shows = []

with open("file1.txt", "r") as my_file:
    contents = my_file.readlines()

    for i in range(0, len(contents), 2):
        key = contents[i].strip()
        value = contents[i + 1].strip()
        if key in my_dict:
            pop_items = my_dict.pop(key)
            my_dict[key] = list()
            my_dict[key].append(pop_items)
            my_dict[key].append(value)
            my_dict[key] = "; ".join(my_dict[key])
        else:
            my_dict[key] = value
        tv_shows.append(value)

print(my_dict)
my_dict = sorted(my_dict.items())
tv_shows.sort()

with open("output_keys.txt", "w") as output_file:
    for key, value in my_dict:
        output_file.write("{}: {}\n".format(int(key), value))


with open("output_titles.txt", "w") as title_file:
    for show in tv_shows:
        title_file.write("{}\n".format(show))
