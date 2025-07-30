import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import mysql.connector  # MySQL connector
from mysql.connector import Error

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
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Function to create a MySQL database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="root",      # Replace with your MySQL username
            password="password",  # Replace with your MySQL password
            database="jarvis_db"  # Replace with your database name
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to initialize the MySQL database
def init_db():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS memory
                             (id INT AUTO_INCREMENT PRIMARY KEY, 
                             key_text VARCHAR(255) NOT NULL, 
                             value_text VARCHAR(255) NOT NULL)''')
            connection.commit()
            print("Database initialized successfully.")
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Function to remember something
def remember(key, value):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO memory (key_text, value_text) VALUES (%s, %s)", (key, value))
            connection.commit()
            print(f"Remembered: {key} -> {value}")
        except Error as e:
            print(f"Error remembering data: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Function to recall something
def recall(key):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT value_text FROM memory WHERE key_text = %s", (key,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Error as e:
            print(f"Error recalling data: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Function to forget something
def forget(key):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM memory WHERE key_text = %s", (key,))
            connection.commit()
            print(f"Forgot: {key}")
        except Error as e:
            print(f"Error forgetting data: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Function to send an email
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')  # Replace with your email and password
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email.")

# Main function
if __name__ == "__main__":
    init_db()  # Initialize the database
    wishMe()   # Greet the user

    while True:
        query = takeCommand()  # Take voice input

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
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
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'  # Replace with your music directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Replace with your VS Code path
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"  # Replace with the recipient's email
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        elif 'remember that' in query:
            speak("What should I remember?")
            key = takeCommand()
            speak("What is the value?")
            value = takeCommand()
            remember(key, value)
            speak(f"I have remembered {key} as {value}")

        elif 'what is' in query:
            key = query.replace("what is", "").strip()
            value = recall(key)
            if value:
                speak(f"{key} is {value}")
            else:
                speak(f"I don't remember anything about {key}")

        elif 'forget' in query:
            key = query.replace("forget", "").strip()
            forget(key)
            speak(f"I have forgotten {key}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir!")
            break

        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")