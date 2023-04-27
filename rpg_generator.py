import random
import time

name = input("Input a name of your character: ")
gender = input("Input a gender of your character (female, male, non-binary): ").lower()
if gender in ['male', 'female', 'non-binary']:
    print('Thanks, character generation in progress')
else:
    print('Invalid gender')
    exit()

time.sleep(3)

races = ["human", "elf", "dwarf", "orc", "demon", "goblin"]
classes = ["warrior", "assassin", "mage", "hunter", "priest", "bard"]
hair_color = ["brown", "black", "red", "blond", "green", "white", "grey", "yellow", "violet"]
eye_color = ["black", "red", "blue", "brown", "green", "grey", "yellow", "violet"]
special_features = ["a face scar", "lack of one ear", "cross-eyes", "six fingers"]
attributes = ["charisma", "strength", "intelligence", "magic abilities"]


def traits(races, classes, hair_color, eye_color, special_features):
    race = random.choice(races)
    c_class = random.choice(classes)
    h_c = random.choice(hair_color)
    e_c = random.choice(eye_color)
    s_f = random.choice(special_features)
    character = {
        "race": race,
        "class": c_class,
        "hair color": h_c,
        "eye color": e_c,
        "special features": s_f
    }
    print('Your character features:')
    return character


# print(traits(races, classes, hair_color, eye_color, special_features))

print("You have points to assign to strength, charisma, intelligence, and magic abilities.")
points = 35
strength = 0
charisma = 0
intelligence = 0
magic_abilities = 0

while True:
    print("You have", points, "points left.")
    print("""
    1-add points
    2-take points
    3-see points per attribute
    4-exit
    """)
    choice = input("choice: ")
    if choice == "1":
        attribute = input("which attribute? strength, charisma, intelligence, or magic abilities? ")
        if attribute in attributes:
            add = int(input("how many points? "))
            if add <= points and add > 0:
                if attribute == "strength":
                    strength += add
                    print(name, "now has", strength, "strength points.")
                elif attribute == "charisma":
                    charisma += add
                    print(name, "now has", charisma, "charisma points.")
                elif attribute == "intelligence":
                    intelligence += add
                    print(name, "now has", intelligence, "intelligence points.")
                elif attribute == "magic abilities":
                    magic_abilities += add
                    print(name, "now has", magic_abilities, "magic abilities points.")
                points -= add
            else:
                print("invalid number of points.")
        else:
            print("invalid attribute.")
    elif choice == "2":
        attribute = input("which attribute? strength, charisma, intelligence, or magic abilities? ")
        if attribute in attributes:
            take = int(input("how many points? "))
            if attribute == "strength" and take <= strength and take > 0:
                strength -= take
                print(name, "now has", strength, "strength points.")
                points += take
            elif attribute == "charisma" and take <= charisma and take > 0:
                charisma -= take
                print(name, "now has", charisma, "charisma points.")
                points += take
            elif attribute == "intelligence" and take <= intelligence and take > 0:
                intelligence -= take
                print(name, "now has", intelligence, "intelligence points.")
                points += take
            elif attribute == "magic abilities" and take <= magic_abilities and take > 0:
                magic_abilities -= take
                print(name, "now has", magic_abilities, "magic abilities points.")
                points += take
            else:
                print("invalid number of points.")
        else:
            print("invalid attribute.")

    elif choice == "3":
        print("strength -", strength)
        print("charisma -", charisma)
        print("intelligence -", intelligence)
        print("magic abilities -", magic_abilities)

    elif choice == "4":
        if points == 0:
            break
        else:
            print("use all your points!")
    else:
        print("invalid choice.")

print("congrats! you're done designing " + name + '.')
print(traits(races, classes, hair_color, eye_color, special_features))
print(name, "has", strength, "strength points,", charisma, "charisma points,", intelligence, "intelligence points, and",
      magic_abilities, "magic abilities points.") 