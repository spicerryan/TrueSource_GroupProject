# -*- coding: utf-8 -*-

#Group Project | ISMG4400-002
#Group Name: True Source Analytics
#Industry: Business Services
#Members: Ryan Spicer, Craig Cunningham, Miriam Mohamed

#TrueSource Feedback and Engagement Survery Bot

#!pip install openai
#import openai

import os
import openai

response = openai.ChatCompletion.create(
    api_key = "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",
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"system",
            "content":"You are participating in a feedback and engagement survey."
            
            
        },
        {"role":"user",
         "content":"***"
         
         }
        
        
        ],
    temperature = 0,
    max_tokens = 256,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
    
    
        )
print (response)
TrueSourceGPTcontent = response["choices"][0]["message"]["content"]
print (TrueSourceGPTcontent)

# Greet the user and get them to enter their first name
def greet_user():
    print("Welcome to the TrueSource Feedback and Engagement Survey Bot!")
    user_name = input("Please enter your first name: ")
    return user_name

# Display the menu options
def display_menu():
    print("\nMain Menu:")
    print("1. Take the survey")
    print("2. View previous survey results")
    print("3. Exit")

# Function to take the survey
def take_survey():
    print("\nLet's start the survey. Please answer the following questions:")
    
    # Generate questions and collect responses
    # Question 1:
    user_responses = []
    question = "How satisfied are you with your job? (1 - Very Dissatisfied, 5 - Very Satisfied): "
    user_answer = input(question)
    user_responses.append({"question": question, "answer": user_answer})

    # Question 2:
    user_responses = []
    question = "Question 2? (1 - ***, 5 - ***): "
    user_answer = input(question)
    user_responses.append({"question": question, "answer": user_answer})

    # Question 3:
    user_responses = []
    question = "Question 3? (1 - ***, 5 - ***): "
    user_answer = input(question)
    user_responses.append({"question": question, "answer": user_answer})
    
    print("\nThank you for completing the survey!")

# Function to view previous survey results (FUNCTIONALITY NOT YET IMPLEMENTED)
def view_results():
    print("\nViewing previous survey results... (This functionality is not implemented yet)")

# Main program
if __name__ == "__main__":
    user_name = greet_user()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            take_survey()
        elif choice == "2":
            view_results()
        elif choice == "3":
            print(f"Goodbye, {user_name}!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

