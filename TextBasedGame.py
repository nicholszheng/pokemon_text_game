# Nicole Zheng
#IT-140 Intro to Scripting

# creates the main menu that displays the introduction to the game and instructions
def main_menu():
    print("\nWelcome to the 'Moving Between Rooms' game created by Nicole Zheng."
          "\nMove Commands: North, South, East, West."
          "\nTo collect items, enter ‘item’ to collect item in the current room."
          "\n\nWelcome to the town of Pokemon! We encourage fellow Pokemon to go on exciting adventures."
          "\nThe town provided a quest for you to gain experience so that you may be a better version of yourself!"
          "\n\nQUEST: Go on an adventure to collect all 6 items before fighting the boss villain Meowth."
          "\nYou may exit the game by typing 'exit' when a move is requested.")


# this creates a class called move_between_rooms with the three values
def move_between_rooms(current_room, move, rooms):
    current_room = rooms[current_room][move]  # assigned var current_room which pulls the current location
    return current_room  # return applies the changes made to the var current_room


def get_item(current_room, move, rooms, inventory):
    # adding items to inventory and removing it from current room
    inventory.append(rooms[current_room]['Item'])  # adds item into inventory
    del rooms[current_room][
        'Item']  # when item is added into inventory, the same item is now deleted from the current room


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

        # for when user arrives at the villain location
        if current_room == 'Final Room: Boss Meowth':
            # winning the battle
            if move.capitalize() == 'West' and len(inventory) == 6:  # user can enter boss location if met requirements
                print(\n"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Final Dialogue~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                print(
                    "\nYou entered the room that appeared to be empty, you looked around to see what is left behind."
                    "\nBefore you could turn around, you hear a “MEOWTH~”")

                print("\n\nYou’ve been clawed from the back. Immediately, you jump back and pulled out the Oran Berry"
                      "\nyou’ve found on the way here. "
                      "\nYou pop the berry in your mouth and your injuries heals quickly.")

                print("\n\nMeowth slowly approaches you with a big smirk and confidently says, I’m going to steal you "
                      "\nand make Team Rocket prou-MEOWTH!' The boss was hit in the eye by the gravelrock you tossed.")

                print("\n\n'Why… you…’ Meowth angrily lowers his voice with his left eye shut."
                      "\nHe lunges forward with his paw, which you dodge easily. "
                      "\nYou’ve gathered enough energy to release your strong ability, Thunderbolt. "
                      "\nThe thunder crackles down from the sky and shocks Meowth. He falls to the ground unconscious.")

                print("\n\nYou sigh and look around what else may be around the room before you leave."
                      "\nYou just remembered that you have a Reviver Seed that can revive Meowth back to life, "
                      "\nso you do just that. You walk away feeling stronger and confident in yourself.")

                print("\n\n\nCongratulations! You’ve completed the Town’s quest to defeat the villain!"
                      "\nThanks for playing! Hope you enjoyed this mini text game!")
                break

            elif move.capitalize() == 'West' and len(inventory) != 6:  # user respawns when requirements aren't met
                print("\nYou are halfway on the bridge when it starts rumbling. "
                      "\nYou notice the planks under you start cracking and before you could act,"
                      "\nyou lose your balance and fall through the bridge. Pidgeotto swoops in to catch you"
                      "\nbefore you reach the depths of darkness below you. \n\n“Ca-Caw! That was close!” "
                      "the flying pokemon comments as he heads back to town safely."
                      "\n\nYou make it safely back to the beginning of the bridge. Maybe some more items could help.")

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RESPAWNED~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                move = 'East' #this pushes the user from the boss location back to the Bridge location
                current_room = move_between_rooms(current_room, move.capitalize(), rooms)
                # current room is readjusted to allow user to respawn instead of starting over

        print("\n------------------------------")
        print("\nYou are in the ", current_room)
        print("Current Inventory: ", *inventory)  # the star isolates the inventory from the dict format
        print("\nAvailable Moves: ", *rooms[current_room])  # the star isolates the moves from the dict format

        # tells user if they see an item in the location
        if 'Item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['Item']))
            print("---------------------------------------------")

        # requests user to input their next move
        move = input("Enter move: ")
        if move.capitalize() != 'Item' and move.capitalize() in rooms[
            current_room].keys():  # if the input matches the keys in the rooms dict, then...
            current_room = move_between_rooms(current_room, move.capitalize(), rooms)
            # current_room is reassigned which calls out the move_between_rooms class
            continue  # this keyword ends current iteration in a for loop or a while loop, then continues next iteration

        # collecting items and adding inventory
        elif move.capitalize() == 'Item':
            print("You picked up the {}".format(rooms[current_room]['Item']))
            get_item(current_room, move, rooms, inventory)

        # unless user inputs exit
        elif move.capitalize() == 'Exit':
            current_room = 'exit'  # then current_room reassigns to exit
            print("\nGame ended. Thank you for playing the 'Moving Between Rooms' game!")


        # Input validation
        else:
            print("Invalid input. Try again!")  # when user enters a move that does not match the available moves


main() # this actually calls to run the game
