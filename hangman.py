import random

def choose_word():
    words = ['lion','elephant','tiger','giraffe','zebra','monkey','cheetah','hippotamus']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in guessed_letters:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters =[]
    attempts = 6

    while True:
        print("\nAttempts left:" ,attempts)
        print("Words", display_word(secret_word, guessed_letters))
        guess = input("Guess a letter:").lower()

        if guess in guessed_letters:
            print("You've guseed that letter!")
            continue
        
        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess!")
            if attempts == 0:
                print("game over! the word was:", secret_word)
                break
        else:
            print("Correct guess!")
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulation! You correctly guessed the word:", secret_word)
            break


        print("Guseed letters:", guessed_letters)

if __name__ == "__main__":
    hangman()

