import random

print("🎮 Welcome to Rock, Paper, Scissors!")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\nChoose rock, paper, or scissors")
    user = input("Your choice: ").lower()

    if user not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Game logic
    if user == computer:
        print("🤝 It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("✅ You win!")
        user_score += 1

    else:
        print("❌ You lose!")
        computer_score += 1

    # Score display
    print(f"Score → You: {user_score} | Computer: {computer_score}")

    # Play again
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break
