import pyttsx3
from datetime import datetime, date

# engine ko sirf **ek baar init** karo


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    print("Bot:", text)
    engine.stop()
    engine.say(text)
    engine.runAndWait()   # ye ensure kare ki har baar speech play ho

def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I am a simple Python voice bot."
    elif "time" in user_input:
        return "Current time is " + datetime.now().strftime("%H:%M")
    elif "date" in user_input:
        return "Today's date is " + str(date.today())
    elif "python" in user_input:
        return "Python is a programming language used for development, AI, and automation."
    elif "bye" or "byy" or "by" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't know that yet."

# --------- main loop
while True:
    user = input("You: ")
    response = chatbot(user)
    speak(response)

    if "bye" in user.lower():
        break