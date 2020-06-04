import tkinter as tk
from tkinter import ttk

class ViewInteractionPart():

    def __init__(self, parent):
        self.vars = dict()
        self.views = []

    def makeStep(self):
        return None

    def makeStringArgument(self, parent, name):
        row = tk.Frame(parent)
        row.pack(anchor=tk.W, expand=True, fill=tk.X)
        self.views.append(row)

        label = tk.Label(row, text='* {}:'.format(name))
        label.pack(side=tk.LEFT)

        value = tk.Entry(row)
        value.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.vars[name] = value

    def makeSelectArgument(self, parent, name, values):
        row = tk.Frame(parent)
        row.pack(anchor=tk.W, expand=True, fill=tk.X)
        self.views.append(row)

        label = tk.Label(row, text='* {}:'.format(name))
        label.pack(side=tk.LEFT)

        value = ttk.Combobox(row, values=values, state='readonly')
        value.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.vars[name] = value

    def clear(self):
        self.vars.clear()
        for view in self.views:
            view.destroy()
