import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import tkinter as tk
from tkinter import Label
import threading

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    
    engine.say(text)
    engine.runAndWait()

def listen():
   
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def tell_time():
    
    current_time = datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}")

def search_web(query):
   
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)   

def show_robot_visual():
    
    root = tk.Tk()
    root.title("Robot Projection")
    label = Label(root, text="🤖 Hello, I am Jarvis!", font=("Helvetica", 24))
    label.pack(pady=20)
    root.mainloop()

def open_youtube():
    webbrowser.open("https://www.youtube.com")    

def main():
    
    
    threading.Thread(target=show_robot_visual, daemon=True).start()

    speak("Hello, I am Jarvis. How can I assist you today?")

    while True:
        command = listen()
        if "time" in command:
            tell_time()
        elif "search" in command:
            query = command.replace("search", "").strip()
            search_web(query)
        elif "search youtube for" in command:
            query = command.replace("search youtube for", "").strip()
            search_youtube(query)
        elif "open youtube" in command:
            open_youtube()   
        elif "stop" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("I did not understand that command. Please try again.")

if __name__ == "__main__":
    main()
