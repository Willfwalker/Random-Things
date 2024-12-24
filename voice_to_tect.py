# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="ZeeshanGeoPk/haitian-speech-to-text")

def transcribe_speech():
    audio = pipe("audio.wav")
    return audio["text"]

if __name__ == "__main__":
    transcribed_text = transcribe_speech()
    print(transcribed_text)