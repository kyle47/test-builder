from view_interaction_part import ViewInteractionPart
from step_click import StepClick

class ViewClick(ViewInteractionPart):

    def __init__(self, parent):
        super().__init__(parent)
        self.makeStringArgument(parent, 'xpath')
        self.makeSelectArgument(parent, 'type', ['Selenium', 'Javascript'])

    def makeStep(self):
        return StepClick(self.vars['xpath'].get(), self.vars['type'].get())
