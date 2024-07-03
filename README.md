# Spillmate LinkedIn Assistant Tool

This repository contains the code for the Spillmate LinkedIn Assistant Tool, a Streamlit application designed to help create professional and engaging LinkedIn content for Spillmate, a personalized AI chatbot focused on mental health support.

## Features

- **Write Post**: Generate LinkedIn posts about specified topics.
- **Write Article Summary**: Summarize LinkedIn articles.
- **Write Comment Reply**: Craft professional replies to LinkedIn comments.
- **Generate Hashtags**: Generate relevant LinkedIn hashtags.
- **Optimize Content**: Analyze and optimize LinkedIn content.
- **Create Poll**: Create LinkedIn polls.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sahiltr/spillmate-linkedin-assistant.git
    cd spillmate-linkedin-assistant
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a `.env` file in the project root directory with the following content:
        ```env
        GOOGLE_API_KEY=your_google_api_key
        ```

    - Set the Streamlit secrets for authentication by adding a `secrets.toml` file in the `.streamlit` directory with the following content:
        ```toml
        [secrets]
        USERNAME = "your_username"
        PASSWORD = "your_password"
        ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Log in using the username and password defined in the `secrets.toml` file.

4. Select a feature, enter your prompt, and define the desired character count range to generate the content.


## Contact

For any questions or suggestions, please feel free to contact:

- Sahil (thakursahil1912@gmail.com)

---

*Note: Replace placeholders like `your_google_api_key`, `your_username`, `your_password`, and `your_email@example.com` with actual values.*
