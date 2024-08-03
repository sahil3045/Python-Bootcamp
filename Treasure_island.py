print('''    __|\
         .-'    '-.
        / .--, _ a L
      .J (  '-' "'--'
     '-'-.)  .~~~~~~~~~~~~~~~~~~~~.
             |  Treasure Island   |     __
             |                    | ,.-'e ''-'7
             |                    |  '--.    (
             |                    |      ),   \
             '~~~~~~~~~~~~~~~~~~~~'      ` )  :
                                      ,__.'_.'
                                      '-, (
                                  snd   '--'
''')  #arts from ascii.co.uk
print("Welcome to the game Treasure Island!!!")
print("Let's begin!")
print("Your mission is to find the treasure.")
a = input("You're at a crossroad, where do you want to go left or right? ").lower()
if a == "right":
    b = input("You arrive at a sea. There is an island at a distance, do you want to 'wait' for a boat or 'swim' to the island? ").lower()

    if b == "wait":
        print("You arrive at the island safely.")
        c = input("There are 3 doors in front of you. 'Red', 'Blue', 'Green'. Which would you like to enter? ")
        if c == "Red":
            print("Its a room full of fire. Game over.")
        elif c == "Blue":
            print("Its a room full of poisonus animals. Game over.")
        else:
            print("Treasure found. You win!!")

    else: 
        print("A shark ate you while swimming. Game over!")

else:
    print("You fall into a hole. Game over!")



