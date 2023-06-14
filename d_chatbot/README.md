# MinorTron: AI Chatbot with Django and SQLite

This is an AI chatbot named MinorTron. It is built in Python using Django and SQLite. The chatbot utilizes the GPT-3.5-turbo model developed by OpenAI. The application allows users to log in and continue conversations, as the message history is saved to the database.

## Prerequisites

To run this application, you need to have the following installed:

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)
- OpenAI Python library

## Installation

1. Clone this repository to your local machine or download the source code as a zip file.
2. Navigate to the project directory using the command line.
3. Create a virtual environment (optional but recommended) using the following command:

   ```
   python3 -m venv venv

   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     venv\\Scripts\\activate

     ```

   - For Unix/Linux:

     ```
     source venv/bin/activate

     ```

5. Install the required dependencies by running:

   ```
   pip install -r requirements.txt

   ```

## Configuration

1. Obtain an API key for the GPT-3.5-turbo model from OpenAI.
2. Create a new directory in the chatbot directory called config.py.
3. Open `chatbot/config.py` and create a new variable called `API_KEY`. Enter the value of your own OpenAi API key.

## Usage

1. Run the following command to apply the database migrations:

   ```
   python manage.py migrate

   ```

2. Start the Django development server:

   ```
   python manage.py runserver

   ```

3. Open your web browser and go to `http://localhost:8000` to access the application.
4. Sign up for a new account or log in if you already have one.

   1. You can create an admin account by opening your terminal and entering the following command and following the prompts:

   ```
   python3 manage.py createsuperuser
   ```

   2. You can view the admin panel by visiting `http://localhost:8000/admin`

5. Once logged in, you can start a conversation with the AI chatbot.
6. Your conversation history will be saved, and you can continue the chat whenever you log in again.

## Project Structure

The main files and directories in this project are:

- `D_chatbot/`: The Django project's main directory.
  - `chatbot/`: The Django app directory containing the chat functionality.
    - `models.py`: Defines the database models for users and messages.
    - `views.py`: Handles the chat functionality and API endpoints.
    - `templates/`: Contains HTML templates for the chat interface.
    - `static/`: Contains static files such as CSS and JavaScript.
  - `d_chatbot/settings.py`: Configuration file for the Django project.
  - `d_chatbot/urls.py`: Contains the URL routing configuration.
- `manage.py`: Command-line utility for managing the Django project.

## License

This project is licensed under the [MIT License](notion://www.notion.so/LICENSE).

## Acknowledgments

- This project utilizes the GPT-3.5-turbo model developed by OpenAI.
- The Django framework provides the foundation for this application.
- The SQLite database engine is used to store message history.

## Stretch Goals

- Redesign UI with Tkinter or Recreate UI with Next.js
- Create separate page for user chat history
- Migrate to PostgreSql database
