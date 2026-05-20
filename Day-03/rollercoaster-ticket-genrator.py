print("Welcome to the rollercoaster")
height= int(input("What is your height in cm ? : "))
total_payment=0
age= int(input("What is your age ? : "))
if height >=120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Your are eligible for child ticket cost $5")
        total_payment = total_payment + 5
    elif age <= 18:
        print("Your are eligible for youth ticket cost $7")
        total_payment = total_payment + 7
    else:
        print("Your are eligible for adult ticket cost $12")
        total_payment = total_payment + 12
    photo_choice = input("Do you want a photo taken? (y/n): ")
    if photo_choice == "y":
        print("Please pay $3 for the photo")
        total_payment = total_payment + 3
    print(f"Your total payment is ${total_payment}")
else:
    print("Sorry you are not eligible to ride the rollercoaster")