from step import Step

class StepClick(Step):

    def __init__(self, xpath, type):
        super().__init__()
        self.xpath = xpath
        self.type = type
        self.text = "Click the element located by '{}' ({})".format(xpath, type)
        
    def execute(self, driver):
        element = driver.find_element_by_xpath(self.xpath)

        if self.type == 'Javascript':
            driver.execute_script('arguments[0].click()', element)
        else:
            element.click()
        