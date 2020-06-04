import tkinter as tk
from tkinter import ttk

from view_click import ViewClick
from view_navigate import ViewNavigate
from view_input import ViewInput
from selenium import webdriver

class ViewTest():

    def __init__(self, parent):
        self.interaction_arguments = None
        self.steps = []
        self.driver = None

        self.view = tk.Frame(parent)
        self.view.pack(fill=tk.X, padx=5, pady=5)
        
        steps_label = tk.Label(self.view, text='Steps:')
        steps_label.pack(anchor=tk.W)

        self.step_list = tk.Frame(self.view)
        self.step_list.pack(fill=tk.X)

        separator = ttk.Separator(self.view, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=5)

        addLabel = tk.Label(self.view, text='New Step:')
        addLabel.pack(anchor=tk.W)

        self.interactions = ['Click', 'Navigate', 'Input']

        interaction_row = tk.Frame(self.view)
        interaction_row.pack(fill=tk.X, expand=True)

        interaction_label = tk.Label(interaction_row, text='Interaction:')
        interaction_label.pack(side=tk.LEFT)

        self.interaction = ttk.Combobox(interaction_row, state='readonly', values=self.interactions)
        self.interaction.pack(side=tk.LEFT, expand=True, fill = tk.X)
        self.interaction.bind("<<ComboboxSelected>>", self.onChangeInteraction)

        self.argument_section = tk.Frame(self.view)
        self.argument_section.pack(fill=tk.X)
        
        row = tk.Frame(self.view)
        row.pack(fill=tk.X, expand=True)

        self.add = tk.Button(row, command=self.onClickAdd, text='Add')
        self.add.pack(side=tk.LEFT, padx=3)

        self.add = tk.Button(row, command=self.onClickTest, text='Test')
        self.add.pack(side=tk.LEFT, padx=3)

        separator = ttk.Separator(self.view, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=5)

        testLabel = tk.Label(self.view, text='Test Commands:')
        testLabel.pack(anchor=tk.W)

        self.run = tk.Button(self.view, command=self.onClickRun, text='Run')
        self.run.pack(anchor=tk.W)

        separator = ttk.Separator(self.view, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=5)

        seleniumLabel = tk.Label(self.view, text='Selenium Commands:')
        seleniumLabel.pack(anchor=tk.W)

        row = tk.Frame(self.view)
        row.pack(fill=tk.X, expand=True)

        self.start = tk.Button(row, command=self.onClickStart, text='Start')
        self.start.pack(side=tk.LEFT, padx=3)

        self.stop = tk.Button(row, command=self.onClickStop, text='Stop')
        self.stop.pack(side=tk.LEFT, padx=3)

    def addStep(self, step):
        row = tk.Frame(self.step_list)
        row.pack(fill=tk.X)

        label = tk.Label(row, text='#> {}.) {}'.format(len(self.steps), step.text))
        label.pack(anchor=tk.W)

    def onClickAdd(self):
        step = self.interaction_arguments.makeStep()
        self.steps.append(step)
        self.addStep(step)

    def onClickRun(self):
        if self.driver == None:
            self.onClickStart()

        for step in self.steps:
            step.execute(self.driver)

    def onClickStart(self):
        self.driver = webdriver.Firefox(executable_path=r'C:/Users/kylea/Documents/geckodriver.exe')

    def onClickTest(self):
        if self.driver == None:
            self.onClickStart()
            self.interaction_arguments.makeStep().execute(self.driver)
            self.onClickStop()
        else:
            self.interaction_arguments.makeStep().execute(self.driver)

    def onClickStop(self):
        self.driver.close()
        self.driver = None

    def onChangeInteraction(self, event):
        if self.interaction_arguments != None:
            self.interaction_arguments.clear()

        if self.interaction.get() == 'Click':
            self.interaction_arguments = ViewClick(self.argument_section)

        if self.interaction.get() == 'Navigate':
            self.interaction_arguments = ViewNavigate(self.argument_section)

        if self.interaction.get() == 'Input':
            self.interaction_arguments = ViewInput(self.argument_section)
        
