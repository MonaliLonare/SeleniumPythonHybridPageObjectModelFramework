from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    your_account_has_been_created_text_xpath = "//div[@id='content']/h1"

    def display_status_of_account_created_text(self):
        return self.retrieve_element_text("your_account_has_been_created_text_xpath",self.your_account_has_been_created_text_xpath)
