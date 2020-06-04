from view_interaction_part import ViewInteractionPart
from step_navigate import StepNavigate

class ViewNavigate(ViewInteractionPart):

    def __init__(self, parent):
        super().__init__(parent)
        self.makeStringArgument(parent, 'url')

    def makeStep(self):
        return StepNavigate(self.vars['url'].get())