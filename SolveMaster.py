import os
import openai

# Set the OpenAI API key
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

# Get the user's input problem
user_problem = input("Enter your problem: ")

# Call the function and get the suggested approach
suggested_approach = suggest_approach(user_problem)

# Display the suggested approach to the user
print(f"The suggested approach for your problem is: {suggested_approach}")
