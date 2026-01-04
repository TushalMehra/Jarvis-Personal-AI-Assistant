""""Jarvis - your Personal AI Assistant"""

import datetime
import webbrowser
import pywhatkit
import os
import subprocess
import wikipedia
import math


def jarvis():

    """
    Main Jarvis function that listens for user text commands
    and performs simple actions.
    """

    print("Hello, I am Jarvis! Your personal AI assistant")
    print("How can I help you today?")


    while True:

        command = input("\nYou: ").lower().strip()
        
        # takes input from the user 

        # If input doesn't contain any known keyword, it's probably gibberish
        
        '''known_keywords = ["time", "date", "youtube", "google", "weather", "open","play","exit", "quit", "stop", "search", "what is", "who is", "tell me", "tell me about", "what",]
        
        if not any(keyword in command for keyword in known_keywords):
            
            print("Jarvis: That doesn't seem like a valid command.")
            continue'''
    
        
        if command in ["exit", "quit", "stop"]:
                print("Jarvis: Goodbye! Have a great day!")
                break

        # time related queries

        elif "time" in command:
            now = datetime.datetime.now()

            if "yesterday" in command: 
                ref = now - datetime.timedelta(days=1)

                print("Jarvis: Around this time yesterday it was", ref.strftime("%I:%M %p"))

            elif "tomorrow" in command:
                ref = now + datetime.timedelta(days=1)
                print("Jarvis: Tomorrow at this time it will be", ref.strftime("%I:%M %p"))
            else:
                print("Jarvis: The current time is", now.strftime("%I:%M %p"))


        # 3️⃣ Date related queries
        elif "date" in command:

            now = datetime.datetime.now()

            if "yesterday" in command:
                ref = now - datetime.timedelta(days=1)
                
                print("Jarvis: Yesterday’s date was", ref.strftime("%A, %B %d, %Y"))
            elif "tomorrow" in command:
                ref = now + datetime.timedelta(days=1)
                print("Jarvis: Tomorrow’s date will be", ref.strftime("%A, %B %d, %Y"))
            else:
                print("Jarvis: Today’s date is", now.strftime("%A, %B %d, %Y"))


        # Website opening 

        elif "open" in command:

            if "youtube" in command:

                print("Jarvis: Opening YouTube..")

                webbrowser.open("https://www.youtube.com")


            elif "google" in command:
                
                print("Jarvis: Opening Google..")

                webbrowser.open("https://www.google.com")

            app_name = command.replace("open", "").strip().lower()

             # Dictionary of common apps and their system paths
            apps = {"word":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk",
                    "ms word":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk",
                    "msword":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk",
                    "vs code":r"C:\Users\Tushar\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
                    "vscode":r"C:\Users\Tushar\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
                    "excel": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk",
                    "paint": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Paint.lnk",
                    "powerpoint":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk",
                    "ms powerpoint":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk",
                    "mspowerpoint":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk",
                    "chrome":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk",
                    "google chrome":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk",
                    "edge": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk",
                    "ms edge": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk", 
                    "microsoft edge": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk",
                    "tableau": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Tableau Public 2025.2.lnk", 
                   "pgadmin 4": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 17\pgAdmin 4.lnk",
                   "pgadmin": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 17\pgAdmin 4.lnk",
                   "postgresql": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 17\pgAdmin 4.lnk",
                   "postgre sql": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PostgreSQL 17\pgAdmin 4.lnk",
                   "mysql":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Workbench 8.0 CE.lnk",
                   "my sql":r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Workbench 8.0 CE.lnk",
                   "files":r"C:\Windows\explorer.exe",
                   "file explorer":r"C:\Windows\explorer.exe",
                   "power bi": r"C:\Users\Public\Desktop\Power BI Desktop.lnk",
                   "powerbi": r"C:\Users\Public\Desktop\Power BI Desktop.lnk"
                    
                    }
                
            if app_name in apps:
                app_path = apps[app_name]
                try:

                    print(f"Jarvis: Opening {app_name}...")
                    os.startfile(app_path)

                    continue 
                except Exception as e:
                    print(f"Jarvis: Couldn't open {app_name}. Error: {e}")
                    
                
                
            site_name = command.replace("open","").strip() # to get the Website name

            if site_name == "":

                print("Jarvis: Please tell me what to open (e.g., 'open google').")
                    
                    
            elif "open" in command:
                words = command.split()
                    
                opened = False

                for word in words: 
                    if "." in word:   # to detect website name like "open github.com"

                        print(f"Jarvis: Opening {word}...")
                        webbrowser.open(f"https://{word}")
                        opened = True
                        break
                        
                    
                if not opened:
                    
                # If the user didn’t specify a domain (like .com or .org)

                    Common_Domains = [".com", ".org", ".net", ".edu", ".gov", ".info",
                                        ".io", ".co", ".ai", ".xyz", ".me",
                                        ".in", ".us", ".uk", ".ca", ".au", ".de", ".fr", ".jp"]
                                            
                    famous_sites = [ "youtube", "google", "facebook", "instagram", "twitter",
                                        "linkedin", "reddit", "amazon", "netflix", "spotify",
                                        "github", "stackoverflow", "wikipedia", "whatsapp",
                                        "discord", "zoom", "canva", "dropbox", "paypal", "apple",
                                         "microsoft", "twitch", "tiktok", "flipkart", "coursera"]


                    if site_name in famous_sites:
                        url = f"https://{site_name}.com"
                        webbrowser.open(url)

                    elif not any(domain in site_name for domain in Common_Domains):
                        print("Jarvis: Please specify the full website, e.g., 'open wikipedia.org'.")

                    else:
                        url = f"https://{site_name}"
                        print(f"Jarvis: Opening {site_name}...")
                        webbrowser.open(url)
            else:
                print("Jarvis: That doesn't seem like a valid response, make sure the spelling are correct")

        elif "play" in command: 

            # play any video on Youtube 

            video = command.replace("play", "").strip()  # to get the video title 

            if video: 
                print(f"Jarvis: Playing '{video}' on YouTube...")

                pywhatkit.playonyt(video)   # play the first video 

            else: 
                print("Jarvis: Please tell me what to play (e.g., 'play lovely by billie eilish').")

        elif ("search" in command or 
                "who is" in command or 
                "what is" in command or 
                "tell me about" in command or 
                "explain" in command or
                "meaning of" in command or
                "define" in command or
                "tell me" in command or 
                "what are" in command or
                "explain" in command or
                "meaning of" in command or
                "meaning" in command or
                "define" in command):
            

            topic = (command.replace("search", "")
                 .replace("who is", "")
                 .replace("what is", "")
                 .replace("tell me about", "")
                 .replace("what are", "")
                 .replace("tell me", "")
                 .replace("explain", "")
                 .replace("meaning of", "")
                 .replace("meaning", "")
                 .replace("define", "")
                 .strip())

            if topic:
                print(f"Jarvis: Searching  for '{topic}'...")

                try:

                    summary = wikipedia.summary(topic, sentences =2, auto_suggest = True, redirect = True) 
                    
                    print(f"Jarvis: {summary}")

                except wikipedia.DisambiguationError as e:

                     # If multiple meanings exist, pick the first one
                    print(f"Jarvis: There are multiple results. Showing info about '{e.options[0]}'.")

                    summary =wikipedia.summary(e.options[0], sentences=2)
                    print(f"Jarvis: {summary}")

                except Exception as e:
                    print(f"Jarvis: Searching Google for '{command}'...")
                    webbrowser.open(f"https://www.google.com/search?q={command}")


                except wikipedia.PageError:
                    # If page not found
                    print(f"Jarvis: I couldn’t find an exact page for '{topic}', let me open Google.")
                    webbrowser.open(f"https://www.google.com/search?q={topic}")

                except Exception:
                    # For all other unexpected issues
                    print(f"Jarvis: Something went wrong while searching on Wikipedia.")
                    webbrowser.open(f"https://www.google.com/search?q={topic}")

            else: 
                print("Jarvis: Please tell me what to search for.")

        elif "shutdown" in command:

            print("Jarvis: Shutting down the system")

            os.system("shutdown /s /t 3")


        elif "restart" in command:
            
            print("Jarvis: Shutting down the system")

            os.system("shutdown /s /t 3")

        elif ("what is" in command or "calculate" in command or "plus" in command or "minus" in command or 
              "multiply" in command or "divide" in command or "add" in command or 
              "subtract" in command or "square root" in command or 
              "cube root" in command or "power" in command or "^" in command
              or "+" in command or "-" in command or "/" in command or "*" in command or "and" in command
              or "**" in command or "%" in command or "=" in command  or "sum" in command or "sum of" in command):
            
            print("Jarvis: Let me calculate that for you...")

            try:
                if "square root of " in command:
                    num = float(command.replace("square root of", "").strip())
                    result = math.sqrt(result)

                elif "cube root" in command:
                    num = float(command.replace("cube root of", "").strip())
                    result = round(num ** (1/3), 2)

                elif "power" in command or "^" in command:
                    parts = command.replace("to the power of", "power").split("power")
                    base = float(parts[0].split()[-1])
                    exponent = float(parts[-1].strip())
                    result = base ** exponent

                else:
                    # Replace words with math symbols
                    expression = (command.replace("calculate", "")
                                  .replace("plus", "+")
                                  .replace("minus", "-")
                                  .replace("multiply", "*")
                                  .replace("times", "*")
                                  .replace("divide", "/")
                                  .replace("divided by", "/")
                                  .replace("add", "+")
                                  .replace("subtract", "-")
                                  .replace("sum", "+")
                                  .replace("sum of", "+")
                                  .strip())
                    
                    result = eval(expression)
                print(f"Jarvis: The answer is {result}")

            except Exception:
                print("Jarvis: Sorry, I couldn’t calculate that. Please try again by using a simple structure")


        elif "weather" in command:
            import requests
            from bs4 import BeautifulSoup

            try:

                if "in" in command:
                    city = command.split("in", 1)[-1].strip()

                else: 
                    city = "New Delhi"   # default city

                # Fetch weather data

                url = f"https://www.google.com/search?q=weather+in+{city}"

                html = requests.get(url).text

                soup = BeautifulSoup(html, "html.parser")

                # Extract temperature and condition

                temp = soup.find("span", class_="wob_t q8U8x").text

                condition = soup.find("div", class_="VQF4g").span.text.lower()

                print(f"Jarvis: It's {temp}°C in {city} with {condition}.")

            except Exception:
                print("Jarvis: Sorry, I couldn’t fetch the weather right now.")

        else:
            query = command.replace(" ","+")
            print("Jarvis: I'm not sure about that, but I can search it for you!")
            webbrowser.open(f"https://www.google.com/search?q={query}")

jarvis()




