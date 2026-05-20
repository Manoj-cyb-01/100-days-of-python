print ("Welcome to the python pizza deliveries")
bill=0
size=input("What size of pizza do you want ? S , M or L : ")
pepperoni=input("Do u want pepperoni on your pizza (y/n) ? : ")
extra_cheese=input("Do u want cheese on your pizza (y/n) ? : ")
# size selection
if size == "S":
    bill=bill+15
elif size == "M":
    bill=bill+20
elif size == "L":
    bill=bill+25
else:
    print ("Invalid entry")
# pepperoni selection
if pepperoni == "y":
    if size == "S":
        bill=bill+2
    else:
        bill=bill+3
# extra cheese selection
if extra_cheese == "y":
    bill=bill+1
print(f"Your final bill is : ${bill} .")
