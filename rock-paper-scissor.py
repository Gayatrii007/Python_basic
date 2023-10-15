import random

# Initialize scores
user_score = 0
computer_score = 0

# Game loop
while True:
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose one: rock, paper, scissors")

    # Get user's choice
    user_choice = input("Your choice: ").lower()

    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Generate a random choice for the computer
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Display user and computer choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    print(result)

    # Display the current scores
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
