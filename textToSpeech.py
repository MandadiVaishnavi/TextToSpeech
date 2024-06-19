import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get and print the available voices
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender}")
    print(f" - Age: {voice.age}\n")

# Set a different voice (optional)
engine.setProperty('voice', voices[1].id)  # Change index to select a different voice

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# The text you want to convert to speech
text = "Hello, Vaishnavi! This is a text to speech conversion example with a different voice."

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
