
import random

dice = {
    1 : """
┌─────────┐
│         │
│    ●    │
│         │
└─────────┘
""",
    2 : """
┌─────────┐
│  ●      │
│         │
│      ●  │
└─────────┘
""",
    3 : """
┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘
""",
    4 : """
┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘
""",
    5 : """
┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘
""",
    6 : """
┌─────────┐
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
└─────────┘
"""
}

user = "y"

while user == "y":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print(f"You rolled: {die1} and {die2}")

    print(dice[die1])
    print(dice[die2])

    user = input("Press 'y' to roll again or no to quit: ").lower()
    if user == "no".lower():
        print("thanks for playing")
        break