import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    ("hi|hello|hey|hii", ["Hello!", "Hlw", "Hi there!", "Hey!"]),
    ("ok sorry|sorry" , ["No problem" , "It's okay"]),
    ("how are you?|how r u", ["I'm good,What about you?", "superb, you?", "I'm doing well, how are you?."]),
    ("i am good|fine|i am also good|i am fine",["good to hear","nice"]),
    ("your name?|who are you?", ["I am a chatbot.", "You can call me Chatbot."]),
    ("who made you|who built you|who developed you|who is your owner|who invented you?", ["Rithish"]),
    ("what can you do for me?", ["I can chat with you","I'm here to assist you and have conversations."]),
    ("by|bye|goodbye|ok by", ["Goodbye!", "See you later.", "Bye!"]),
    ("what is your age",["Never ask age of chatbot I dont have age I can have only versions"]),
    ("What is your version",["my version is basic"])
    # You can add more patterns and responses here
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

def basic_chat():
    print("Hi! I'm a basic chatbot. You can start chatting with me. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", chatbot.respond(user_input))

nltk.download('punkt')
basic_chat()
