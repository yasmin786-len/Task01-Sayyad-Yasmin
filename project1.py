print("Bot: Hello! I am DecodeBot.")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I am fine.",
    "what is your name": "I am DecodeBot.",
    "who created you": "I was created by Sayyad Yasmin.",
    "time": "I cannot tell the exact time yet.",
    "bye": "Goodbye!"
}

while True:

    user_input = input("You: ")

    user_input = user_input.lower().strip()

    if user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", reply)
    
    
    '''This project implements a Rule-Based AI Chatbot using
Python dictionaries, control flow, input,
and an infinite loop. The chatbot responds to
predefined user inputs and exits when the user enters
'bye' or 'exit'.'''
