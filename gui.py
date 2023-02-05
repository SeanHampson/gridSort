#gui.py
import tkinter as tk

class Gui:
    def __init__(self, master, title, res):
        self.master          = master
        self.master.title    = title
        self.master.geometry = res

    def addLocations(self):
        for row in range(15):
            for col in range(10):
                text = "Left"
                if col % 2 == 0: 
                    text = "Right"

                button = tk.Button(self.master, text=text)
                

                if row % 3 == 0: button.config(bg="green", fg="white")
                button.grid(row=row, column=col)


