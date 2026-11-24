# Chapter 6: Guess the Number Game

import random

print("--- Guess the Number Game ---")
print("I have chosen a number between 1 and 10.")
print("Can you guess it?")

secret_number = random.randint(1, 10)

while True:
    guess = int(input("\nEnter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try agian.")
    else:
        print("Correct! You guessed the number.")
        break
