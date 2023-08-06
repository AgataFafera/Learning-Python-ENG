import random

print("Welcome to the game Guess the Number. You have maximum 5 attempts.")

max_num = int(input("Choose a maximum number in your game: "))
right_num = random.randint(1, max_num)

attempts = 0  

while attempts < 5:  
    guess = int(input("What's your guess? "))
    
    if guess == right_num: 
        print("Congrats! This is the right number.")
        break
    else: 
        print("Try again.")
        if guess > right_num: 
            print("It's too much!")
        elif guess < right_num: 
            print("It's not enough!")
        attempts += 1  

if attempts == 5:  
    print("Sorry, you've used all your attempts. The correct number was:", right_num)
