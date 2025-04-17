import random
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def load_response_data(file='responses.json'):
    with open(file, 'r') as f:
        return json.load(f)

response_data = load_response_data()

def greet_user():
    return random.choice(response_data["greetings"])

def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in response_data["keywords"]["greetings"]):
        return "greeting"
    elif any(word in user_input for word in response_data["keywords"]["farewells"]):
        return "farewell"
    elif any(word in user_input for word in response_data["keywords"]["faq"]):
        return "faq"
    if "joke" in user_input:
        return "tell_joke"
    elif "weather" in user_input:
        return "tell_weather"
    elif any(keyword in user_input for keyword in response_data["mood_keywords"]["happy"]):
        return "mood_happy"
    elif any(keyword in user_input for keyword in response_data["mood_keywords"]["sad"]):
        return "mood_sad"
    elif any(keyword in user_input for keyword in response_data["mood_keywords"]["angry"]):
        return "mood_angry"
    elif any(keyword in user_input for keyword in response_data["mood_keywords"]["surprised"]):
        return "mood_surprised"
    elif any(keyword in user_input for keyword in response_data["mood_keywords"]["excited"]):
        return "mood_excited"
    elif "location" in user_input:
        return "tell_location"
    elif any(topic.lower() in user_input for topic in response_data["conversation_topics"]):
        return "conversation_topic"
    else:
        return "unknown"

def generate_response(intent, user_input):
    if intent == "tell_joke":
        return random.choice(response_data["jokes"])
    elif intent == "tell_weather":
        return random.choice(response_data["weather"])
    elif intent == "mood_happy":
        return "You seem to be in a good mood! That's great!"
    elif intent == "mood_sad":
        return "I'm sorry to hear that you're feeling down. I'm here for you."
    elif intent == "mood_angry":
        return "Take a deep breath. Everything will be okay!"
    elif intent == "mood_surprised":
        return "Wow, you seem surprised! What happened?"
    elif intent == "mood_excited":
        return "That's awesome! I'm glad you're feeling excited!"
    elif intent == "tell_location":
        return response_data["faq"]["location"]
    elif intent == "conversation_topic":
        return "Let's talk about something fun! What's your favorite movie?"
    elif intent == "greeting":
        return random.choice(response_data["greetings"])
    elif intent == "farewell":
        return random.choice(response_data["farewells"])
    elif intent == "faq":
        return f"{response_data['faq']['hours']} {response_data['faq']['location']}"
    else:
        return "Sorry, I didn't understand that."


def get_user_mood(user_input):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(user_input)
    if sentiment_score['compound'] >= 0.05:
        return "positive"
    elif sentiment_score['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

def main_chat_loop():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        mood = get_user_mood(user_input)
        intent = detect_intent(user_input)
        response = generate_response(intent, user_input)
        
        print(f"Bot (Mood: {mood}): {response}")

if __name__ == "__main__":
    main_chat_loop()
