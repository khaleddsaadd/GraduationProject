import speech_recognition as sr 
r = sr.Recognizer()
print("Start")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=3)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    text = r.recognize_google(audio_data, language="ar")