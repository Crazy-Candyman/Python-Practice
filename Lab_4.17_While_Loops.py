# a while loop that repeats until user inputs "quit"
while str != "quit":
    str = input("enter a fruit: ")
    if str != "quit":
        num = int(input("enter a number: "))
        my_str = "Eating {} {} a day keeps the doctor away.".format(num, str)
        print(my_str)
    else:
        break
