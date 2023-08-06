import random

def roll_dice(start, stop):
    return random.randint(start, stop)

while True:
    dice_start = int(input('Type the number you want your dice to start with: '))
    dice_stop = int(input('Type the number you want your dice to stop with: '))

    result = roll_dice(dice_start, dice_stop)
    print(f"You rolled: {result}")
    play_again = input("Do you want to roll again? (yes/no): ").lower()
    if play_again not in ('yes', 'yeah', 'y', '1'):
        print("Thanks for playing! Goodbye!")
        break
