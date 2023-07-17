def sort_lists():
    menu = '''If you want to add objects to first list, type ADD1.
    If you want to add objects to second list, type ADD2. 
    If you want to see the merged list, type SEE.
    If you want to end, type EXIT.'''
    print(menu)

    list_one = []
    list_two = []
    
    while True: 
        start = input("What do you want to do? ")
    
        if start.lower() == 'add1':
            list_input = input("Type your object: ")
            list_one.append(list_input)

        elif start.lower() == 'add2':
            list_input = input("Type your object: ")
            list_two.append(list_input)

        
        elif start.lower() == 'see':
            merged_list = list_one + list_two
            print(sorted(merged_list))

        elif start.lower() == 'exit':
            print("Goodbye!")
            break
        
        else: 
            print("Invalid input. Try again.")

sort_lists()
