# Nicole Zheng

# creates the main menu that displays the introduction to the game and instructions
def main_menu():
    print("\nWelcome to the 'Moving Between Rooms' game created by Nicole Zheng.")
    print("Move Commands: North, South, East, West.")
    print("To collect items, enter ‘item’ to collect item in the current room.")
    print("\nWelcome to the town of Pokemon! We encourage fellow Pokemon to go on exciting adventures."
          "\nThe town provided a quest for you to gain experience so that you may be a better version of yourself!"
          "\nQUEST: Go on an adventure to collect all 6 items before fighting the boss villain Meowth.")
    print("\nYou may exit the game by typing 'exit' when a move is requested.")
# this creates a class called move_between_rooms with the three values
def move_between_rooms(current_room, move, rooms):
    current_room = rooms[current_room][move] # assigned var current_room which pulls the current location
    return current_room # return applies the changes made to the var current_room

# a nested dictionary called rooms which lists assignments of the key and values
rooms = {
        'Town': {'West': 'Forest', 'East': 'Caves', 'South': 'Bridge'},
        'Forest': {'North': 'Grasslands', 'East': 'Town', 'Item': 'Zoom Lens'},
        'Grasslands': {'East': 'River', 'South': 'Forest', 'Item': 'Apple'},
        'River': {'East': 'Mountain', 'West': 'Grasslands', 'Item': 'Rocky Helmet'},
        'Mountain': {'West': 'River', 'South': 'Caves', 'Item': 'Reviver Seed'},
        'Caves': {'South': 'Rocky Trenches', 'North': 'Mountain', 'West': 'Town', 'Item': 'Gravelrock'},
        'Rocky Trenches': {'North': 'Caves', 'Item': 'Oran Berry'},
        'Bridge': {'North': 'Town', 'West': 'Final Room: Boss Meowth'},
        'Final Room: Boss Meowth': {'East': 'Bridge'}
    }

# when main is defined, the program can then execute as the starting point. In this case, we start the game here
# when we call main()
def main():
    s = ' '
    inventory = [] # created var to store items collected along the way
    current_room = 'Town' # this sets the starting location as the Great Hall
    main_menu() # calls the main_menu (which was already set up before defining main)

    # Game Loop
    while current_room != 'exit':
        print("\n------------------------------")
        print("\nYou are in the ", current_room)
        print("Available Moves: ", *rooms[current_room]) # the star isolates the moves from the dict format

        # requests user to input their next move
        move = input("Enter move: ")
        if move.capitalize() in rooms[current_room].keys(): # if the input matches the keys in the rooms dict, then...
            current_room = move_between_rooms(current_room, move.capitalize(), rooms)
            # current_room is reassigned which calls out the move_between_rooms class
            continue # this keyword ends current iteration in a for loop or a while loop, then continues next iteration

        # unless user inputs exit
        elif move == 'exit':
            current_room = 'exit' # then current_room reassigns to exit
            print("\nGame ended. Thank you for playing the 'Moving Between Rooms' game!")

        # Input validation
        else:
            print("Invalid input. Try again!") # when user enters a move that does not match the available moves

main()
