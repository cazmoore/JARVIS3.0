# This is the product of a Udemy course - needs significant tailoring and refactoring
# TODO tidy up comments and redundant code throughout
# todo add various greetings, bye phrases etc, and set to pick randomly from the list
# todo allow ability to save last access time, so that greeting can be shorter
# todo integrate with todoist, google calendar etc.
# todo modularise code

import clipboard
import datetime
import os
import pyautogui
import pyjokes
import pywhatkit
import random
import requests
import speech_recognition as sr  # Converts spoken input to text
import hidden
import smtplib
import string
import subprocess
import webbrowser as wb
from agi import gpt_output
from email.message import EmailMessage
from mediawiki import MediaWiki
from newsapi import NewsApiClient
from new_voices import speak
# from nltk.tokenize import word_tokenize
from time import sleep

# engine = pyttsx3.init()
wakeword = "jarvis"


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


def time():
    xtime = datetime.datetime.now().strftime("%-I:%-M %p")
    speak(f"The current time is {xtime}.")


def date():
    xtime = datetime.datetime.now().strftime("%A, %-d %B, %Y")
    speak(f"Today is {xtime}.")


def greeting():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning Madam.")
    elif 12 <= hour < 18:
        speak("Good afternoon Madam.")
    elif 18 <= hour < 24:
        speak("Good evening Madam.")
    else:
        speak("Good night Madam.")


def wish_me():
    greeting()
    # time()
    # date()
    speak("How can I help you today?")


def take_command_text():
    query = input("How can I help you today? ")
    return query


def take_command_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-GB")
        print(f"User said: {query}")
        query = query.lower()

        return query

    except Exception as e:
        print(e)
        return "None"


def send_email(recipient, subject, content):
    with smtplib.SMTP('smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(hidden.sender_email, hidden.sender_password)
        email = EmailMessage()
        email["From"] = hidden.sender_email
        email["To"] = recipient
        email["Subject"] = subject
        email.set_content(content)
        server.send_message(email)
        server.close()


def send_whatsapp(phone, message):
    message = message
    wb.open(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
    sleep(10)
    pyautogui.press("enter")


def search_google():
    speak("What should I search for?")
    search = take_command_speech()
    wb.open(f"https://www.google.com/search?q={search}")


def news():
    newsapi = NewsApiClient(api_key="908cab1eef6544789800b7dab655aa7f")
    data = newsapi.get_top_headlines(
        sources='bbc-news,the-verge',
        language='en',
        page_size=5
    )
    news_data = data["articles"]
    for x, y in enumerate(news_data):
        speak(y["title"])

    speak("Those are the headlines for today.")


def text_to_speech():
    text = clipboard.paste()
    speak(text)


def screen_shot():
    # Create a "screenshot" folder in the current directory if it doesn't exist
    screenshot_folder = os.path.join(os.getcwd(), "screenshot")
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)

    # Get the current date and time
    current_time = datetime.datetime.now()
    # Format the current date and time as a string in the desired format
    timestamp = current_time.strftime("Screenshot %Y-%m-%d at %I.%M.%S %p.png")

    # Set the filename for the screenshot using the formatted current date and time
    filename = timestamp
    # Join the filename with the screenshot folder path
    filepath = os.path.join(screenshot_folder, filename)

    # Run the screencapture command to take a screenshot of the entire screen and save it to the "screenshot" folder
    subprocess.run(["screencapture", "-x", "-tpng", "-Sf", filepath])

    # Open the screenshot in Preview
    subprocess.run(["open", filepath])


def password_gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    password_length = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:password_length]))
    print(newpass)


if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command_speech().lower()
        # query = word_tokenize(query)

        if wakeword in query:
            query = query.replace("jarvis", "")
            # print(query)
            # query.remove("jarvis")
            # print(query)
            if "time" in query:
                time()

            elif "date" in query:
                date()

            elif "email" in query:
                email_list = {
                    "caroline": "cmoore365@gmail.com"
                }
                try:
                    speak("Who shall I email?")
                    name = take_command_speech().lower()
                    recipient = email_list[name]
                    speak("What is the subject?")
                    subject = take_command_speech()
                    speak("What should I say?")
                    content = take_command_speech()
                    send_email(recipient, subject, content)
                    speak("I've sent your email.")
                except Exception as e:
                    print(e)
                    speak("I'm sorry, I'm unable to send email at the moment.")

            elif "whatsapp" in query:
                user_name = {
                    "jarvis": "+13459178599"
                }
                try:
                    speak("Who shall I message?")
                    name = take_command_speech().lower()
                    phone_no = user_name[name]
                    speak("What should I say?")
                    content = take_command_speech()
                    send_whatsapp(phone_no, content)
                    speak("I've sent your message.")
                except Exception as e:
                    print(e)
                    speak("I'm sorry, I'm unable to send WhatsApps at the moment.")

            elif "wikipedia" in query:
                wikipedia = MediaWiki()

                speak("What shall I search for?")
                search = take_command_speech().lower()

                data = wikipedia.summary(search, sentences=2)
                speak(data)

            elif "google" in query:
                search_google()

            elif "youtube" in query:
                speak("What shall I look for on YouTube?")
                topic = take_command_speech()
                pywhatkit.playonyt(topic)

            elif "weather" in query:
                url = "https://api.openweathermap.org/data/3.0/onecall?lat=19.284474&lon=-81.373999&units=imperial&appid=316d751955ae34a226ca0fd765d541b1"
                result = requests.get(url)
                data = result.json()

                weather = data["current"]
                temp = weather["temp"]
                feels_like = int(weather["feels_like"])
                humidity = weather["humidity"]
                wind_speed = int(weather["wind_speed"])
                # wind_gust = weather["wind_gust"]
                description = weather["weather"][0]["description"]

                speak(f"It is currently {temp} degrees fahrenheit, with {humidity}% humidity, feeling like {feels_like} "
                      f"degrees. The wind is {wind_speed} miles per hour and {description}.")

            elif "news" in query or "headlines" in query:
                news()

            elif "read" in query:
                text_to_speech()

            elif "open documents folder" in query:
                # Get the path of the user's home directory and append the relative path to Documents folder
                documents_path = os.path.expanduser("~/Documents")

                # Run the open command with the Documents folder path
                subprocess.run(["open", documents_path])

            elif "open code editor" in query:
                program_path = "/Applications/Visual Studio Code.app"
                subprocess.run(["open", program_path])

            elif "joke" in query:
                speak(pyjokes.get_joke())

            elif "screenshot" in query:
                screen_shot()

            elif "remember" in query:
                speak("What should I remember?")
                data = take_command_speech()
                speak(f"You asked me to remember {data}.")
                remember = open("data.txt", "w")
                remember.write(data)
                remember.close()

            elif "remind" in query:
                remember = open("data.txt", "r")
                speak(f"You asked me to remember {remember.read()}.")

            elif "password" in query:
                password_gen()

            elif "offline" in query or "sleep" in query:
                speak("Ok, bye for now.")
                quit()

            else:
                gpt_output(query)
