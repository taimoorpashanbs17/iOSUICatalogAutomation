import pytest
import allure

from TestCases.BaseTest import BaseTest
from Screens.HomeScreen import HomeScreen
from Screens.ActionSheetsScreen import ActionSheetsScreen
from hamcrest import assert_that, equal_to


class TestActionSheets(BaseTest):

    @allure.title("Test Action Sheets Navigation")
    @allure.description("Check that navigation from Action sheets and Home Page going smooth or not")
    def test_action_sheets_navigation(self):
        home_page = HomeScreen(self.driver)
        action_sheets_page = ActionSheetsScreen(self.driver)
        home_page.click_on_action_sheets_link()
        assert_that(action_sheets_page.check_header_displaying(), equal_to(True))
        action_sheets_page.go_back_to_home()
        assert_that(home_page.check_ui_catalog_header_displaying(), equal_to(True))

    @allure.title("Test OK and Cancel Button Functionality")
    @allure.description("Check that Ok and Cancel Button are working fine or not")
    def test_ok_cancel_button_functionality(self):
        home_page = HomeScreen(self.driver)
        action_sheets_page = ActionSheetsScreen(self.driver)
        home_page.click_on_action_sheets_link()
        action_sheets_page.tap_on_ok_cancel_button()
        action_sheets_page.tap_on_ok_button()
        action_sheets_page.tap_on_ok_cancel_button()
        action_sheets_page.tap_on_cancel_button()

    @allure.title("Check UI Features of Action Sheets")
    @allure.description("Check all UI Features of Action sheets are there")
    def test_action_sheets_ui_features(self):
        home_page = HomeScreen(self.driver)
        action_sheets_page = ActionSheetsScreen(self.driver)
        home_page.click_on_action_sheets_link()
        assert_that(action_sheets_page.check_ok_cancel_button_displaying(), equal_to(True))
        assert_that(action_sheets_page.check_other_button_displaying(), equal_to(True))

    @allure.title("Test Other Button Functionality")
    @allure.description("Check that Other Button is working fine as per requirement")
    def test_other_button_functionality(self):
        home_page = HomeScreen(self.driver)
        action_sheets_page = ActionSheetsScreen(self.driver)
        home_page.click_on_action_sheets_link()
        action_sheets_page.click_other_button()
        action_sheets_page.click_destructive_button()
        action_sheets_page.click_other_button()
        action_sheets_page.click_safe_choice_button()
        action_sheets_page.go_back_to_home()
        assert_that(home_page.check_ui_catalog_header_displaying(), equal_to(True))
