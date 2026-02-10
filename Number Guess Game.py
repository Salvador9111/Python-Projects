import random
# Number Guessing Game
Comp = random.randint(1, 10)
count = 0
while True:
    user = int(input("Enter number (1-10): "))
    count += 1
    if user < Comp:
        print("Higher number please")
    elif user > Comp:
        print("Lower number please")
    else:
        print(f"Congratulations! You guessed it in {count} attempts.")
        break