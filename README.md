# Multi-Agent Chat Application

This repository contains a multi-agent chat application built using the autogen library. The application sets up various conversational agents with distinct personas and allows them to engage in group chats on different topics.

## Project Structure

### Files
- **`autogen-bananaonducttape.py`**: Script to set up and run a group chat with agents discussing a humorous topic.
- **`autogen-pizzadebateclub.py`**: Script to set up and run a group chat with agents debating food-related topics.
- **`streamlit-autogen-bananaonducttape.py`**: Streamlit application to interact with the multi-agent chat system via a web interface.
- **`OAI_CONFIG_LIST.json`**: Configuration file for the OpenAI API.
- **`requirements.txt`**: List of dependencies required for the project.

## Setup

### Install Dependencies
Run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

### Run Streamlit Application
Run the Streamlit application using the following command:
```bash
streamlit run streamlit-autogen-bananaonducttape.py
```

## Usage

### Streamlit Application
The Streamlit application provides a user-friendly interface to interact with the multi-agent chat system. You can view the descriptions of different agents and initiate chats on various topics.

### Scripts

#### autogen-bananaonducttape.py
- Sets up a humorous group chat with the following agents:
  - **StoryTeller**: A wildly imaginative writer who crafts absurd and humorous stories.
  - **Comedian**: A master of comedy who adds sharp wit and puns to every situation.
  - **Editor**: A sarcastic editor who critiques with humor and ensures coherence.
  - **MemeMachine**: A quirky AI obsessed with generating viral memes.

#### autogen-pizzadebateclub.py
- Sets up a debate-style group chat on food-related topics with the following agents:
  - **Chef_Luigi**: A passionate Italian chef.
  - **Foodie_Fran**: An enthusiastic food lover.
  - **Health_Guru**: A health-conscious expert.
  - **Meme_Machine**: A humorous AI specializing in food-related memes.
  - **Moderator**: A neutral and impartial moderator.

## Configuration
The configuration for the OpenAI API is stored in `OAI_CONFIG_LIST.json`. Ensure that the API key and other details are correctly set up before running the scripts.

## Contact
For any questions or issues, please open an issue on the GitHub repository.

