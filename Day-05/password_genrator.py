import random

symbols=['!','@','#','$','%','^','&', '*','_']
numbers=['1','2','3','4','5','6','7','8','9','0']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


print("Welcome to Password Generator")
no_letters =int(input("Enter the number of letters you would like to add in password: "))
no_numbers = int(input("Enter the number of numbers you would like to add in password: "))
no_symbols = int(input("Enter the number of symbols you would like to add in password: "))


# Easy Level
password = ""

for i in range(no_letters+1):
    password += random.choice(letters)
for i in range(no_symbols + 1):
    password += random.choice(symbols)
for i in range(no_numbers+1):
    password += random.choice(numbers)

print(f"Your easy level password is: {password}")


# Hard Level

password_list = []
for i in range(0,no_letters):
    password_list.append(random.choice(letters))
for i in range(0,no_symbols ):
    password_list.append(random.choice(symbols))
for i in range(0,no_numbers):
    password_list.append(random.choice(numbers))

password1=""
random.shuffle(password_list)
for i in password_list:
    password1+=i
print(f"Your hard level password is: {password1}")



