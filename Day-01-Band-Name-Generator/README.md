# Day 01 – Band Name Generator 🎸

## Overview

This is a simple Python project built on **Day 1** of the *100 Days of Code: Python Bootcamp*.
The program generates a band name based on user input.

The user is asked for:

* The name of the city they grew up in
* Their pet's name

The program then combines these two inputs to create a band name.

---

## How It Works

1. The program welcomes the user.
2. It asks for the city where the user grew up.
3. It asks for the user's pet name.
4. It combines both inputs and generates a band name.

Example:

```
Welcome to the Band Name Generator
What's the name of the city you grew up in? London
What's your pet's name? Bruno

Your band name could be: London Bruno Band
```

---

## Python Concepts Used

* `print()` function
* `input()` function
* Variables
* String concatenation

---

## Source Code

```python
print("Welcome to the Band Name Generator...")

city = input("What's the name of the city you grew up in: ")
pet_name = input("What's your pet's name: ")

print(city + " " + pet_name + " Band")
```

---

## Learning Outcome

This project demonstrates the basic fundamentals of Python programming including user input, variables, and string manipulation.

