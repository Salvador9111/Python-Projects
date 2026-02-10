import random
# Rock Paper Scissor
def play_game():
    while True:
        user = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

        if user == 'quit':
            print("Thanks for playing!")
            break

        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

play_game()