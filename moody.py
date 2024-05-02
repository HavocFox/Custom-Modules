# moody.py

def mood_response(mood):
    if mood.lower() == 'happy':
        return "That's great to hear!"
    elif mood.lower() == 'sad':
        return "I'm sorry to hear that. Hope things get better."
    elif mood.lower() == 'okay':
        return "It's still good that your day isn't horrible."
    else:
        return "Please try again - I don't know what mood that is."
