import tkinter as tk
import random

# Defining the function 
def generate_planet():

    name = name_entry.get() # Extracting the text entered by the user into the name_entry widget

    extraterrestrial_planets = [ # Planet type Data
        "Gas Giant",
        "Ice Giant",
        "Terrestrial Planet",
        "Ocean Planet",
        "Dwarf Planet",
        "Hot Jupiter",
        "Super-Earth",
        "Mini-Neptune",
        "Tatooine-like Planet",
        "Iron Planet",
        "Dark Eden",
        "Exomoon"
    ]

    star_types = [ # Star type data
        "Red Dwarf",
        "Yellow Dwarf (like our Sun)",
        "Blue Giant",
        "White Dwarf",
        "Supergiant",
        "Main Sequence Star",
        "Brown Dwarf",
        "Binary Star",
        "Neutron Star",
        "Black Hole"
    ]

    choice_type = random.choice(extraterrestrial_planets) # Random planet type
    distance = random.randint(4, 1000000000) # Random distance in light years
    star_type = random.choice(star_types) # Random star type

    # If statement to choose mass according to the planet type 

    if choice_type in ["Gas Giant", "Hot Jupiter", "Ice Giant"]:
        mass = random.randint(10, 1000)
    elif choice_type in ["Terrestrial Planet", "Ocean Planet", "Super-Earth", "Tatooine-like Planet", "Iron Planet", "Dark Eden"]:
        mass = round(random.uniform(0.8, 8), 2)
    elif choice_type in ["Dwarf Planet", "Exomoon"]:
        mass = round(random.uniform(0.001, 0.01), 5)
    else:
        mass = round(random.uniform(9, 13), 2)

    # Result text displayed in the window
    result_text = (
        f"Planet {name.capitalize()} is {distance} ly away from the Solar System. It's a {choice_type}.\n"
        f"Mass: {mass} of Earth's.\n"
        f"This planet orbits around a {star_type}."
    )

    result_label.config(text=result_text)

# Creating the main window
root = tk.Tk()
root.title("Planet Generator")
root.geometry("500x200")


# Creating and place widgets
label_name = tk.Label(root, text="Enter planet name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

# Creating a planet name entry
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Creating generate button allowing to start the function
generate_button = tk.Button(root, text="Generate Planet", command=generate_planet)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Text with the result
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()