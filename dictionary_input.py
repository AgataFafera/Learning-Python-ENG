def fun_dict():
    menu = '''If you want to add more keys and values, type ADD.
    If you want to see your new dictionary, type SEE. 
    If you want to end, type EXIT.'''
    print(menu)

    dict_input = {}
    
    while True: 
        start = input("What do you want to do? ")
    
        if start.lower() == 'add':
            key_input = input("Type your key: ")
            value_input = input("Type your value: ")
            dict_input[key_input] = value_input

        
        elif start.lower() == 'see':
            swapped_dict = {value: key for key, value in dict_input.items()}
            print(swapped_dict)

        elif start.lower() == 'exit':
            print("Goodbye!")
            break
        
        else: 
            print("Invalid input. Try again.")

fun_dict()
