from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

#function to check user guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("That is too high, try again! ")
        return turns - 1
    elif user_guess < actual_answer:
        print("That is too low, try again! ")
        return turns - 1
    else:
        print(f"You are correct! The answer was {actual_answer}!")


#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #let user guess number
        guess = int(input("Guess a number between 1 and 100: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses. You lose")
            return

game()