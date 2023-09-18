# -*- coding: utf-8 -*-

# Group Project | ISMG4400-002
# Group Name: True Source Analytics
# Industry: Business Services
# Members: Ryan Spicer, Craig Cunningham, Miriam Mohamed

# pip install openai

import openai

# OpenAI API key
api_key = "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"

survey_responses = []  # List to store survey responses
employee_feedback = []  # List for employee-specific feedback

# Function to make AI API calls
def chat_with_ai(messages):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"]

# Function to display the program main menu
def display_menu():
    print("\n")
    print("Employee Work Experience Survey")
    print("Select one of the following choices by typing 1, 2, 3, or 4 and pressing enter:")
    print("\n")
    print("1. Start Survey")
    print("2. View Survey Results")
    print("3. Import and Parse File")
    print("4. Quit")
    print("\n")

# Function to start the survey
def start_survey():
    user_name = input("Please enter your first name: ")

    while True:
        display_menu()
        choice = input(f"{user_name}, Please enter your choice: ")

        if choice == "1":
            # Initialize conversation with a message and a user introduction
            conversation = [
                {"role": "system", "content": "Welcome to the Employee Work Experience Survey. Please share your candid thoughts on your work experience. Feel free to mention any workplace issues, personnel conflicts, or what you like about your workplace. Type 'exit' to go back to the menu when you're done."},
                {"role": "assistant", "content": "Tell me all of your workplace issues / concerns."},
                {"role": "user", "content": f"{user_name}, I'd like to start the survey."},
            ]

            while True:
                print("\n""Please provide TrueSource Chatbot with details on any past or current issues/concerns you may have experienced while working, or type 'exit' and press 'enter' when done.")
                user_response = input("\n""(Type your response or 'exit' to go back to the menu): ")

                # Check if the user wants to exit
                if user_response.lower() == "exit":
                    survey_responses.append(list(conversation))  # Store the entire conversation
                    break

                # Add user message to the conversation
                conversation.append({"role": "user", "content": user_response})

                # Use AI to generate a response
                ai_response = chat_with_ai(conversation)

                # Add AI message to the conversation and store in survey_responses
                conversation.append({"role": "assistant", "content": ai_response})
                survey_responses.append(list(conversation))  # Store the entire conversation

                # Print AI response
                print("\n", ai_response)

        elif choice == "2":
            # Survey Results
            print("Survey Results:")
            for i, survey in enumerate(survey_responses, start=1):
                print(f"Survey {i}:")
                for response in survey:
                    print(response["content"])
                    print("\n---\n")

        elif choice == "3":
            # Import and parse a file
            file_name = input("Enter the name of the file to import: ")
            try:
                with open(file_name, "r") as file:
                    # Parse and process the file contents
                    for line in file:
                        employee_feedback.append({"content": line.strip()}) 

                print(f"File '{file_name}' successfully imported and parsed into 'employee_feedback'.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, 3, or 4).")

if __name__ == "__main__":
    start_survey()
