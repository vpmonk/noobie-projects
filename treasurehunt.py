print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

direction = input("You're at a crossroad. Where do you want to go? Type 'LEFT' or 'RIGHT': ").lower()

if direction == 'left':
    action = input("You came to a lake. There is an island in the middle of the lake. Type 'WAIT' to wait for a boat or 'SWIM' to swim across: ").upper()

    if action == 'WAIT':
        door = input("You successfully waited for a boat. You reach the island safely. NOW YOU FIND TWO DOORS 'YELLOW' AND 'RED': ").lower()
        if door == 'red':
            print("Demon slayer just killed you! Game over.")
        elif door == 'yellow':
            print('you found treasure')
            print(r"""
          ____...------------...____
       _.-"` /o/__ ____ __ __  __ \o\_`"-._
     .'     / /                    \ \     '.
     |=====/o/======================\o\=====|
     |____/_/________..____..________\_\____|
     /   _/ \_     <_o#\__/#o_>     _/ \_   \
     \_________\####/_________/
      |===\!/========================\!/===|
      |   |=|          .---.         |=|   |
      |===|o|=========/     \========|o|===|
      |   | |         \() ()/        | |   |
      |===|o|======{'-.) A (.-'}=====|o|===|
      | __/ \__     '-.\uuu/.-'    __/ \__ |
      |==== .'.'^'.'.====|
   |  _\o/   __  {.' __  '.} _   _\o/  _|
      `""""-""""""""""""""""""""""""""-""""` ")
        """)
        else:
            print("Invalid input. Game over!")

    elif action == 'SWIM':
        print("You decided to swim across the lake.")
        print("Uh-oh! There were piranhas in the lake. You got bitten. Game over!")
    else:
        print("Invalid input. Game over!")

elif direction == 'right':
    print("You fell into a hole. Game over!")
    print("Play again, dude.")
else:
    print("Invalid input. Game over!")
