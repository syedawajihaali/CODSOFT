def get_response(user_input):
    user_input = user_input.lower()
    
    if any(keyword in user_input for keyword in ["hello", "hi", "hey"]):
        response = "Hello! How can I assist you?"
    elif "how are you" in user_input:
        response = "I'm just a chatbot designed to help and assist you with your queries. While I don't experience emotions like humans, I'm always here to help you. Is there something specific you'd like to know?"
    elif "tell me a joke" in user_input or "say something funny" in user_input:
        response = "Sure, here's a joke for you: Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif "what's your name" in user_input:
        response = "You can call me ChatBot! I'm here to chat and have fun with you."
    elif "what's my name" in user_input:
        response = "I'm sorry, but I don't have access to your name."
    elif "what's the weather like today?" in user_input:
        response = "I'm sorry but I don't have access to your location or the current weather. Is there anything else I can help you with?"
    elif "tell me a fun fact" in user_input:
        response = "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"
    elif "can you recommend me a book" in user_input:
        response = "How about 'Eleanor Oliphant Is Completely Fine' by Gail Honeyman? It's a contemporary fiction novel about a quirky and socially awkward women named Eleanor who embarks on a journey of self-discovery and friendship. It's a heartlfelt and uplifting story that you might enjoy"
    elif "can you recommend me a movie" in user_input:
        response = "How about 'Inception'? It's a mind-bending sci-fi thriller directed by Christopher Nolan. It's filled with action, suspense, and explores the concept within dreams. It's definitely a must-watch!"
    elif "what's the meaning of life?" in user_input:
        response = "Hmm, thats is a deep and philosophical question. It can mean different things to different people. Some find meaning in relationships, others in personal growth or pursuing their passions. It's a journey of self-discovery and finding what brings you joy anf fulfillment."
    elif "do you believe in aliens?" in user_input:
        response = "I'm open to the possibility of extraterrestrial life. The universe is vast and there could be other intelligent beings out there. It's an intriguing topic to think about!"
    elif "do you know any tongue twisters" in user_input:
        response = "Sure, here's a tongue twister for you: 'How can a clam cram in clean cream can' Give it a try!"
    elif "suggest a place for vacation" in user_input:
        response = "How about visiting Bali for your vacation? It's a tropical paradise known for its beautiful beaches, lush landscapes, and vibrant culture. You'll have a great time exploring the temples, trying delicious local cuisine, and relaxing on the stunning beaches."
    elif "what's artificial intelligence?" in user_input:
        response = "Artificial Intelligence (AI) is a field of computer science that focuses on creating intelligent machines that can perform tasks that typically require human intelligence. It involves developing algorithms and systems that can learn, reason, and make decisions, allowing them to solve complex problems, recognize patterns, and interact with humans. AI has applications in various areas, including natural language processing, computer vision, robotics, and more. It's pretty fascinating!"
    elif "tell me a story" in user_input:
        response = "Once upon a time, there was a little girl named Lily who loved exploring the world. One night, as she lay in bed, she closed her eyes and imagined herself on a grand adventure. She sailed across the ocean on a magical ship, climbed mountains to touch the sky, and even visited a castle made of candy! With each new dream, Lily's imagination grew bigger and brighter. As she drifted off to sleep, she knew that tomorrow would bring even more exciting journeys. Sweet dreams, my friend!"
    elif "goodbye" in user_input:
        response = "Goodbye! Have a great day!"
    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm sorry, I'm not sure how to respond to that."
    
    return response

def main():
    print("Chatbot: Hi there! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
 