from step import Step

class StepInput(Step):

    def __init__(self, xpath, value):
        super().__init__()
        self.xpath = xpath
        self.value = value
        self.text = "Input '{}' into element located by '{}'".format(self.value, self.xpath)

    def execute(self, driver):
        driver.find_element_by_xpath(self.xpath).send_keys(self.value)