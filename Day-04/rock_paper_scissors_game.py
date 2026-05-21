import random
images=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
print("What do u choose?")
user_choice = int(input("type '0' for rock, '1' for paper or '2' for scissors: "
                    "Enter your choice: "))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice")
    exit()
else:
    if user_choice == 0:
        print(images[user_choice])
    if user_choice == 1:
        print(images[user_choice])
    if user_choice == 2:
        print(images[user_choice])
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(images[computer_choice])
if computer_choice == 1:
    print(images[computer_choice])
if computer_choice == 2:
    print(images[computer_choice])
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == "0" and computer_choice == 2:
    print("You win")
elif user_choice == "1" and computer_choice == 0:
    print("You win")
elif user_choice == "2" and computer_choice == 1:
    print("You win")
else:
    print("You lose")

