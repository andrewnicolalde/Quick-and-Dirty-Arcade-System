#!/usr/bin/env python3

import urllib.request
import subprocess
import time
import os
import signal

# Make initial request
with urllib.request.urlopen("https://storage.googleapis.com/arcademachine/title.html") as response:
        title = response.read()
    
    # Store first response to avoid repeatedly launching same process
current_title = title

# No current title checks for first run
if title == b"robotbwl":
    # game_proc = subprocess.Popen(["mame", "robotbwl"], shell=False, preexec_fn=os.setsid)
    game_proc = subprocess.Popen(["mame", "robotbwl"], shell=False)
    print(game_proc.pid)
else:
    print("The value of the page is NOT robotbwl")
    
time.sleep(4)

# Repeatedly check status of current title
while True:
    with urllib.request.urlopen("https://storage.googleapis.com/arcademachine/title.html") as response:
        title = response.read()

    # If the latest title is different from the current title, launch the game
    if title == b"robotbwl":
        if current_title != title:
            subprocess.Popen(["kill", "-9", str(game_proc.pid)], shell=False) # Murder MAME because it doesn't seem to accept regular kills
            game_proc = subprocess.Popen(["mame", "robotbwl"], shell=False) 
        else:
            print("The current game is already", title)
    else:
        print("The value of the page is NOT robotbwl, killing current game process.")
        subprocess.Popen(["kill", "-9", str(game_proc.pid)], shell=False) # Murder MAME because it doesn't seem to accept regular kills
    
    time.sleep(4)
