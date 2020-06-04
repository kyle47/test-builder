from step import Step

class StepNavigate(Step):

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.text = "Navigate to '{}'".format(self.url)

    def execute(self, driver):
        driver.get(self.url)