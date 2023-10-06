import random

#defining function to read the file with words
def reading_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            words = file.read().split(", ")
            word = random.choice(words)
            return word
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")

#defining function to check if the guess is a valid single letter
def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

#defining function containing loop with the game
def play_word_guessing_game(word, max_attempts):
    
    #creating set to store player guesses
    player_guesses = set()
    
    #creating string to store guessed letters   
    revealed_word = "_" * len(word)

    while max_attempts > 0:
        guess = input("Enter your guess (one letter): ").lower()

        #handling invalid guesses
        if not is_valid_guess(guess):
            print("Invalid guess. Please enter a single letter.")
            continue
            
        #handling repetitions
        if guess in player_guesses:
            print("You've already guessed that letter.")
            continue

        player_guesses.add(guess)

        if guess in word:
            print("Correct guess!")
            
            #changing "_" symbol to guessed letter
            revealed_word = "".join([letter if letter in player_guesses else "_" for letter in word])

            if revealed_word == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess!")
            max_attempts -= 1

        print("Word:", revealed_word)
        print("Attempts left:", max_attempts)
        
        #running out of attempts
        if max_attempts == 0:
            print(f"Out of attempts. The word was: {word}.")
            break

print("Welcome to the word-guessing game!")

#asking user to choose the level of difficulty
level = input("Choose level of difficulty: easy, medium, or hard: ")

#elif statement to choose level of difficulty
if level.lower() == "easy":
    word = reading_file('threeletters.txt')
elif level.lower() == "medium":
    word = reading_file('fourletters.txt')
elif level.lower() == "hard":
    word = reading_file('sevenletters.txt')
else:
    print("Invalid input. Please choose a valid difficulty level.")

print(f"The word has {len(word)} letters.")
print("You have 10 attempts to guess the word.")

#calling the function
play_word_guessing_game(word, 10)


    
    
