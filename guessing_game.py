import random

def number_guessing_game():

    secret_number = random.randint(1, 100)

    print ("Welcome to the number Guessing Game!")
    print("Guess a number between 1 and 100")

    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
         
        attempts += 1
        
        if guess ==secret_number:
           print(f"Congratualtions! You've guesed the number{secret_number} correctly!")
           print(f"It took you {attempts} attempts to guess.")
           break
        elif guess > secret_number:
           print("Too high! Try again.")
        else:
           print("Too low! Try again!")






      