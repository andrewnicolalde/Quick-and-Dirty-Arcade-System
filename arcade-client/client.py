#!/usr/bin/env python3

import urllib.request
import subprocess
import time
import os
import signal

# Dict of acceptable titles to play.
title_command = {
    "Robot Bowl": "robotbwl",
    "Car Polo": "carpolo"
}

print(title_command)

# Make initial request
with urllib.request.urlopen("https://storage.googleapis.com/arcademachine/title.html") as response:
    title = response.read().decode('utf-8')
    print(title)
    
    # Store first response to avoid repeatedly launching same process
    current_title = title
    print(current_title)

    # No current title checks for first run
    print(title in title_command)
    if title in title_command:
        game_proc = subprocess.Popen(["mame", title_command[title]], shell=False)
        print(game_proc.pid)
    else:
        print("Invalid title")

    time.sleep(4)

# Repeatedly check status of current title
while True:
    with urllib.request.urlopen("https://storage.googleapis.com/arcademachine/title.html") as response:
        title = response.read().decode('utf-8')

    # If the latest title is different from the current title, launch the game
    if title in title_command:
        if current_title != title:
            subprocess.Popen(["kill", "-9", str(game_proc.pid)], shell=False) # Murder MAME because it doesn't seem to accept regular kills
            game_proc = subprocess.Popen(["mame", title_command[title]], shell=False)
            current_title = title
        else:
            print("The current game is already", title)
    
    
    time.sleep(4)
