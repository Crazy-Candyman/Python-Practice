"""
This program takes an input of a refund
amount and returns the exact change in
dollars, quarters, dimes, nickels, and pennies
"""


def exact_change(user_total):
    num_dollars = user_total // 100  # total divided by $1 and assigned to dollars
    user_total %= 100  # total is subtracted by how many $dollars can be deducted
    num_quarters = user_total // 25  # new total is divided and so on....
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total // 1
    user_total %= 1
    # return num of each
    return (
        num_dollars,
        num_quarters,
        num_dimes,
        num_nickels,
        num_pennies,
    )


if __name__ == "__main__":
    input_val = int(input("Enter your refund amount here: "))
    exact_change(input_val)  # call function using input as argument
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(
        input_val
    )

    if input_val < 1:
        print("no change")

    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    elif num_dollars > 1:
        print(f"{num_dollars} dollars")

    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    elif num_quarters > 1:
        print(f"{num_quarters} quarters")

    if num_dimes == 1:
        print(f"{num_dimes} dime")
    elif num_dimes > 1:
        print(f"{num_dimes} dimes")

    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    elif num_nickels > 1:
        print(f"{num_nickels} nickels")

    if num_pennies == 1:
        print(f"{num_pennies} penny")
    elif num_pennies > 1:
        print(f"{num_pennies} pennies")
