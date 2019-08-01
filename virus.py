import webbrowser
import time
import random

sites = ["http://www.google.com",
         "http://www.yahoo.com",
         "http://www.duckduckgo.com",
         "http://www.msn.com",
         "http://www.dalecarnegie.com",
         "http://www.youtube.com",
         "http://www.gmail.com"]

while True:
    site = random.choice(sites)
    webbrowser.open(site)
    seconds = random.randrange(5,20)
    time.sleep(seconds)
