print("Welcome to your Perfect Number checking program.")

while True:
    try:
        number = int(input("Type any natural number: ")) # Asking user for the number
        num_sum = 0 # A variable to sum dividers
        if number <= 0: # Checking if the number is natural
            print("Please select a natural number.") 
            continue # Going back to the input
        else:
            for i in range(1,number): # For loop to check all numbers in range
                if number % i == 0: # Searching for the dividors
                    num_sum += i # Adding dividors to the sum variable
                else:
                    pass 

        if num_sum == number: # Checking if the sum of the dividors is equal to the given number
            print(True) 
            break
        else: 
            print(False)
            break             

    except ValueError: # Raising value error in case of invalid data
        print("Invalid data.")
        break