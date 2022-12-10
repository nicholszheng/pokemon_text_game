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
    current_room = rooms[current_room][move]  # assigned var current_room which pulls the current location
    return current_room  # return applies the changes made to the var current_room


def get_item(current_room, move, rooms, inventory):
    # adding items to inventory and removing it from current room
    inventory.append(rooms[current_room]['Item'])
    del rooms[current_room]['Item']

# when main is defined, the program can then execute as the starting point. In this case, we start the game here
# when we call main()
def main():

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

    s = ' '
    inventory = []  # created var to store items collected along the way
    current_room = 'Town'  # this sets the starting location as the Great Hall
    main_menu()  # calls the main_menu (which was already set up before defining main)

    # Game Loop

    while current_room != 'exit':
        print("\n------------------------------")
        print("\nYou are in the ", current_room)
        print("Available Moves: ", *rooms[current_room])  # the star isolates the moves from the dict format

        # requests user to input their next move
        move = input("Enter move: ")
        if move.capitalize() in rooms[current_room].keys():  # if the input matches the keys in the rooms dict, then...
            current_room = move_between_rooms(current_room, move.capitalize(), rooms)
            # current_room is reassigned which calls out the move_between_rooms class
            continue  # this keyword ends current iteration in a for loop or a while loop, then continues next iteration

        # unless user inputs exit
        elif move == 'exit':
            current_room = 'exit'  # then current_room reassigns to exit
            print("\nGame ended. Thank you for playing the 'Moving Between Rooms' game!")

        # Input validation
        else:
            print("Invalid input. Try again!")  # when user enters a move that does not match the available moves

        # collecting items and adding inventory
        if len(move) == 4 and move[0] == 'Get' and s.join(move[1:3]) in rooms[current_room]['Item']:
            print("You picked up the {}".format(rooms[current_room]['Item']))
            print('---------------------------------------')
            get_item(current_room, move, rooms, inventory)

        # tells user if they see an item in the location
        if current_room != 'Final Room: Boss Meowth' and 'Item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['Item']))
            print("---------------------------------------------")

    while True:
        # for when user arrives at the villain location
        if current_room == 'Final Room: Boss Meowth':
            # winning the battle
            if len(inventory) == 6:
                print("You entered the room that appeared to be empty, you looked around to see what is left behind."
                      "\nBefore you could turn around, you hear a “MEOWTH~”")

                print("You’ve been clawed from the back. Immediately, you jump back and pulled out the Oran Berry"
                      "you’ve found on the way here. "
                      "\nYou pop the berry in your mouth and your injuries heals quickly.")

                print("Meowth slowly approaches you with a big smirk and confidently says, I’m going to steal you "
                      "and make Team Rocket prou-MEOWTH!' The boss was hit in the eye by the gravelrock you tossed.")

                print("'Why… you…’ Meowth angrily lowers his voice with his left eye shut. "
                      "He lunges forward with his paw, which you dodge easily. "
                      "You’ve gathered enough energy to release your strong ability, Thunderbolt. "
                      "The thunder crackles down from the sky and shocks Meowth. He falls to the ground unconscious.")

                print("You sigh and look around what else may be around the room before you leave."
                      "You just remembered that you have a Reviver Seed that can revive Meowth back to life, "
                      "so you do just that. You walk away feeling stronger and confident in yourself.")

                print("Congratulations! You’ve completed the Town’s quest to defeat the villain!\n"
                      "Thanks for playing! Hope you enjoyed this mini text game!")

            else:
                # respawning (because you didn't collect all six)
                print("You are halfway on the bridge when it starts rumbling. "
                      "You notice the planks under you start cracking and before you could act, "
                      "you lose your balance and fall through the bridge. Pidgeotto swoops in to catch you "
                      "before you reach the depths of darkness below you. “Ca-Caw! That was close!” "
                      "the flying pokemon comments as he heads back to town safely. "
                      "You make it safely back to the beginning of the bridge. Maybe some more items could help.")

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RESPAWNED~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        break

main()
