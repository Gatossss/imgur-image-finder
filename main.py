from os import truncate
import requests 
import random
import string
import dhooks
from dhooks import Webhook
import threading

def main():
    while True:
        characters = string.ascii_letters + string.digits + string.ascii_uppercase
        generated = ''.join(random.choice(characters) for i in range(7))

        r = requests.get ("https://i.imgur.com/" + generated + ".png")

        if r.url == "https://i.imgur.com/removed.png":
            pass
        else:
            hook = Webhook('https://discord.com/api/webhooks/930532298342948918/4ijaQ9CrZn2CUZUdkw3X5h4QfuWB0eqmjOyn0clqCvpBMNPxB4sh5xf1_mMenpRr2qxt')
            hook.send(r.url)


for x in range(69):
    threading.Thread(target=main).start()
 
