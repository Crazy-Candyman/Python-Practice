""" This program swaps two inputs in
receiving order using the return method."""


def swap_values(user_val1, user_val2):  # function defined
    return user_val2, user_val1  # return with values swapped


if __name__ == "__main__":
    """Type your code here. Your code must call the function."""

    val1 = input()
    val2 = input()
    swap_values(val1, val2)  # called function
    x, y = swap_values(val1, val2)  # unpacked returns
    print(x, y)
