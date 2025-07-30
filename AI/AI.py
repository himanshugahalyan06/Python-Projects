import speech_recognition as sr
import pyttsx3
import json
import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google.oauth2 import service_account
import io
import serial
import time
import requests  

OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


SERVICE_ACCOUNT_FILE ="C:/Users/Himanshu/OneDrive/Desktop/HACKATHON/credentials1.json"
 
SCOPES = ["https://www.googleapis.com/auth/drive"]
MEMORY_QUESTION_FILE_ID = "1UrIfKW7i3XIvP-5nZg1avY35sSBNowoD"
MEMORY_ANSWER_FILE_ID = "1ZGo5Drgu4j0koyMOsku1qmH4l2j9RWKF"


engine = pyttsx3.init()
engine.setProperty("rate", 150)


try:
    arduino = serial.Serial("COM3", 9600, timeout=1)
    time.sleep(2)  
    print("Connected to Arduino on COM3")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None  


try:
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build("drive", "v3", credentials=creds)
    print("Google Drive API authenticated successfully!")
except FileNotFoundError:
    print("❌ Error: credentials1.json file not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"❌ Google API authentication error: {e}")
    exit()


def load_memory(file_id):
    try:
        request = drive_service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        file.seek(0)
        return json.load(file)
    except Exception as e:
        print(f"Error loading memory: {e}")
        return []


def save_memory(file_id, data):
    try:
        temp_file = "memory_temp.json"
        with open(temp_file, "w") as f:
            json.dump(data, f)

        media = MediaFileUpload(temp_file, mimetype="application/json")
        drive_service.files().update(fileId=file_id, media_body=media).execute()
        print("Memory saved successfully!")
        os.remove(temp_file)
    except Exception as e:
        print(f"Error saving memory: {e}")


def send_to_arduino(command):
    if arduino:
        try:
            arduino.write(command.encode())  
            print(f"Sent to Arduino: {command}")
        except Exception as e:
            print(f"Error sending command: {e}")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)  
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            return command
        except sr.WaitTimeoutError:
            print("Listening timed out. Try speaking again.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please repeat.")
            return None
        except sr.RequestError:
            speak("Could not connect to the speech recognition service.")
            return None


def openrouter_ai(query):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",  
        "messages": [{"role": "user", "content": query}]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"OpenRouter AI Error: {e}")
        return "I couldn't retrieve an answer."


def ai_assistant():
    memory_questions = load_memory(MEMORY_QUESTION_FILE_ID)
    memory_answers = load_memory(MEMORY_ANSWER_FILE_ID)
    
    speak("Hello! I will remember important things you say.")

    while True:
        command = listen()
        if not command:
            continue

       
        if "stop" in command:
            speak("Stopping all operations. Goodbye!")
            break  

     
        if "what do you remember" in command:
            if memory_questions:
                speak("Here is what I remember:")
                for q, a in zip(memory_questions, memory_answers):
                    speak(f"Question: {q}, Answer: {a}")
            else:
                speak("I don't remember anything yet.")
            continue

        if "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break

       
        motor_commands = {
            "go forward": "W",
            "go back": "S",
            "turn left": "A",
            "turn right": "D"
        }
        for phrase, cmd in motor_commands.items():
            if phrase in command:
                speak(f"{phrase.capitalize()}.")
                send_to_arduino(cmd)
                continue

       
        found = False
        for i, q in enumerate(memory_questions):
            if q.lower() == command.lower():  
                speak(f"The answer is: {memory_answers[i]}")
                found = True
                break
        if found:
            continue


       
        if "remember" in command:
            parts = command.split("remember", 1)[1].strip().split(" is ")
            if len(parts) >= 2:
                question, answer = parts[0].strip(), parts[1].strip()
                
                
                question_exists = False
                for i, q in enumerate(memory_questions):
                    if q.lower() == question.lower():  
                        memory_answers[i] = answer  
                        question_exists = True
                        break
                
                if not question_exists:
                    memory_questions.append(question)  
                    memory_answers.append(answer)
                
                save_memory(MEMORY_QUESTION_FILE_ID, memory_questions)
                save_memory(MEMORY_ANSWER_FILE_ID, memory_answers)
                speak(f"I learned: {question} is {answer}")
            else:
                speak("Please say something like 'remember my name is Devanshu,Himanshu,Riya,Vanshika'.")
            continue

       
        if "forget" in command or "remove" in command:
            key_phrase = command.replace("forget", "").replace("remove", "").strip()
            if key_phrase in memory_questions:
                index = memory_questions.index(key_phrase)
                memory_questions.pop(index)
                memory_answers.pop(index)
                save_memory(MEMORY_QUESTION_FILE_ID, memory_questions)
                save_memory(MEMORY_ANSWER_FILE_ID, memory_answers)
                speak(f"I forgot: {key_phrase}")
            else:
                speak(f"I don't remember {key_phrase}.")
            continue

       
        speak("Let me check that for you.")
        response = openrouter_ai(command)
        speak(response)


if __name__ == "__main__":
    ai_assistant()