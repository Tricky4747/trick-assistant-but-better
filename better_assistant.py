# made by Tricky
import datetime
import json
import wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha
import sys
from selenium import webdriver

print(
    "   _________          _          __                              \n  |  _   _  |        (_)        [  |  _                          \n  |_/ | | \_|_ .--.  __   .---.  | | / ]                         \n      | |   [ `/'`\][  | / /'`\] | '' <                          \n     _| |_   | |     | | | \__.  | |`\ \                         \n    |_____| [___]   [___]'.___.'[__|  \_]                   _    \n     / \                    (_)        / |_                / |_  \n    / _ \     .--.   .--.   __   .--. `| |-',--.   _ .--. `| |-' \n   / ___ \   ( (`\] ( (`\] [  | ( (`\] | | `'_\ : [ `.-. | | |   \n _/ /   \ \_  `'.'.  `'.'.  | |  `'.'. | |,// | |, | | | | | |,  \n|____| |____|[\__) )[\__) )[___][\__) )\__/'-;__/[___||__]\__/                                                                   "
)
print("Initializing Trick...")


class Response:
    def __init__(self, filename):
        self.file_content = self.read_file(filename)["intents"]

    def get_response(self, message):
        patterns = [element["patterns"] for element in self.file_content]
        for index, pattern in enumerate(patterns):
            if message in pattern:
                return random.choice(self.file_content[index]["responses"])
        return None

    def read_file(self, filename):
        if not os.path.isfile(filename):
            raise Exception()
        with open(filename, "r", encoding="utf8") as file_reader:
            return json.loads(file_reader.read())

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")


def myCommand():

    query = str(input("Query: "))
    return query

def webopen(url):
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        ),
    )
    webbrowser.get("chrome").open(url)

# main program
wish_me()
print("I am Trick. How may I help you?")

responses = Response("intents.json")

# logic for executing basic tasks
name = "Tricky"
if name == "Tricky":

    while True:

        query = myCommand()
        query = query.lower()

        if "open youtube" in query:
            print("okay")
            webopen("www.youtube.com")

        else:
            bot_response = responses.get_response(query)
            if bot_response:
                print(bot_response)
            else:

                if "google" in query:
                    print("Okay!")
                    str = query.replace("google", "")
                    url = f"google.com/search?q={str}"
                    webopen(url)

                elif "banner" in query:
                    print(
                        "   _________          _          __                              \n  |  _   _  |        (_)        [  |  _                          \n  |_/ | | \_|_ .--.  __   .---.  | | / ]                         \n      | |   [ `/'`\][  | / /'`\] | '' <                          \n     _| |_   | |     | | | \__.  | |`\ \                         \n    |_____| [___]   [___]'.___.'[__|  \_]                   _    \n     / \                    (_)        / |_                / |_  \n    / _ \     .--.   .--.   __   .--. `| |-',--.   _ .--. `| |-' \n   / ___ \   ( (`\] ( (`\] [  | ( (`\] | | `'_\ : [ `.-. | | |   \n _/ /   \ \_  `'.'.  `'.'.  | |  `'.'. | |,// | |, | | | | | |,  \n|____| |____|[\__) )[\__) )[___][\__) )\__/'-;__/[___||__]\__/                                                                   " + "\n"
                    )

                elif 'play music' in query:
                    songs_dir = "E:\\Tricky\\Tricky songs"
                    songs = os.listdir(songs_dir)
                    print(songs)
                    os.startfile(os.path.join(songs_dir, songs[random.randint(0, len(songs))]))

                elif'the time' in query:
                    strTime = datetime.datetime.now().strftime('%H:%M:%S')
                    print(f"The time is{strTime}")

                elif 'open timer' in query or 'open cstimer' in query or 'open CS timer' in query.lower():
                    print('okay')
                    webopen('www.cstimer.net')


                elif 'nothing' in query or 'abort' in query or 'stop' in query:
                    print("Bye Tricky, have a good day!")
                    sys.exit()

                elif 'open youtube' in query:
                    print('okay')
                    webopen('www.youtube.com')

                elif 'open google' in query:
                    print('okay')
                    webopen('www.google.com')

                elif 'open gmail' in query:
                    print('okay')
                    webopen('www.gmail.com')

                else:


                    try:
                        try:
                            res = client.query(query)
                            results = next(res.results).text
                            print("WOLFRAM-ALPHA says - ")
                            print("Got..  it.")
                            print(results)

                        except:
                            print("Searching...")
                            results = wikipedia.summary(query, sentences=2)
                            print("Got it.")
                            print("WIKIPEDIA says - ")
                            print(results)

                    except:
                        print("sorry, I couldnt find that. Here are the results on google.")
                        url = "google.com/search?q=" + query
                        webopen(url)

        print("Next Query!")
