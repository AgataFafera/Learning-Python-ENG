def bmi(w, h): #defining a function calculating BMI
    your_bmi = w / (h**2) #BMI formula
    print(your_bmi)
    if your_bmi < 18.5:
        return "Underweight"
    elif 18.5 <= your_bmi < 25.0: 
        return "Normal" 
    elif 25.0 <= your_bmi < 30.0:
        return "Overweight" 
    else: 
        return "Obesity"

while True: 
    try:
        weight = float(input("Please type your weight: "))
        height = float(input("Please type your height: ")) /100
        print(bmi(weight, height)) #Calling the function
        break
    except (ValueError, ZeroDivisionError): #Error handling 
        print("Invalid input. Please enter valid weight (kg) and height (cm) as floating-point numbers.")
