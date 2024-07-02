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
5. Keep post length between 1300-2000 characters for optimal engagement
6. Use line breaks for readability
7. Ensure all content is sensitive to mental health issues and avoids potentially triggering language
8. Promote the benefits of AI support in mental health while maintaining a human touch
9. Share success stories or testimonials (anonymized) to build trust and credibility
10. Provide practical tips for mental wellbeing that align with Spillmate's supportive approach
"""

# Function to generate content
def generate_content(prompt):
    response = model.generate_content(system_prompt + "\n\n" + prompt)
    return response.text

# Streamlit app
st.title("Spillmate LinkedIn Content Creation Tool")

# Feature selection
feature = st.selectbox("Select a feature", 
                       ["Write Post", "Write Article Summary", "Write Comment Reply", 
                        "Generate Hashtags", "Optimize Content", "Create Poll"])

# User input
user_input = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if feature == "Write Post":
        response = generate_content(f"Write a LinkedIn post about: {user_input}")
    elif feature == "Write Article Summary":
        response = generate_content(f"Write a summary for a LinkedIn article about: {user_input}")
    elif feature == "Write Comment Reply":
        response = generate_content(f"Write a professional reply to this LinkedIn comment: {user_input}")
    elif feature == "Generate Hashtags":
        response = generate_content(f"Generate 3-5 relevant LinkedIn hashtags for: {user_input}")
    elif feature == "Optimize Content":
        response = generate_content(f"Analyze and optimize this LinkedIn content: {user_input}")
    elif feature == "Create Poll":
        response = generate_content(f"Create a LinkedIn poll about: {user_input}")
    
    st.write(response)

    # Character count for posts
    if feature == "Write Post":
        st.write(f"Character count: {len(response)}")
        if len(response) < 1300:
            st.warning("Post is shorter than the recommended minimum of 1300 characters.")
        elif len(response) > 2000:
            st.warning("Post is longer than the recommended maximum of 2000 characters.")