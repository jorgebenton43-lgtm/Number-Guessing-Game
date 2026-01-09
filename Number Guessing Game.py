import random

min_number = 1
max_number = 1000
max_attempts = 10

secret_number = random.randint(min_number, max_number)

def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a Number between {min_number} to {max_number}: "))
            if min_number <= guess <= max_number: 
                return guess
            else:
                print("invalid input please select a different number.")
        except ValueError:
            print("Invalid Number Please select a different number.")
def check_guess(guess, secret_number): 
    if guess == secret_number:
        return "correct"
    elif guess < secret_number: 
        return "too low"
    else: 
        return "too high"
def play_game():
    attempts = 0 
    won = False 

    while attempts < max_attempts: 
        attempts += 1 
        guess = get_guess()
        results = check_guess(guess, secret_number)

        if results == "correct":
            print(f"You win, You guessed {results}")
        else: 
            print(f"{results} try again")
    if not won: 
        print("You ran out of attempts.")

if __name__ == "__main__":
    print("welcome to the guessing game")
    play_game()