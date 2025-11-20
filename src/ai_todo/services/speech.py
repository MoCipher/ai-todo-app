from speech_recognition import Recognizer, Microphone
import pyttsx3

class SpeechService:
    def __init__(self):
        self.recognizer = Recognizer()
        self.microphone = Microphone()
        self.tts_engine = pyttsx3.init()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
            return audio

    def recognize_speech(self, audio):
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"Recognized command: {command}")
            return command
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            return None

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def add_task(self, task_description):
        # Placeholder for adding a task
        self.speak(f"Task '{task_description}' added to your to-do list.")

    def update_task(self, task_id, new_description):
        # Placeholder for updating a task
        self.speak(f"Task {task_id} updated to '{new_description}'.")