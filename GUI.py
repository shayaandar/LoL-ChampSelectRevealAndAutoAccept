import tkinter as tk
import lcu_class
import main

# Basic gui to start auto queue and reveal 
# Must reset after every game
# Need to make updates to design 

running = False

def toggle_execution():
    global running
    running = not running
    if running:
        main.main()    

window = tk.Tk()
window.title("Auto queue and champ select reveal")

button = tk.Button(window, text="Turn on", command=toggle_execution, width=50, height=10, bg="blue", fg="black", font=("Arial", 12))
button.pack()

window.mainloop()
