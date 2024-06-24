from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from Utilities import ExcelUtils
from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/Tutorialsninja.xlsx", "RegisterTest", 2, 1),
            ExcelUtils.get_cell_data("ExcelFiles/Tutorialsninja.xlsx", "RegisterTest", 2, 2),
            self.generate_email_with_time_stamp(), "1234567890", "12345", "12345", "no", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.display_status_of_account_created_text().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Monali", "Lonare",
                                                                 self.generate_email_with_time_stamp(), "1234567890",
                                                                 "12345", "12345", "yes", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.display_status_of_account_created_text().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Monali", "Lonare", "lonaremona123@gmail.com", "1234567890", "12345", "12345",
                                          "yes", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_email_address_already_registered_warning_text().__contains__(
            expected_warning_message)

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")
