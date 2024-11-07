
import gradio as gr
import random

# Sample MCQ database (you can expand this with more questions)
mcq_database = {
    'math': [
        {
            'question': 'What is the value of π (pi) rounded to two decimal places?',
            'options': ['3.14', '3.16', '3.12', '3.18'],
            'correct': '3.14'
        },
        {
            'question': 'Solve: 2x + 5 = 15',
            'options': ['x = 5', 'x = 6', 'x = 7', 'x = 8'],
            'correct': 'x = 5'
        },
        {
            'question': 'Solve: 3x - 3 = 15',
            'options': ['x = 4', 'x = 6', 'x = 7', 'x = 8'],
            'correct': 'x = 4'
           


       }
    ],
    'science': [
        {
            'question': 'The material which transfer heat is known as?',
             'options': ['Conductor', 'Insulator', 'Thermal conductor', 'Thermal insulator'],
             'correct': 'Thermal conductor'
        },
        {
            'question': 'Which is the most abundant gas in Earth\'s atmosphere?',
            'options': ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'],
            'correct': 'Nitrogen'
        },
        {
            'question': 'What is the chemical formula for water?',
            'options': ['H2O', 'CO2', 'O2', 'N2'],
            'correct': 'H2O'
        },
        {
             'question': 'The material which transfer heat is known as?',
             'options': ['Conductor', 'Insulator', 'Thermal conductor', 'Thermal insulator'],
             'correct': 'Thermal conductor'
        }
    ]
}

def get_random_question(subject):
    return random.choice(mcq_database[subject])

def mcq_chatbot(message, history):
    if not message.strip():
        return "Please ask a question about math or science!"
    
    # Determine if user wants math or science question
    subject = 'math' if 'math' in message.lower() else 'science'
    
    # Get random question from database
    question_data = get_random_question(subject)
    
    # Format response
    response = f"Here's a {subject} question:\n\n"
    response += question_data['question'] + "\n\n"
    for i, option in enumerate(question_data['options']):
        response += f"{chr(65+i)}) {option}\n"
    
    response += "\nType your answer (A/B/C/D) or ask for another question!"
    
    # Check if user provided an answer
    if len(message) == 1 and message.upper() in ['A', 'B', 'C', 'D']:
        selected_answer = question_data['options'][ord(message.upper()) - 65]
        if selected_answer == question_data['correct']:
            return "Correct! Would you like another question?"
        else:
            return f"Sorry, that's incorrect. The correct answer is {question_data['correct']}. Would you like another question?"
    
    return response

iface = gr.ChatInterface(
    mcq_chatbot,
    chatbot=gr.Chatbot(height=600),
    textbox=gr.Textbox(
        placeholder="Type 'math' or 'science' for a question, or A/B/C/D to answer",
        container=False,
        scale=7
    ),
    title="Math & Science MCQ Bot",
    description="A chatbot for 6th-8th grade Math and Science MCQs",
    theme="soft",
    examples=[
        "Give me a math question",
        "I want a science question", 
        "Math question please",
        "Science MCQ",
        "Grade 7 math practice",
        "8th grade science test",
        "6th grade algebra",
        "Chemistry question", 
        "Physics problem",
        "Geometry practice"
    ],
    cache_examples=True
)

if __name__ == "__main__":
    iface.launch(share=True)
