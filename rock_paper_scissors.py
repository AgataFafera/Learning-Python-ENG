import random

#list with possible figures
figures = ["Rock", "Paper", "Scissors"]

#variable to sum the score
user_score = 0
program_score = 0

#starting and stopping the game
print("Welcome to the rock-paper-scissors game. ")

while True:
    try:
        #user's choice
        choice_user = input("Type 'rock', 'paper', 'scissors' or 'game finish': ")

        #program's choice
        choice_program = random.choice(figures)

        #check if the user's choice is valid
        options = ["Rock", "Paper", "Scissors", "Game Finish"]
        if choice_user.lower() not in [figure.lower() for figure in options]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        #tie variant
        elif choice_user.lower() == choice_program.lower():
                print(f"{choice_program}. Tie!")

        #user's win variant
        elif (
            (choice_user.lower() == "paper" and choice_program.lower() == "rock")
            or (choice_user.lower() == "rock" and choice_program.lower() == "scissors")
            or (choice_user.lower() == "scissors" and choice_program.lower() == "paper")
            ):
            print(f"{choice_program}. You won!")
            user_score += 1

        #game finish variant - showing the score and closing the program   
        elif choice_user.lower() == "game finish":

            if program_score > user_score: #program has more points
                print(f"You lost the game! Your score: {user_score}. Computer's score: {program_score}.")
                break

            elif program_score < user_score: #user has more points
                print(f"You won the game! Your score: {user_score}. Computer's score: {program_score}.")
                break

            else: #tie in points
                print(f"Tie! Your score: {user_score}. Computer's score: {program_score}.")
                break

        #program's win variant
        else:
            print(f"{choice_program}. You lost!")
            program_score += 1

    except ValueError:
        print("Invalid data. Please enter a valid input.")
