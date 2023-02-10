import allure
import pytest

import logging
from Utilities.LogUtil import Logger

from Screens.DatePickerScreen import DatePickerScreen
from Screens.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from hamcrest import assert_that, equal_to
from Utilities.date_utils import DateUtils, generate_random_time
from Utilities.MiscUtils import get_final_date_verification, get_hours
from Utilities.TextFileUtils import read_text_file
from Screens.DatePickerScreen import get_date_file_name

log = Logger(__name__, logging.INFO)


class TestDatePicker(BaseTest):

    @allure.title("Check Date Picker Page Navigation")
    @allure.description("Test that Navigation between Date Picker Screen and Home Screen is working as per requirement")
    @pytest.mark.functional
    def test_text_fields_navigation(self):
        """
        In this test, we are handling navigation, which is :

            1. App goes to 'Date Picker' Link and clicks.
            2. Verifies that user is in 'Date Picker' page, by presence of 'Date Picker' Header.
            3. Goes Back to Home Page.
            4. Verifies that 'UI Catalog' page is displaying or not.
        """

        home_page = HomeScreen(self.driver)
        date_picker_page = DatePickerScreen(self.driver)
        home_page.click_on_date_picker_link()
        assert_that(date_picker_page.check_header_displaying(), equal_to(True))
        date_picker_page.go_back()
        assert_that(home_page.check_ui_catalog_header_displaying(), equal_to(True))

    @allure.title("Check Date Picker Page UI Presence")
    @allure.description("Test that UI Elements are displaying within Date Picker screen")
    @pytest.mark.ui
    def test_text_fields_ui_features(self):
        """
        In this test, we are verifying UI properties within "Date Picker" Page, in which we can see three things,
        i.e. Time Button, Date Button and Final time/Date result., so Test case will be:
            1. App goes to 'Date Picker' Link and clicks.
            2. Verifies that Time Button is displaying and able to clickable.
            3. Verifies that Date Button is displaying and able to clickable.
            4. Final Output displaying and showing current date and time.
        """

        home_page = HomeScreen(self.driver)
        date_picker_page = DatePickerScreen(self.driver)
        home_page.click_on_date_picker_link()
        assert_that(date_picker_page.check_date_button_displaying(), equal_to(True))
        assert_that(date_picker_page.check_date_button_clickable(), equal_to(True))
        assert_that(date_picker_page.check_time_button_displaying(), equal_to(True))
        assert_that(date_picker_page.check_time_button_clickable(), equal_to(True))
        assert_that(date_picker_page.check_time_result_displaying(), equal_to(True))
        assert_that(date_picker_page.get_final_time_text(),
                    equal_to(DateUtils().get_current_date_time_for_time_picker()))

    @allure.title("Check Date Picker functionality")
    @allure.description("Test that Date Picker functionality is working fine")
    @pytest.mark.functional
    def test_date_wheel_picker_functionality(self):
        home_page = HomeScreen(self.driver)
        date_picker_page = DatePickerScreen(self.driver)
        home_page.click_on_date_picker_link()
        date_picker_page.click_on_date_wheel_picker_button()
        date_picker_page.select_date_for_date_picker()
        date_file = read_text_file(get_date_file_name())
        date = get_final_date_verification(date_file)
        year = read_text_file(get_date_file_name())[-4:]
        date_to_verified = date+", "+year
        assert_that(date_picker_page.get_value_date_wheel_picker(), equal_to(date_to_verified))

    @allure.title("Check Time Wheel Picker functionality")
    @allure.description("Test that Time Wheel picker functionality is working fine")
    @pytest.mark.functional
    def test_time_wheel_picker_functionality(self):
        generate_random_time()
        data = read_text_file("time.txt")
        hours = get_hours(data)
        mints = data[-5:-3]
        am_pm = data[-3:]
        home_page = HomeScreen(self.driver)
        date_picker_page = DatePickerScreen(self.driver)
        home_page.click_on_date_picker_link()
        date_picker_page.click_on_time_picker_wheeler()
        date_picker_page.enter_hours(hours)
        date_picker_page.enter_minutes(mints)
        date_picker_page.enter_am_pm(am_pm)
        log.logger.info(data + " was successfully added as Time")
