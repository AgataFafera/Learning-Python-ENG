import random

# List of prefixes
prefixes = ['Aer', 'Bran', 'Cyra', 'Dael', 
            'Elys', 'Fael', 'Gwyn', 'Hyra', 'Ith', 'Jor', 'Kael', 
            'Luna', 'Myth', 'Nyx', 'Orin', 'Pry', 'Quin', 'Rav', 'Syl', 
            'Tyra', 'Vyr', 'Wyn', 'Xan', 'Yara', 'Zephyr', 'Ea', 'Gal', 'Har', 
            'Ithil', 'Kor', 'Lyra', 'Mel', 'Nim', 'Ori', 'Pha', 'Rin', 'Sol', 'Thal', 'Vael', 'Xyl', 'Zar']

# List of suffixes
suffixes = ['a', 'ara', 'en', 'ia', 'in', 'is', 'ith', 'ora', 'us', 'wyn', 'yx', 
            'ara', 'el', 'ia', 'il', 'ion', 'or', 'ara', 'is', 'ith', 'on', 'orin', 'ys']

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List of consonants
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def fantasy_name():
    name = ''
    while True:
        choice = input('''What do you want to add to your name?
                            Prefix (type 1)
                            Suffix (type 2)
                            Vowel (type 3)
                            Consonant (type 4)
                            End (type 5): ''')
        if choice == '1':
            name += random.choice(prefixes)  # Add a random prefix to the name
            print(name.title())  # Print the name with the first letter capitalized
        elif choice == '2':
            name += random.choice(suffixes)  # Add a random suffix to the name
            print(name.title())  # Print the name with the first letter capitalized
        elif choice == '3':
            name += random.choice(vowels)  # Add a random vowel to the name
            print(name.title())  # Print the name with the first letter capitalized
        elif choice == '4':
            name += random.choice(consonants)  # Add a random consonant to the name
            print(name.title())  # Print the name with the first letter capitalized
        elif choice == '5':
            break  # Exit the loop if '5' is selected
        else:
            print('Invalid input')  # Print an error message for invalid choices
    print(f'Your final name: {name.title()}')  # Print the final name with the first letter capitalized

fantasy_name()  # Call the function to generate a fantasy name
