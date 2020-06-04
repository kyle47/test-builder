from view_interaction_part import ViewInteractionPart
from step_input import StepInput

class ViewInput(ViewInteractionPart):

    def __init__(self, parent):
        super().__init__(parent)
        self.makeStringArgument(parent, 'xpath')
        self.makeStringArgument(parent, 'value')

    def makeStep(self):
        return StepInput(self.vars['xpath'].get(), self.vars['value'].get())
