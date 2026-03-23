# ----------------------- Mini ChatBot Rule Based -----------------------
# ==================== Additional Features in Future ===============
# Add time based greeting (using datetime module)
# Add text to speech (using (pyttsx3))
# Add voice input (using speech_recognition)
# Connect to an AI API for real answers (like OpenAI / Hugging Face)
# Store Chat history in a file using File Handling

import random
import datetime
import time

name = input("Swaggat hai aapka 🙏, Enter your name: ")
persent = datetime.datetime.now().hour

# presentTime = t

responses_memory = {

    "greeting": {
        "inputs": ["hi", "hello", "hey"],
        "responses": [
            "Hey! 😊 What’s on your mind today?",
            "Hello! How can I help you?",
            "Hi there! Need any help?"
        ]
    },

    "how_are_you": {
        "inputs": ["how are you", "how are you doing"],
        "responses": [
            "I’m doing great! 😎",
            "All good here! What about you?",
            "Feeling awesome! 😊"
        ]
    },

    "bot_intro": {
        "inputs": ["who are you", "your name"],
        "responses": [
            "I’m your personal chatbot 🤖",
            "I’m a simple chatbot built to help you!",
            "Call me your assistant 😄"
        ]
    },

    "help": {
        "inputs": ["help", "what can you do"],
        "responses": [
            "I can chat and answer simple questions!",
            "Try asking me something fun 😄"
        ]
    },

    "jokes": {
        "inputs": ["joke", "tell me a joke"],
        "responses": [
            "Why do programmers hate nature? Because it has too many bugs 😆",
            "Why did the computer get cold? Because it forgot to close Windows 🥶"
        ]
    },

    "bored": {
        "inputs": ["bored", "i am bored"],
        "responses": [
            "Let’s fix that 😄 Want a joke?",
            "Hmm… ask me something interesting 😎"
        ]
    },

    "sad": {
        "inputs": ["sad", "i am sad"],
        "responses": [
            "I’m here for you 🙂",
            "Hope things get better soon 💛"
        ]
    },

    "thanks": {
        "inputs": ["thanks", "thank you"],
        "responses": [
            "You’re welcome! 😊",
            "Anytime 😄"
        ]
    },

    "goodbye": {
        "inputs": ["bye", "goodbye", "exit"],
        "responses": [
            "Goodbye! 👋",
            "See you later!",
            "Take care 😄"
        ]
    },
    "random": {
        "inputs": ["something", "random", "anything"],
        "responses": [
            "Did you know? Honey never spoils 🍯",
            "Fun fact: Octopuses have 3 hearts 🐙",
            "Random fact: Bananas are berries 🍌"
        ]
    },
    "motivation": {
        "inputs": ["motivate me", "i feel lazy", "no motivation"],
        "responses": [
            "Start small, but start now 💪",
            "Discipline beats motivation 🔥",
            "You’ve got this! Keep going 🚀"
        ]
    },
    "food": {
        "inputs": ["hungry", "food", "what to eat"],
        "responses": [
            "Maybe try pizza 🍕 or something you love!",
            "How about ordering your favorite food?",
            "I wish I could eat too 😄 What are you craving?"
        ]
    },
    "coding": {
        "inputs": ["coding", "programming", "learn coding"],
        "responses": [
            "Start with Python or JavaScript 👍",
            "Practice daily and build projects 💻",
            "Coding is all about consistency!"
        ]
    }

}

def getResponseOfChat(userQuestion):
    userQuestion = userInput.lower()
    for eachKey in responses_memory:
        for pattern in responses_memory[eachKey]["inputs"]:
            if pattern in userQuestion:
                return random.choice(responses_memory[eachKey]["responses"])
    
    return random.choice([
        "Sorry, I didn’t understand that 🤔",
        "Can you rephrase?",
        "I’m not sure about that!"
    ])

# ---------------------------------------------------------------------------------------------------


if 5<= persent <= 11:
    print(f"Good Morning {name} ")
elif 11<= persent <= 16:
    print(f"Good Afternoon {name}")
elif 16<= persent <= 20:
    print(f"Good Eveneing {name}")
else:
    print(f"Good Night {name}")

print("🤖 Chatbot: Hello! Type 'exit' to stop.")
while True:
    userInput = input("You: ")
  
    if userInput.lower() == "exit":
        print("🤖 Chatbot: Goodbye! 👋")
        break
    reply = getResponseOfChat(userInput)
    print("🤖 Chatbot:", reply)