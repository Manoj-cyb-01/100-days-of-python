print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1=input("You are at a cross road. Where do you want to go ? Type 'left' or 'right' : ").lower()
if choice1=='left':
    choice2= input("You've come to the lake . there is a island in the middle of the lake ."
                   "Type 'wait' to wait for a boat. Type 'swim' to swim across : ").lower()
    if choice2=='wait':
        choice3=input("You reached the island safely"
              "there  are three doors.one red ,one yellow and one blue . which color do u choose ?").lower()
        if choice3=='red':
            print("It's a room full of fire . Game over.....!")
        elif choice3=='yellow':
            print("You found the Treasure . You Win.....!")
        elif choice3=='blue':
            print("You enter the room of beasts . Game over....!")
    else:
        print("You got attacked by crocodile . Game over....! ")
else:
    print("you fell in to the hole . Game Over....! ")
