#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random

class SimpleChatbotPython:
    def __init__(self):
        # Greeting the user and explaining the purpose of the program
        self.greetings = ["Hello! I'm your little Python helper! Ask me a question.", 
                          "Hi there! Ready for your Python question", 
                          "Hey! What do you want to learn today?"]
        
         # Saying goodbay to user
        self.goodbyes = ["Goodbye!", "See you later!", "Bye!"]
        
        # Answers to typical questions
        self.responses = {
            
            "How are you?": ["I'm good, thank you!", "Not bad!", "Doing well."],
            "What's your name?": ["I'm a  simple Python Chatbot.", "Call me ChatBot.", "No name, just call me Bot."],
            "What do you do?": ["I'm answering your Python questions", "I'm here to assist you."],
            "Why did my cat vomit on my new carpet?": ["Because your cat is a little jerk!"],
        }
        
        
    # Define a couple of functions answering to certain questions containg key words
    def function_question(self):
        return ''' In Python, a function is a reusable block of code that performs a specific task. \n
        It is defined using the `def` keyword, followed by the function name, parameters, and a colon. \n
        Functions help organize code, promote code reusability, and enhance modularity in Python programs. '''
        
    def python_question(self):
        return ''' Python is a high-level, interpreted programming language known for its simplicity and readability.\n 
        Created by Guido van Rossum, it emphasizes code readability and allows developers to express concepts \n
        with fewer lines of code than languages like C++ or Java. \n
        Python supports multiple programming paradigms, making it versatile for various applications, \n
        including web development, data science, artificial intelligence, and automation. '''
    
    def class_question(self):
        return ''' In Python, a class is a blueprint for creating objects, \n
        providing a way to define attributes and behaviors that the objects will possess. \n
        It serves as a template that encapsulates data and functions, enabling the creation of instances or objects based on \n
        that template with shared characteristics and functionality. '''
    
    def module_question(self):
        return ''' In Python, a module is a file containing Python code that defines variables, functions, \n
        and classes, which can be utilized in other Python files by importing them. \n
        Modules facilitate code organization, reusability, and the creation of a modular program structure in Python applications. '''
        
    def love_question(self):
        return ''' What is love? \n
        Baby, don't hurt me \n
        Don't hurt me, no more \n
        Baby, don't hurt me \n
        Don't hurt me, no more \n
        What is love? Yeah-yeah '''
        
    def loop_question(self):
        return ''' In Python, a loop is a control flow structure that allows \n
        a set of instructions to be repeatedly executed until a specific condition is met. \n
        The two main types of loops in Python are "for" loops, which iterate over a sequence (e.g., a list or range), \n
        and "while" loops, which repeatedly execute as long as a given condition is true. \n
        Loops are essential for automating repetitive tasks and iterating through data structures in Python programs.'''
    
    def error_question(self):
        return ''' In Python, an error refers to a deviation from the expected behavior in a program, preventing its successful execution. \n
        There are two main types of errors: syntax errors, which occur when the code structure violates Python's rules and cannot be parsed, \n
        and runtime errors, which occur during the execution of a program when an operation is attempted that is not valid. \n
        Exception handling in Python allows developers to anticipate and handle runtime errors, 
        improving the robustness of their programs. '''
    
    def variable_question(self):
        return ''' In Python, a variable is a named storage location that holds data, \n
        allowing programmers to reference and manipulate values in their code. \n
        Variables are created by assigning a value to a name using the assignment operator (`=`). \n
        Python is dynamically typed, meaning that the type of a variable is inferred at runtime based on the assigned value, \n
        making it flexible but requiring attention to data types during programming.'''
     
    # Define function to respond to user's inputs
    def get_response(self, user_input):
        user_input_lower = user_input.lower()
        
        if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey"]):
            return random.choice(self.greetings)
        elif any(goodbye in user_input_lower for goodbye in ["bye", "goodbye", "exit"]):
            return random.choice(self.goodbyes)
        elif "function" in user_input_lower:
            return self.function_question()
        elif "python" in user_input_lower:
            return self.python_question()
        elif "class" in user_input_lower:
            return self.class_question()
        elif "module" in user_input_lower:
            return self.module_question()
        elif "love" in user_input_lower:
            return self.love_question()
        elif "loop" in user_input_lower:
            return self.loop_question()
        elif "error" in user_input_lower:
            return self.error_question()
        elif "variable" in user_input_lower:
            return self.variable_question()
        else:
            return "I'm not sure how to respond to that."
        
        
def main():
    chatbot = SimpleChatbotPython()

    print("Welcome to the Simple Chatbot!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: " + chatbot.goodbyes[0])
            break

        response = chatbot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()


# In[ ]:




