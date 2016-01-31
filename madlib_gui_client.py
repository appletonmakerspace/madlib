from madlib import Madlib
from tkinter import Button, Frame, Label, Tk
import tkinter


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.new_madlib_button = Button(
            frame, text="New Madlib", command=self.new_madlib
            )
        self.new_madlib_button.pack(side=tkinter.LEFT)
        self.quit_button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.quit_button.pack(side=tkinter.RIGHT)
        self.label = Label(root, text=Madlib().get_madlib())
        self.label.pack()

    def new_madlib(self):
        self.label.config(text=Madlib().get_madlib())

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
