import random

def guess_number():
    """
    It's a simple guess the numbers game
    """
    number = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print("Correct")
                break
        except ValueError:
            print("Incorrect value")

guess_number()

