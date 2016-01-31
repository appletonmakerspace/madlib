import random
from tkinter import Button, Frame, Label, Tk
import tkinter


class Madlib:

    def get_madlib(self):
        madlib = """
        Once there was a {0}. It {1} at the {2}.
        Then because of its {3} it {4}. Wow! You sure are {5}!
        Thanks! I {6} you very much.
        """
        nouns = ['cheesecakes', 'bicycle', 'park', 'computer']
        verbs = ['watched tv', 'voted', 'fell over']
        adjectives = ['smelly', 'slimy', 'soft', 'loud']

        output = madlib.format(
            random.choice(nouns),
            random.choice(verbs),
            random.choice(nouns),
            random.choice(nouns),
            random.choice(verbs),
            random.choice(adjectives),
            random.choice(adjectives)
        )
        return output


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
