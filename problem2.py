#The "Guess the Number" Game
import random
secret = random.randint(1, 20)
def guess_the_number(secret):
    attempts = 0
    while attempts < 5:
        attempts += 1
        guess = int(input(f"Attempt {attempts}/5. Enter your guess: "))
        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            print("You got it!")
    print(f"Game Over! The number was {secret}")
print("I'm thinking of a number between 1 and 20.")
guess_the_number(10)


    