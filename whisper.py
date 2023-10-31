import openai
from config import API_KEY, AUDIO_FILE_PATH, OUTPUT_TEXT_FILE

# Set your OpenAI API key
openai.api_key = API_KEY

# Load the audio file
audio_file = open(AUDIO_FILE_PATH, "rb")

# Transcribe the audio file using OpenAI's Whisper API
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Extract and print the transcribed text
print(transcript['text'])

# Save the transcribed text to a text file
with open(OUTPUT_TEXT_FILE, "w") as text_file:
    text_file.write(transcript['text'])
