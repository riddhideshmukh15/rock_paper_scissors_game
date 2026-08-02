import random

# List of choices
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("-----------------------------------")

while True:
    # User choice
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please try again.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")

    else:
        print("💻 Computer Wins!")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        break

    print()