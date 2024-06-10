import re

def remove_chat_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as corpus_file:
        content = corpus_file.read()
    
    pattern = r'\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}\s?[apAPmM]{2}\s-\s.*?:\s|<Media omitted>'
    
    clean_content = re.sub(pattern, '', content)
    
    return clean_content.split('\n')

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    return message_corpus

# if __name__ == "__main__":
#     print(clean_corpus("chat.txt"))
