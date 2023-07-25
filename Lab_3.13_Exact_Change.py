change = int(input())

dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

if change == 0:
    print("No change")

dollars = change // 100
if dollars > 0:
    change = change - (dollars * 100)
if dollars == 1:
    print(f"{dollars} Dollar")
elif dollars > 1:
    print(f"{dollars} Dollars")

quarters = change // 25
if quarters > 0:
    change = change - (quarters * 25)
if quarters == 1:
    print(f"{quarters} Quarter")
elif quarters > 1:
    print(f"{quarters} Quarters")

dimes = change // 10
if dimes > 0:
    change = change - (dimes * 10)
if dimes == 1:
    print(f"{dimes} Dime")
elif dimes > 1:
    print(f"{dimes} Dimes")


nickels = change // 5
if nickels > 0:
    change = change - (nickels * 5)
if nickels == 1:
    print(f"{nickels} Nickel")
elif nickels > 1:
    print(f"{nickels} Nickels")


pennies = change // 1
if pennies > 0:
    change = change - (pennies * 1)
if pennies == 1:
    print(f"{pennies} Penny")
elif pennies > 1:
    print(f"{pennies} Pennies")
