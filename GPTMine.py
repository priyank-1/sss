import os
import gradio as gr
import openai
import pandas as pd

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

# Define the path to your Excel file containing questions
excel_file_path = "./ques.xlsx"

# Load questions from the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Extract questions from the first column (column 0) of the DataFrame
questions = df.iloc[:, 0].tolist()

# Combine the questions into a single string with each question separated by a newline
training_question = "\n".join(questions)

# Function to generate a response using GPT-3.5 Turbo
def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=50,  # Adjust the maximum number of tokens in the response
    )
    return response.choices[0].text.strip()

# Create a Gradio interface for the chatbot
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=7, label="Enter your text"),
    outputs="text",
    title="Custom-trained AI Chatbot"
)

# Launch the Gradio interface
iface.launch(share=True)
