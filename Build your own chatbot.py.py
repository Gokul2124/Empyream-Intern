responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "bye": "Goodbye! Feel free to return if you have more questions.",
}

# Main chat loop
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = responses.get(user_input, "I'm not sure how to respond to that.")
    print("Chatbot:", response)
