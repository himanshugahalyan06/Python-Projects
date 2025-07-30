import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import mysql.connector
import requests
from bs4 import BeautifulSoup
import schedule
import time
import threading
import psutil
import shutil
from mysql.connector import Error
from gtts import gTTS
from googletrans import Translator
import subprocess

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Indian language support (22 major languages)
INDIAN_LANGUAGES = {
    'hindi': 'hindi', 'bengali': 'bn', 'telugu': 'te', 'marathi': 'mr',
    'tamil': 'ta', 'urdu': 'ur', 'gujarati': 'gu', 'kannada': 'kn',
    'malayalam': 'ml', 'oriya': 'or', 'punjabi': 'pa', 'assamese': 'as',
    'maithili': 'mai', 'santali': 'sat', 'kashmiri': 'ks', 'nepali': 'ne',
    'sindhi': 'sd', 'konkani': 'kok', 'dogri': 'doi', 'manipuri': 'mni',
    'bodo': 'brx', 'sanskrit': 'sa'
}

# Global language setting (default English)
current_language = 'en'
translator = Translator()

# Function to speak with multi-language support
def speak(audio, lang=None):
    global current_language
    
    lang_code = current_language if lang is None else lang
    
    if lang_code != 'en':
        try:
            # Translate to target language
            translated = translator.translate(audio, dest=lang_code).text
            tts = gTTS(text=translated, lang=lang_code)
            tts.save("temp_speech.mp3")
            subprocess.Popen(["start", "temp_speech.mp3"], shell=True)
            time.sleep(1)  # Allow time for speech to play
            return
        except Exception as e:
            print(f"Translation error: {e}")
            # Fallback to English
            engine.say("Error in translation. Using English.")
            engine.runAndWait()
    
    # Default English speech
    engine.say(audio)
    engine.runAndWait()

# Function to set language
def set_language(lang_name):
    global current_language
    if lang_name.lower() in INDIAN_LANGUAGES:
        current_language = INDIAN_LANGUAGES[lang_name.lower()]
        speak(f"Language set to {lang_name}", lang='en')
        return True
    else:
        speak("Sorry, that language is not supported", lang='en')
        return False

# Function to wish the user based on time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis. Please tell me how may I help you")

# Function to take voice commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Function to create a MySQL database connection
def create_connection(db_name=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database=db_name
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Initialize databases
def init_db():
    # Create jarvis_db if not exists
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS jarvis_db")
            cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
            conn.commit()
            print("Databases created successfully.")
        except Error as e:
            print(f"Error creating databases: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    # Create memory table in jarvis_db
    conn = create_connection("jarvis_db")
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS memory (
                             id INT AUTO_INCREMENT PRIMARY KEY, 
                             key_text VARCHAR(255) NOT NULL, 
                             value_text VARCHAR(255) NOT NULL)''')
            conn.commit()
            print("Memory table initialized successfully.")
        except Error as e:
            print(f"Error initializing memory table: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    # Create employee table in employee_db
    conn = create_connection("employee_db")
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data (
                             id INT AUTO_INCREMENT PRIMARY KEY,
                             name VARCHAR(255) NOT NULL,
                             position VARCHAR(255) NOT NULL,
                             department VARCHAR(255) NOT NULL,
                             email VARCHAR(255) NOT NULL,
                             phone VARCHAR(20) NOT NULL)''')
            conn.commit()
            print("Employee table initialized successfully.")
        except Error as e:
            print(f"Error initializing employee table: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# Employee database functions
def add_employee(name, position, department, email, phone):
    conn = create_connection("employee_db")
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO employee_data 
                             (name, position, department, email, phone) 
                             VALUES (%s, %s, %s, %s, %s)''', 
                             (name, position, department, email, phone))
            conn.commit()
            speak(f"Employee {name} added successfully")
            return True
        except Error as e:
            print(f"Error adding employee: {e}")
            speak("Sorry, I couldn't add the employee")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

def get_employee(search_term):
    conn = create_connection("employee_db")
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            # Try searching by ID
            if search_term.isdigit():
                cursor.execute("SELECT * FROM employee_data WHERE id = %s", (search_term,))
            else:
                cursor.execute("SELECT * FROM employee_data WHERE name LIKE %s", (f'%{search_term}%',))
            
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error fetching employee: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

# File system operations
def create_file(file_path):
    try:
        with open(file_path, 'w') as f:
            pass
        speak(f"File {file_path} created successfully")
        return True
    except Exception as e:
        print(f"Error creating file: {e}")
        speak("Sorry, I couldn't create the file")
        return False

def delete_file(file_path):
    try:
        os.remove(file_path)
        speak(f"File {file_path} deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        speak("Sorry, I couldn't delete the file")
        return False

def create_folder(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        speak(f"Folder {folder_path} created successfully")
        return True
    except Exception as e:
        print(f"Error creating folder: {e}")
        speak("Sorry, I couldn't create the folder")
        return False

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        speak(f"Folder {folder_path} deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting folder: {e}")
        speak("Sorry, I couldn't delete the folder")
        return False

# Web scraping
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and speak the title
        title = soup.title.string if soup.title else "No title found"
        speak(f"Page title: {title}")
        
        # Extract and speak first paragraph
        first_para = soup.find('p')
        if first_para:
            speak("First paragraph: " + first_para.get_text()[:200] + "...")
        else:
            speak("No paragraph content found")
        
        return True
    except Exception as e:
        print(f"Web scraping error: {e}")
        speak("Sorry, I couldn't scrape that website")
        return False

# Task scheduling
def schedule_task(task_time, task_command):
    try:
        schedule.every().day.at(task_time).do(
            lambda: speak(f"Reminder: It's time for {task_command}")
        )
        speak(f"Task scheduled for {task_time}")
        return True
    except Exception as e:
        print(f"Scheduling error: {e}")
        speak("Sorry, I couldn't schedule that task")
        return False

# System monitoring
def system_status():
    try:
        # CPU usage
        cpu_percent = psutil.cpu_percent()
        # Memory usage
        memory = psutil.virtual_memory()
        # Disk usage
        disk = psutil.disk_usage('/')
        
        status_report = (
            f"CPU Usage: {cpu_percent}%, "
            f"Memory Usage: {memory.percent}%, "
            f"Disk Usage: {disk.percent}%"
        )
        
        speak(status_report)
        return True
    except Exception as e:
        print(f"System monitoring error: {e}")
        speak("Sorry, I couldn't check system status")
        return False

# Email function
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
        return True
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email")
        return False

# Background scheduler thread
def scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start scheduler in background
scheduler = threading.Thread(target=scheduler_thread, daemon=True)
scheduler.start()

# Main function
if __name__ == "__main__":
    init_db()  # Initialize databases
    wishMe()   # Greet the user

    while True:
        query = takeCommand()  # Take voice input

        # Multi-language support
        if 'set language' in query:
            lang = query.replace('set language', '').strip()
            if set_language(lang):
                speak(f"Language changed to {lang}")

        # Employee database operations
        elif 'add employee' in query:
            speak("Please provide employee details")
            speak("Full name?")
            name = takeCommand()
            speak("Position?")
            position = takeCommand()
            speak("Department?")
            department = takeCommand()
            speak("Email?")
            email = takeCommand()
            speak("Phone number?")
            phone = takeCommand()
            add_employee(name, position, department, email, phone)
        
        elif 'find employee' in query:
            search_term = query.replace('find employee', '').strip()
            employees = get_employee(search_term)
            if employees:
                for emp in employees:
                    speak(f"Found: {emp['name']}, {emp['position']} in {emp['department']}")
            else:
                speak("No employees found with that name or ID")

        # File system operations
        elif 'create file' in query:
            file_path = query.replace('create file', '').strip()
            create_file(file_path)
        
        elif 'delete file' in query:
            file_path = query.replace('delete file', '').strip()
            delete_file(file_path)
        
        elif 'create folder' in query:
            folder_path = query.replace('create folder', '').strip()
            create_folder(folder_path)
        
        elif 'delete folder' in query:
            folder_path = query.replace('delete folder', '').strip()
            delete_folder(folder_path)

        # Web scraping
        elif 'scrape website' in query:
            url = query.replace('scrape website', '').strip()
            if not url.startswith('http'):
                url = 'https://' + url
            scrape_website(url)

        # Task scheduling
        elif 'schedule task' in query:
            speak("Please say the time in 24-hour format (e.g., 15:30)")
            task_time = takeCommand()
            speak("What should I remind you about?")
            task_command = takeCommand()
            schedule_task(task_time, task_command)

        # System monitoring
        elif 'system status' in query or 'system health' in query:
            system_status()

        # Existing features
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient@example.com"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir!")
            break

        else:
            speak("I didn't understand that command. Can you please repeat?")