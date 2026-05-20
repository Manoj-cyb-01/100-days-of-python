weight =int(input("Enter your weight: "))
height = int(input("Enter your height in cm : "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else :
    print("overweight")