import random

story_parts = {
    "character": ["el niño", "la niña", "el hombre", "la mujer", "el perro", "el gato"],
    "action": ["corrió", "saltó", "caminó", "nadó", "voló", "condujo"],
    "location": ["en el parque", "en la playa", "en la montaña", "en la ciudad", "en el campo", "en el bosque"]
}

def generate_story():
    character = random.choice(story_parts["character"])
    action = random.choice(story_parts["action"])
    location = random.choice(story_parts["location"])
    story = f"{character} {action} {location}."
    return story

print(generate_story())
