import random

def number_guessing_game():
    print("🎮 Welcome to 'Where Data Meets Intelligence'!")
    print("I'm thinking of a number between 1 and 20.")
    print("You have 5 chances to guess it right.\n")

    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess → "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s). Great job!")
            break
        elif guess < secret_number:
            print("📉 Too low! Try a higher number.\n")
        else:
            print("📈 Too high! Try a lower number.\n")

    if attempts == max_attempts and guess != secret_number:
        print(f"\n😢 Out of attempts! The number was {secret_number}. Better luck next time!")

# Run the game
number_guessing_game()
