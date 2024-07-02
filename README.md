# README File

# Language Learning Application

This application is designed to help users practice phrases in different languages using the OpenAI API. The application connects to a SQLite database, retrieves phrases, and allows users to practice them.

## Packages

The following Python packages are used in this project:

- **os**: Standard library for interacting with the operating system.
- **sqlite3**: Standard library for SQLite database interactions.
- **openai**: For interacting with the OpenAI API.
- **dotenv**: For loading environment variables from a `.env` file.
- **tabulate**: For displaying tabular data in a readable format.

## User's Instructions

1. **Prompt for Username and Password**:
   - When you run the application, you will be prompted to enter your username and password.

2. **Choose Native Language**:
   - If you are a new user, you will be prompted to select your native language from 10 options, each translated into the respective languages.
   - If you are a returning user, your native language will be retrieved from the database.

3. **Select Target Language**:
   - After choosing your native language, you will be prompted to select a target language you would like to practice from the 10 available languages, presented in your native language.

4. **Display Phrases**:
   - The application will then display the 25 most common universal phrases in a table format using the `tabulate` package. Each phrase will be shown in both your native language and the target language.

5. **Learn Phrases**:
   - You will be asked which phrase you would like to learn. A request will be sent to the OpenAI API to provide conjugation and example usage of the selected phrase.

6. **Further Assistance**:
   - After learning the phrase, you will be asked if you need further assistance. You can choose:
     - `0` to end the learning process.
     - `-1` to select another phrase to learn.
     - Ask a question to ChatGPT as an AI assistant.

7. **Exit**:
   - If you choose `0`, the learning session will end with a message, "Thank you!" indicating that Verbo has helped you learn the phrase.

## Sample Usage

### Each File's Purpose

- **Insert Data**:
  - Use `insertData.py` to insert phrases into the SQLite database.

- **Create Database Tables**:
  - Run `database.py` to create the necessary tables (user table, language table, and language translation table).

- **User Interaction**:
  - Run `user.py` to insert user information into the database, prompt for native and desired languages, and practice phrases.

- **Practice Phrases**:
  - Run `main.py` to start the application and follow the prompts to practice phrases in different languages.


Getting an API Key from the ChatGPT API

Sign Up / Log In:

Go to the OpenAI website.
If you don't have an account, click on the "Sign Up" button to create a new account.
If you already have an account, click on the "Log In" button and sign in with your credentials.
Navigate to the API Section:

Once logged in, navigate to the API section of the website. You can find this option in the main menu or dashboard.

Create a New API Key:

In the API section, look for the option to create a new API key.
Click on the "Create API Key" button.
Provide a name for your API key to help you identify it later (e.g., "ChatGPT Project Key").
Click "Generate Key" to create your new API key.
Copy the API Key:

Once the API key is generated, copy it to your clipboard. Make sure to store it securely, as it will be needed to authenticate your API requests.

At this point, we recommend storing the api key in a .env file at the same level as the main.py file.

Furthermore, it may be beneficial to create a .gitignore file and have the .env file be ignored by git.


