#add the lists
tasks = []
hours = []

#print the menu and ask for an input
menu = ''' 
Hello. This is your To-Do-List program. What do you want to do?
If you want to add task, type add.
If you want to remove task, type remove. 
If you want to view tasks, type view. 
If you want to exit, type exit. '''

print(menu)

#while loop to create the program
while True: 
    start = input("Type:")
    
    #add the task
    if start.lower() == 'add':
        task = input("Add the task: ")
        tasks.append(task)
        hour = input("Add the task's hour: ")
        hours.append(hour)
        print("Task added!")
    
    #remove the task
    elif start.lower() == 'remove':
        task = input("Which task do you want to remove? Type the task name:")
        if task in tasks:
            task_index = tasks.index(task)
            hours.pop(task_index)
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found.")
    
    #view all tasks with assigned hours
    elif start.lower() == 'view':
        for task, hour in zip (tasks, hours):
            print(task, hour)
     
    #exit program
    elif start.lower() == 'exit':
        print("Goodbye!")
        break
        
    #invalid input  
    else: 
        print("Invalid input. Try again.")
