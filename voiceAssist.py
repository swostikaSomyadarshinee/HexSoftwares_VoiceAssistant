import os
import pyttsx3
import speech_recognition as sr
from datetime import datetime

class VoiceAssistant:
    
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        """Converts text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def wish(self):
        """Greeting the user."""
        hour = datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good morning! How can I help you?")
        elif 12 <= hour < 18:
            self.speak("Good afternoon! How can I help you?")
        else:
            self.speak("Good evening! How can I help you?")

    def speechrecognition(self):
        """Listen to user and convert speech to text."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                query = recognizer.recognize_google(audio, language='en-in')
                print(f"User said: {query}")
                return query.lower()
            except Exception as e:
                print("Sorry, I didn't catch that. Could you please repeat?")
                return None

    def MainExe(self):
        self.wish()  
        
        while True:
            self.Query = self.speechrecognition()  # Capture speech
            
            if not self.Query:
                continue
            
            if "hello" in self.Query:
                self.speak("Hello sir, welcome back")

            elif "bye" in self.Query:
                self.speak("Nice to meet you sir, Have a nice day")
                break

            elif "good night" in self.Query:
                self.speak("Wishing you a very good night. Take care and sweet dreams")

            elif "time" in self.Query:
                time = datetime.now().strftime("%H:%M")
                self.speak(f"The time now is: {time}")

            elif "open notepad" in self.Query:
                npath = "C:\\Windows\\notepad.exe"
                os.startfile(npath)

            elif "prompt" in self.Query:
                os.system("start cmd")

# Instantiating and running the assistant
if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.MainExe()
