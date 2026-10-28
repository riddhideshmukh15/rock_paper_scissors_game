
import random


choices = ["rock", "paper", "scissors"]


user_score = 0
computer_score = 0
ties = 0

print("Welcome to Rock, Paper, Scissors!")


while True:
    # User choice
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a Tie!")
        ties += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    
    print("\n------ SCOREBOARD ------")
    print("Your Wins:", user_score)
    print("Computer Wins:", computer_score)
    print("Ties:", ties)
    print("------------------------")

    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===== FINAL SCORE =====")
        print("Your Wins:", user_score)
        print("Computer Wins:", computer_score)
        print("Ties:", ties)
        print("\nThanks for playing!")
        break

    print()
