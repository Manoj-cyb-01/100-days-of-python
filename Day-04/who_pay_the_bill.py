import random
friends =["alice", "bob", "charlie", "dave", "eve"]
print(f"{random.choice(friends)} has to pay the bill.")
### or ####
print(f"{friends[random.randint(0,len(friends)-1)]} has to pay the bill")
