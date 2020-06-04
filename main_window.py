import tkinter as tk

from view_test import ViewTest

class MainWindow():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Test Builder')

        self.test_view = ViewTest(self.window)

    def start(self):
        self.window.mainloop()
