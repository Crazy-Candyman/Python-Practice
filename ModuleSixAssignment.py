# Gabriel Nina (Gabe)

list_of_directions = ["North", "East", "West", "South"]
rooms = {
    "Great Hall": {"South": "Bedroom"},
    "Bedroom": {"North": "Great Hall", "East": "Cellar"},
    "Cellar": {"West": "Bedroom"},
}

new_room = "Great Hall"
current_room = new_room # Great Hall starting room.
exit_room = "Exit"

print(
    "\nThe commands to move from one room to another are:\n"
    "'go north', 'go east', 'go south', 'go west'\n"
    "If you would like to exit the game, type 'Exit'"
)

while True:  # Infinite while loop.
    print("\nYou are currently in the {}".format(current_room))
    move = input("Enter your move: ").title().split()  # User input
    try:
        if "Go" in move[0]:
            if move[1] in list_of_directions:
                if move[1] in rooms[current_room].keys():  # if direction is valid.
                    new_room = rooms[current_room][move[1]]  # assigned new_room.
                    current_room = new_room  # current_room is equal to new_room.
                else:
                    print("Sorry, you can't go that way.\n")
            else:
                print("\nInvalid Input")
        elif "Exit" in move:
            current_room = exit_room  # Current room = "Exit".
        else:
            print("\nInvalid Input")
    except IndexError:
        print("\nInvalid Input")

    # Options presented to player if current room = "Exit".
    while current_room == exit_room:
        print(
            "\nIf you would like to leave the game then enter 'q'\n"
            "If you would like to continue this adventure then enter 'c'"
        )
        move = input("\nWhat would you wish to do?").lower()
        if move == "q":
            break  # End while loop
        elif move == "c":
            current_room = new_room  # Current room re-assigned previous room.
            break
        else:
            print("\nNot a valid input")

    # Game will end here if current room still "Exit".
    if current_room == exit_room:
        break

print("\nThanks for playing!")
