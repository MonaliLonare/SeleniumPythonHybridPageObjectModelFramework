from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_text_field_name = "firstname"
    last_name_text_field_name = "lastname"
    email_address_text_field_name = "email"
    telephone_text_field_name = "telephone"
    password_text_field_name = "password"
    confirm_password_field_id = "input-confirm"
    privacy_policy_check_box_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_radio_button_name = "newsletter"
    email_address_already_registered_warning_text_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_text_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_text_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_text_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_address_warning_text_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_text_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_text_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name):
        self.type_into_element(first_name, "first_name_text_field_name", self.first_name_text_field_name)

    def enter_last_name(self, last_name):
        self.type_into_element(last_name, "last_name_text_field_name", self.last_name_text_field_name)

    def enter_email_address(self, email):
        self.type_into_element(email, "email_address_text_field_name", self.email_address_text_field_name)

    def enter_telephone_text_field(self, telephone):
        self.type_into_element(telephone, "telephone_text_field_name", self.telephone_text_field_name)

    def enter_password_text_field(self, password):
        self.type_into_element(password, "password_text_field_name", self.password_text_field_name)

    def enter_confirm_password_field(self, confirm_password):
        self.type_into_element(confirm_password, "confirm_password_field_id", self.confirm_password_field_id)

    def click_on_privacy_policy_check_box_field(self):
        self.element_click("privacy_policy_check_box_field_name", self.privacy_policy_check_box_field_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_on_newsletter_radio_button(self):
        self.element_click("newsletter_radio_button_name", self.newsletter_radio_button_name)

    def register_an_account(self, first_name, last_name, email_address, telephone_text_field, password_text_field,
                            confirm_password_field, yes_or_no, privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_address(email_address)
        self.enter_telephone_text_field(telephone_text_field)
        self.enter_password_text_field(password_text_field)
        self.enter_confirm_password_field(confirm_password_field)
        if yes_or_no.__eq__("yes"):
            self.select_yes_on_newsletter_radio_button()
        if privacy_policy.__eq__("select"):
            self.click_on_privacy_policy_check_box_field()
        return self.click_on_continue_button()

    def retrieve_email_address_already_registered_warning_text(self):
        return self.retrieve_element_text("email_address_already_registered_warning_text_xpath",
                                          self.email_address_already_registered_warning_text_xpath)

    def retrieve_privacy_policy_warning_text(self):
        return self.retrieve_element_text("privacy_policy_warning_text_xpath", self.privacy_policy_warning_text_xpath)

    def retrieve_first_name_warning_text(self):
        return self.retrieve_element_text("first_name_warning_text_xpath", self.first_name_warning_text_xpath)

    def retrieve_last_name_warning_text(self):
        return self.retrieve_element_text("last_name_warning_text_xpath", self.last_name_warning_text_xpath)

    def retrieve_email_address_warning_text(self):
        return self.retrieve_element_text("email_address_warning_text_xpath", self.email_address_warning_text_xpath)

    def retrieve_telephone_warning_text(self):
        return self.retrieve_element_text("telephone_warning_text_xpath", self.telephone_warning_text_xpath)

    def retrieve_password_warning_text(self):
        return self.retrieve_element_text("password_warning_text_xpath", self.password_warning_text_xpath)

    def verify_all_warnings(self, expected_privacy_policy_warning_message, expected_first_name_warning_message,
                            expected_last_name_warning_message, expected_email_warning_message,
                            expected_telephone_warning_message, expected_password_warning_message):
        actual_privacy_policy_warning_message = self.retrieve_privacy_policy_warning_text()
        actual_first_name_warning_message = self.retrieve_first_name_warning_text()
        actual_last_name_warning_message = self.retrieve_last_name_warning_text()
        actual_email_warning_message = self.retrieve_email_address_warning_text()
        actual_telephone_warning_message = self.retrieve_telephone_warning_text()
        actual_password_warning_message = self.retrieve_password_warning_text()

        status = False

        if expected_privacy_policy_warning_message.__contains__(actual_privacy_policy_warning_message):
            if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
                if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                    if expected_email_warning_message.__eq__(actual_email_warning_message):
                        if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_password_warning_message):
                                status = True

        return status
