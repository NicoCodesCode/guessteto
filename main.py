import random

running = True
difficulties = {
    1: {"name": "easy", "chances": 10},
    2: {"name": "medium", "chances": 5},
    3: {"name": "hard", "chances": 3},
}

while running:
    print("\nWelcome to Guessteto!")
    print("I will think of a number between 1 and 100")
    print("You have a limited amount of chances to guess the correct number")

    print("\nPlease select the difficulty level:")
    print(f"1. Easy ({difficulties[1]["chances"]} chances)")
    print(f"2. Medium ({difficulties[2]["chances"]} chances)")
    print(f"3. Hard ({difficulties[3]["chances"]} chances)")

    difficulty = None
    chances = 0

    while difficulty is None:
        try:
            choice = int(input("\nEnter your choice (1-3): "))

            if choice not in (1, 2, 3):
                raise ValueError

            difficulty = difficulties[choice]["name"]
            chances = difficulties[choice]["chances"]
        except ValueError:
            print("Invalid choice")

    print(f"\nGreat! You have selected the {difficulty} difficulty level")
    print("Let's start the game!")

    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))

            if not 1 <= guess <= 100:
                raise ValueError

            attempts += 1

            if number > guess:
                print(f"Incorrect! The number is greater than {guess}")
            elif number < guess:
                print(f"Incorrect! The number is less than {guess}")
            else:
                break

        except ValueError:
            print("Please enter a number between 1 and 100")

    if guess == number:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts")
    else:
        print(f"You ran out of chances! The correct number was {number}")

    try:
        play_again = int(input("Enter 1 to play again... "))
        if play_again != 1:
            break
    except ValueError:
        break
