# Chatbot Application

This is a simple chatbot application that uses the `chatterbot` library for natural language processing and conversation simulation. The bot is trained using a cleaned corpus of a WhatsApp chat export.

## Features

- Clean and preprocess WhatsApp chat exports
- Train a chatbot using the cleaned chat data
- Interactive conversation with the trained chatbot

## Requirements

- Python 3.6+
- `chatterbot` library
- `re` (regular expressions)
- `sqlite3`

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/alisajid4041/chat-bot.git
cd chat-bot
```
### 2. Create your virtual enviornment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install the Required Packages
```bash
Copy code
pip install -r requirements.txt
```
### 4. Prepare the Chat Data
Place your WhatsApp chat export file (e.g., chat.txt) in the root directory of the project.
 
### 5. Clean the Chat Data
Run the cleaner.py script to preprocess the chat data and remove metadata.
```bash
Copy code
python cleaner.py
```
### 6. Train the Chatbot
Run the bot.py script to train the chatbot using the cleaned chat data.

```bash
Copy code
python bot.py
```
