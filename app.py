import streamlit as st
from transformers import pipeline

# Initialize the model
model = pipeline('text-generation', model='gpt2')

# Set up Streamlit app
st.title('Generative AI Assistant')

# Add a text input for user prompt
user_input = st.text_input('Enter a prompt:', '')

# Generate text
if user_input:
    result = model(user_input, max_length=50)
    st.write(result[0]['generated_text'])
