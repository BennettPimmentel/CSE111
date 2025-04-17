import pytest
from chatbot import detect_intent, generate_response

def test_detect_intent():
    assert detect_intent("Tell me a joke") == "tell_joke"
    assert detect_intent("What's the weather like?") == "tell_weather"
    assert detect_intent("I'm feeling great!") == "mood_happy"
    assert detect_intent("I'm so sad today.") == "mood_sad"
    assert detect_intent("I'm furious about something.") == "mood_angry"
    assert detect_intent("Wow, that was surprising!") == "mood_surprised"
    assert detect_intent("I'm so excited about this!") == "mood_excited"
    assert detect_intent("Where are you located?") == "tell_location"
    assert detect_intent("Let's talk about movies!") == "conversation_topic"
    assert detect_intent("Hello there!") == "unknown"


def test_generate_response():

    response = generate_response("tell_joke", "Tell me a joke")
    assert response in ["Why did the tomato blush? Because it saw the salad dressing!",
                        "I would tell you a construction joke, but I'm still working on it.",
                        "Why don't skeletons fight each other? They don't have the guts."]

    response = generate_response("tell_weather", "What's the weather like?")
    assert response in ["The weather today is sunny and warm!", 
                        "It's a rainy day outside. Don't forget your umbrella!",
                        "It looks cloudy today. You might want to carry a jacket."]

    response = generate_response("mood_happy", "I'm feeling great!")
    assert response == "You seem to be in a good mood! That's great!"

    response = generate_response("mood_sad", "I'm so sad today.")
    assert response == "I'm sorry to hear that you're feeling down. I'm here for you."

    response = generate_response("mood_angry", "I'm furious about something.")
    assert response == "Take a deep breath. Everything will be okay!"

    response = generate_response("mood_surprised", "Wow, that was surprising!")
    assert response == "Wow, you seem surprised! What happened?"

    response = generate_response("mood_excited", "I'm so excited about this!")
    assert response == "That's awesome! I'm glad you're feeling excited!"

    response = generate_response("tell_location", "Where are you located?")
    assert response == "We are based in the cloud, everywhere and nowhere!"

    response = generate_response("conversation_topic", "Let's talk about movies!")
    assert response == "Let's talk about something fun! What's your favorite movie?"

    response = generate_response("unknown", "Hello there!")
    assert response == "Sorry, I didn't understand that."
