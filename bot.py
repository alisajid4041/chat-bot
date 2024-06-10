from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

# File containing the cleaned chat content
CORPUS_FILE = "chat.txt"

# Initialize ChatBot
chatbot = ChatBot('Chatpot')

# Initialize ListTrainer
trainer = ListTrainer(chatbot)

# Read cleaned chat content from the file
cleaned_corpus = clean_corpus(CORPUS_FILE)

# Train the chatbot using the cleaned corpus
trainer.train(cleaned_corpus)

# Define exit conditions
exit_conditions = (":q", "quit", "exit")

# Interactive chat loop
while True:
    query = input("> ")
    if query.lower() in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
