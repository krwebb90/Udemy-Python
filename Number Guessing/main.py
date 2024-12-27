from art import logo
import random

print(logo)
print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

def guess_number():
    answer = random.randint(1, 100)
    difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ")
    number_of_guesses = 0
    if difficulty == "hard":
        number_of_guesses += 5
    else:
        number_of_guesses += 10
    print(f"You have {number_of_guesses} guesses.")
    while number_of_guesses > 0:
        user_guess = int(input("Guess a number: "))
        if user_guess < 0 or user_guess > 100:
            print("Sorry, guess between 1 and 100.")
        elif user_guess > answer:
            print(f"That is incorrect. The number is lower.")
            number_of_guesses -= 1
            print(f"You have {number_of_guesses} guesses left.")
        elif user_guess < answer:
            print(f"That is incorrect. The number is higher.")
            number_of_guesses -= 1
            print(f"You have {number_of_guesses} guesses left.")
        else:
            print(f"You guessed correctly! The number was {user_guess}.")
            break

guess_number()