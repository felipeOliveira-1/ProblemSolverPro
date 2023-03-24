import os
import openai

# Set the OpenAI API key
# Replace with your actual API key
openai.api_key = ""

# Define the list of problem-solving approaches
problem_solving_approaches = [
    "Design Thinking",
    "Data-driven methodology",
    "Lean Thinking",
    "Systems Thinking",
    "TRIZ (Theory of Inventive Problem Solving)",
    "Methodology for systematic innovation",
    "Creative Problem Solving (CPS)",
    "Agile Methodology",
    "Root Cause Analysis (RCA)",
    "Decision Matrix Analysis",
    "SWOT Analysis",
    "Brainstorming",
    "PDCA (Plan, Do, Check, Act) Cycle",
    "A3 Problem Solving",
    "The Eight Disciplines (8D) Method",
    "The OODA Loop (Observe, Orient, Decide, Act)",
    "Divergent thinking",
    "Convergent thinking",
    "PESTLE Analysis",
    "Gap Analysis",
    "Appreciative Inquiry"
]

# Function to suggest the best approach based on user input


def suggest_approach(user_problem):
    # Define the messages to send to the chat model
    messages = [
        {"role": "system", "content": f"Here is a list of problem-solving approaches: {problem_solving_approaches}."},
        {"role": "user", "content": f"Which approach is best suited to address the following problem: '{user_problem}'?"}
    ]

    # Use OpenAI Chat API to suggest an approach
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract and return the suggested approach from the response
    return completion.choices[0].message['content'].strip()

# Function to display the start screen and handle user input


def display_start_screen():
    # ASCII art for the start screen
    ascii_art = r"""
.______   .______        ______   .______    __       _______ .___  ___.                    
|   _  \  |   _  \      /  __  \  |   _  \  |  |     |   ____||   \/   |                    
|  |_)  | |  |_)  |    |  |  |  | |  |_)  | |  |     |  |__   |  \  /  |                    
|   ___/  |      /     |  |  |  | |   _  <  |  |     |   __|  |  |\/|  |                    
|  |      |  |\  \----.|  `--'  | |  |_)  | |  `----.|  |____ |  |  |  |                    
| _|      | _| `._____| \______/  |______/  |_______||_______||__|  |__|                    
     _______.  ______    __      ____    ____  _______    .______   .______        ______   
    /       | /  __  \  |  |     \   \  /   / |   ____|   |   _  \  |   _  \      /  __  \  
   |   (----`|  |  |  | |  |      \   \/   /  |  |__      |  |_)  | |  |_)  |    |  |  |  | 
    \   \    |  |  |  | |  |       \      /   |   __|     |   ___/  |      /     |  |  |  | 
.----)   |   |  `--'  | |  `----.   \    /    |  |____    |  |      |  |\  \----.|  `--'  | 
|_______/     \______/  |_______|    \__/     |_______|   | _|      | _| `._____| \______/  
                                                                                            
             
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print(ascii_art)
    print("Welcome to ProblemSolverPro!")
    print("Press Enter to start, or type 'F1' for help.")

    while True:
        user_input = input()
        if user_input.lower() == '':  # Press Enter to start
            while True:  # Loop to allow multiple requests or exit
                # Get the user's input problem
                user_problem = input("Enter your problem: ")
                # Call the function and get the suggested approach
                suggested_approach = suggest_approach(user_problem)
                # Display the suggested approach to the user
                print(
                    f"The suggested approach for your problem is: {suggested_approach}")

                # Ask the user if they want to make a new request or exit
                new_request_input = input(
                    "Press Enter to make a new request or type 'exit' to exit the program: ")
                if new_request_input.lower() == 'exit':
                    print("Thank you for using ProblemSolverPro! Goodbye.")
                    return  # Exit the program
        elif user_input.lower() == 'f1':  # Type 'F1' for help
            print("ProblemSolverPro is an AI-powered advisor that helps you choose the best approach to solve problems.")
            print("How to use: Describe your problem when prompted, and the program will suggest an appropriate approach.")
            print("Press Enter to start, or type 'F1' for help.")
        else:
            print("Invalid input. Press Enter to start, or type 'F1' for help.")


# Run the start screen
display_start_screen()
