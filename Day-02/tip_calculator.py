print ("Welcome to the tip calculator ")
amt = float(input("What is the total amount of the bill : $"))
tip=int(input("select the  percentage of the tip u wanna give 10% , 12% , 15% : "))
people= int(input("Enter the number of people to split the bill : "))
grand_total= amt + (amt*(tip/100))
total = grand_total / people
print(" The amount per person : $",round(total , 2))
