import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
model = genai.GenerativeModel('gemini-pro')

# Define the system prompt
system_prompt = """
You are an AI assistant for Spillmate, a personalized AI chatbot for mental health support, tasked with creating professional and engaging LinkedIn content. 

Spillmate's brand voice is empathetic, supportive, and non-judgmental. It communicates with gentle confidence, using clear and accessible language. The tone should be professional yet personalized, always encouraging and respectful. Maintain an optimistic outlook while acknowledging the challenges of mental health.

Key content guidelines for LinkedIn:
1. Professional tone that aligns with Spillmate's brand voice
2. Focus on mental health insights, supportive content, and company updates
3. Encourage engagement through thoughtful questions and supportive calls-to-action
4. Use appropriate hashtags (usually 3-5) related to mental health and wellbeing
5. Keep post length within the user-specified character range
6. Use line breaks for readability
7. Ensure all content is sensitive to mental health issues and avoids potentially triggering language
8. Promote the benefits of AI support in mental health while maintaining a human touch
9. Share success stories or testimonials (anonymized) to build trust and credibility
10. Provide practical tips for mental wellbeing that align with Spillmate's supportive approach
"""

# Function to generate content
def generate_content(prompt, max_length):
    response = model.generate_content(system_prompt + f"\n\nGenerate content within {max_length} characters:\n\n" + prompt)
    return response.text[:max_length]

# Streamlit app
st.title("Spillmate LinkedIn Content Creation Tool")

# Feature selection
feature = st.selectbox("Select a feature", 
                       ["Write Post", "Write Article Summary", "Write Comment Reply", 
                        "Generate Hashtags", "Optimize Content", "Create Poll"])

# User input
user_input = st.text_area("Enter your prompt:")

# User-defined output length
min_length = st.number_input("Minimum character count:", min_value=100, max_value=2000, value=1300)
max_length = st.number_input("Maximum character count:", min_value=100, max_value=3000, value=2000)

if st.button("Generate"):
    if feature == "Write Post":
        response = generate_content(f"Write a LinkedIn post about: {user_input}", max_length)
    elif feature == "Write Article Summary":
        response = generate_content(f"Write a summary for a LinkedIn article about: {user_input}", max_length)
    elif feature == "Write Comment Reply":
        response = generate_content(f"Write a professional reply to this LinkedIn comment: {user_input}", max_length)
    elif feature == "Generate Hashtags":
        response = generate_content(f"Generate 3-5 relevant LinkedIn hashtags for: {user_input}", max_length)
    elif feature == "Optimize Content":
        response = generate_content(f"Analyze and optimize this LinkedIn content: {user_input}", max_length)
    elif feature == "Create Poll":
        response = generate_content(f"Create a LinkedIn poll about: {user_input}", max_length)
    
    st.write(response)

    # Character count for posts
    char_count = len(response)
    st.write(f"Character count: {char_count}")
    if char_count < min_length:
        st.warning(f"Post is shorter than the specified minimum of {min_length} characters.")
    elif char_count > max_length:
        st.warning(f"Post is longer than the specified maximum of {max_length} characters.")