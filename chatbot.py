print("AI Chatbot Started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello":
        print("Bot: Hi! How are you?")
    elif user_input == "how are you":
        print("Bot: I'm doing great!")
    elif user_input == "what is your name":
        print("Bot: My name is AI Bot.")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")