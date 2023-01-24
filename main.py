import random

story_parts = {
    "caracter": ["el niño", "la niña", "el hombre", "la mujer", "el perro", "el gato", "el toro"],
    "accion": ["corrió", "saltó", "caminó", "nadó", "voló", "condujo"],
    "localizacion": ["en el parque", "en la playa", "en la montaña", "en la ciudad", "en el campo", "en el bosque"]
}

def generate_story():
    character = random.choice(story_parts["caracter"])
    action = random.choice(story_parts["accion"])
    location = random.choice(story_parts["localizacion"])
    story = f"{character} {action} {location}."
    return story

print(generate_story())
