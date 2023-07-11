import tkinter as tk
from tkinter import ttk

import urllib3
import warnings 
import time
import random 

import lcu_class
import lcu_args

# Basic gui to start auto queue and reveal 
# Must reset after every game

# Optionality to enable auto accept
def enable_readycheck():
    if checkbox_var1.get() == 1:
        lcu_class.enable_ready_check = True
    else:
        lcu_class.enable_ready_check = False

# Optionality to enable champ select reveal 
def enable_champselect():
    if checkbox_var2.get() == 1:
        lcu_class.enable_champ_select = True
    else:
        lcu_class.enable_champ_select = False

# Recursively check gameflow state and perform API calls based on current state
def recursive_gameflow_check(lcu: lcu_class.LCU):
    enable_ready_check = enable_readycheck()
    enable_champ_select = enable_champselect()
    gameflow_phase = lcu.get_gameflow_phase()
    # Automatically starts matchmaking 
    if gameflow_phase == 'Lobby':
        print("Currently in lobby: starting matchmaking")
        lcu.start_matchmaking()
        time.sleep(random.randint(2,5))
    # Auto queue accept 
    if enable_ready_check and gameflow_phase == "ReadyCheck":
        print("Accepting Queue")
        time.sleep(random.randint(1,3))
        lcu.accept_queue()
    time.sleep(random.randint(4,7))
    # Champ select reveal 
    if enable_champ_select and gameflow_phase == 'ChampSelect':
        print("Entering champ select: outputting team data")
        participants = lcu.get_champ_select_participants()
        lcu.get_summoner_stats(participants, lcu.get_current_summoner())
        return None 
    
    recursive_gameflow_check(lcu)

def secondary_gameflow_check(lcu):
    gameflow_phase = lcu.get_gameflow_phase()

running = False
def toggle_execution():
    global running
    running = not running
    if running:
        lcu = lcu_class.LCU()
        lcu.set_region(lcu_args.get_lol_region())  # Set the region
        try:
            credentials = lcu_args.get_port_and_token()
            print(credentials)
        except:
            print("Credentials not retrieved, must start client or restart client")

        # Ignore certificate error 
        warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)

        lcu.set_credentials(credentials[0], credentials[1], credentials[2], credentials[3])
        lcu.initialize_LCU()
        lcu.initialize_riot()
        lcu.get_current_summoner()
        # Checks game state, auto accepts queue, and auto pulls up u.gg for teammates
        recursive_gameflow_check(lcu)


window = tk.Tk()
window.title("Queue Assist")
window.config(bg="white")

checkbox_var1 = tk.IntVar()
checkbox_var2 = tk.IntVar()

# Title Frame
title_frame = tk.Frame(window, bg="#34495e")
title_frame.pack(fill="x")

# Header Label
header_label = tk.Label(title_frame, text="League of Legends Queue Assist",
                        font=("Roboto", 20, "bold"), fg="white", bg="#34495e", padx=20, pady=15)
header_label.pack()

# Subheader Label
subheader_label = tk.Label(window, text="Start your client before turning on the tool",
                           font=("Arial", 16, "bold"), fg="black", bg="white", pady=15)
subheader_label.pack()



# Checkbox 1
checkbox1 = tk.Checkbutton(window, text="Auto Accept Queue", bg='white', fg='black',pady=5,variable=checkbox_var1, command=enable_readycheck)
checkbox1.pack()

# Checkbox 2
checkbox2 = tk.Checkbutton(window, text="Champ Select Reveal", bg='white', fg='black', pady=5,variable=checkbox_var2, command=enable_champselect)
checkbox2.pack()

# Bottom Space
space = tk.Label(window, height=2, bg="white")
space.pack()

button = tk.Button(window, text="Activate Queue Assist", command=toggle_execution, width=18, height=3, bg="#34495e", fg="black", font=("Helvetica", 16, "bold"), relief="raised", borderwidth=0, padx=10, pady=10)
button.pack()

# Hover effect
def on_enter(e):
    button.config(bg="#2c3e50")

def on_leave(e):
    button.config(bg="#34495e")

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Bottom Space
bottom_space = tk.Label(window, height=5, bg="white")
bottom_space.pack()

# Start the GUI event loop
window.mainloop()
