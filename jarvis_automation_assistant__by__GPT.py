import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import mysql.connector
import psutil
import shutil
import schedule
import time
import requests
import pywhatkit
import bs4
from mysql.connector import Error
from langdetect import detect
from security_and_face_emotion import unlock_with_face, detect_emotion
from sign_language import detect_sign_language
from multilingual_voice import speak, takeCommand, detect_language_and_speak, LANGUAGE_CODES
from multilingual_voice import detect
from gtts import gTTS
import playsound
from langdetect import detect
import speech_recognition as sr
import os
import cv2
import mediapipe as mp
import cv2
import face_recognition
from deepface import DeepFace


# Load known face

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

# Function to take voice commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Database connection functions
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="employee"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def fetch_employee(emp_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employee_data WHERE Emp_ID = %s", (emp_id,))
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error fetching employee: {e}")
        finally:
            cursor.close()
            connection.close()

# File system operations
def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    speak(f"Folder {folder_name} created successfully.")

def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        speak(f"Folder {folder_name} deleted.")
    except:
        speak("Error deleting the folder.")

# Web scraping
def fetch_weather():
    url = "https://www.weather.com/en-IN/weather/today"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    weather = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ')
    speak(f"Current temperature is {weather.text}")

# System monitoring
def check_cpu():
    usage = psutil.cpu_percent()
    speak(f"CPU is at {usage} percent usage")

# Email function
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        speak("Sorry, I am not able to send this email.")

# Scheduled task example
def scheduled_task():
    print("Running scheduled task...")
    speak("Running scheduled task")

schedule.every().day.at("10:30").do(scheduled_task)

# Main function
if __name__ == "__main__":
    wishMe()

    while True:
        schedule.run_pending()
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'create folder' in query:
            speak("Folder name please")
            folder = takeCommand()
            create_folder(folder)

        elif 'delete folder' in query:
            speak("Folder name to delete")
            folder = takeCommand()
            delete_folder(folder)

        elif 'weather' in query:
            fetch_weather()

        elif 'cpu' in query or 'system status' in query:
            check_cpu()

        elif 'employee' in query:
            speak("Please tell me the employee ID")
            emp_id = takeCommand()
            data = fetch_employee(emp_id)
            if data:
                speak(f"Employee details are: ID {data[0]}, Name {data[1]}, Company {data[2]}")
            else:
                speak("No employee found with that ID")
        elif 'play' in query:
            song = query.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            
        elif 'exit' in query:
            speak("Goodbye sir")
            break

        else:
            speak("Sorry, I didn't understand that")
        # jarvis_main.py

        # Security Unlock
    print("Scanning face for security...")
    known_face = "your_face.jpg"  # Put your registered face image here
    known_encoding = unlock_with_face(encode_known_face(known_face))

    if not known_encoding:
        print("Access Denied.")
        exit()

    # Greeting
    speak("Welcome back Sir, how can I assist you today?", lang='en')

    while True:
        query = takeCommand()
        if query == "None":
            continue

        detect_language_and_speak(query)

        if 'emotion' in query:
            emotion = detect_emotion()
            speak(f"I can see you're feeling {emotion}", lang='en')

        elif 'sign language' in query:
            result = detect_sign_language()
            speak(result)

        elif 'exit' in query:
            speak("Goodbye sir", lang='en')
            break
# multilingual_voice.py

LANGUAGE_CODES = {
    'hi': 'Hindi', 'ta': 'Tamil', 'te': 'Telugu', 'kn': 'Kannada', 'ml': 'Malayalam',
    'bn': 'Bengali', 'mr': 'Marathi', 'gu': 'Gujarati', 'pa': 'Punjabi', 'ur': 'Urdu',
    'or': 'Odia', 'as': 'Assamese', 'en': 'English', 'sd': 'Sindhi', 'kok': 'Konkani',
    'mai': 'Maithili', 'ks': 'Kashmiri', 'ne': 'Nepali', 'sa': 'Sanskrit',
    'bho': 'Bhojpuri', 'doi': 'Dogri', 'mni': 'Manipuri'
}

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3")
    os.remove("voice.mp3")

def takeCommand(language='en-IN'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language=language)
        print(f"You said: {query}")
        return query
    except:
        print("Sorry, didn't catch that.")
        return "None"

def detect_language_and_speak(query):
    lang_code = detect(query)
    lang = lang_code if lang_code in LANGUAGE_CODES else 'en'
    speak(query, lang=lang)

# sign_language.py


def detect_sign_language():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=2,
                           min_detection_confidence=0.7,
                           min_tracking_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    detected = False

    while True:
        success, img = cap.read()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                # Placeholder for classification logic
                detected = True
                cv2.putText(img, "Sign Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if not detected:
            cv2.putText(img, "Show hand sign...", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Sign Language Detection - Press Q to Exit", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Sign language detection completed"

# --- security_and_face_emotion.py --- (REAL-TIME FACE UNLOCK & EMOTION DETECTION)


def encode_known_face(image_path):
    image = face_recognition.load_image_file(image_path)
    return face_recognition.face_encodings(image)[0]

# Face Unlock with Real-Time Webcam

def unlock_with_face(known_face_encoding):
    video = cv2.VideoCapture(0)
    unlocked = False

    while not unlocked:
        _, frame = video.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
            if True in matches:
                print("Access Granted")
                unlocked = True
                break

        cv2.imshow("Security Check - Press Q to Quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return unlocked

# Real-Time Emotion Detection

def detect_emotion():
    cap = cv2.VideoCapture(0)
    detected_emotion = ""

    while True:
        _, frame = cap.read()
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        cv2.putText(frame, f"Emotion: {emotion}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Emotion Detection - Press Q to Exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            detected_emotion = emotion
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected_emotion