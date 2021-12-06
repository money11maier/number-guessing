# Number Guessing Game

import random

def game_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    else:
        return  5

def guess_comparison(guess, number, attempts):
    if guess == number:
        print(f"You're correct! The number was {number}")
        return -10 
    elif guess > number:
        print(f"Too high.")
        return -1
    else:
        print(f"Too low.")
        return -1
        
def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = game_difficulty(difficulty)
    chosen_number = random.randint(1, 100)
    #print(chosen_number)
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_guess = int(input("What is your guess: "))
        attempts += guess_comparison(user_guess, chosen_number, attempts)
    if attempts == 0 and user_guess != chosen_number:
            print(f"The number was {chosen_number}. You lose!")

guessing_game()














