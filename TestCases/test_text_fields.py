import allure
import pytest

from Screens.TextFieldScreen import TextFieldScreen
from TestCases.BaseTest import BaseTest
from Screens.HomeScreen import HomeScreen
from hamcrest import assert_that, equal_to, is_not


class TestTextFields(BaseTest):
    """
        All Test cases of Text Fields Screen should be handled here.

    """

    @allure.title("Check Text Fields Page Navigation")
    @allure.description("Test that Navigation between Text Fields Screen and Home Screen is working as per requirement")
    @pytest.mark.functional
    def test_text_fields_navigation(self):
        """
        In this test, we are handling navigation, which is :

            1. App goes to 'Text Fields' Link and clicks.
            2. Verifies that user is in 'Text Fields' page, by presence of 'Text Fields' Header.
            3. Goes Back to Home Page.
            4. Verifies that 'UI Catalog' page is displaying or not.
        """

        home_page = HomeScreen(self.driver)
        text_fields_page = TextFieldScreen(self.driver)
        home_page.click_on_text_fields_link()
        assert_that(text_fields_page.check_header_displaying(), equal_to(True))
        text_fields_page.go_back()
        assert_that(home_page.check_ui_catalog_header_displaying(), equal_to(True))

    @allure.title("Check Text Fields Page UI Presence")
    @allure.description("Test that UI Elements are displaying within Text Fields screen")
    @pytest.mark.ui
    def test_text_fields_ui_features(self):
        """
        In this test, we are verifying UI properties within "Text Fields" Page, as Text Fields contains
        five different text fields i.e. Default, Tinted, Custom, Secure and specific Keyword, Test case will
        be like:

            1. App goes to 'Text Fields' Link and clicks.
            2. Verifies presence of all text fields headers.
            3. Verifies presence of all text fields.
        """

        home_page = HomeScreen(self.driver)
        text_fields_page = TextFieldScreen(self.driver)
        home_page.click_on_text_fields_link()
        assert_that(text_fields_page.check_default_text_field_header_displaying(), equal_to(True))
        assert_that(text_fields_page.check_default_text_field_displaying(), equal_to(True))
        assert_that(text_fields_page.check_tinted_text_field_header_displaying(), equal_to(True))
        assert_that(text_fields_page.check_tinted_text_field_displaying(), equal_to(True))
        assert_that(text_fields_page.check_secure_text_field_header_displaying(), equal_to(True))
        assert_that(text_fields_page.check_secure_text_field_displaying(), equal_to(True))
        assert_that(text_fields_page.check_specific_keyword_text_field_header_displaying(), equal_to(True))
        assert_that(text_fields_page.check_specific_keyword_text_field_displaying(), equal_to(True))
        assert_that(text_fields_page.check_custom_text_field_header_displaying(), equal_to(True))
        assert_that(text_fields_page.check_custom_text_field_displaying(), equal_to(True))

    @allure.title("Check Text Fields Feature")
    @allure.description("Test that all Text Fields are working fine after entering values and showing exact values")
    @pytest.mark.functional
    @pytest.mark.parametrize("default_field_value, tinted_field_value, specific_key_word_field_value, "
                             "custom_field_value", [("This is Testing Default Value", "This is Testing Tinted Value",
                                                     "This is Testing Specific Keyword Value",
                                                     "This is Testing Custom Field Value")])
    def test_text_fields_functionality(self, default_field_value, tinted_field_value, specific_key_word_field_value,
                                       custom_field_value):
        """
        In this test,  we are handling functionality of four text fields i.e. 'Default', 'Tinted', 'Specific Keyword'
        and 'Custom', coverage contains:
         1. App goes to 'Text Fields' Link and clicks.
         2. Enter values on one field.
         3. Verify that placeholder text i.e. 'Placeholder text' shouldn't be displaying at all.
         4. Verify that value which is added, should be displaying.
        """

        home_page = HomeScreen(self.driver)
        text_fields_page = TextFieldScreen(self.driver)
        home_page.click_on_text_fields_link()
        text_fields_page.enter_value_on_default_text_field(default_field_value)
        assert_that(text_fields_page.get_value_from_default_text_field(), is_not("Placeholder text"))
        assert_that(text_fields_page.get_value_from_default_text_field(), equal_to(default_field_value))
        text_fields_page.enter_value_on_tinted_text_field(tinted_field_value)
        assert_that(text_fields_page.get_value_from_tinted_text_field(), is_not("Placeholder text"))
        assert_that(text_fields_page.get_value_from_tinted_text_field(), equal_to(tinted_field_value))
        text_fields_page.enter_value_on_specific_keyword_text_field(specific_key_word_field_value)
        assert_that(text_fields_page.get_value_from_specific_keyword_text_field(), is_not("Placeholder text"))
        assert_that(text_fields_page.get_value_from_specific_keyword_text_field(),
                    equal_to(specific_key_word_field_value))
        text_fields_page.enter_value_on_custom_text_field(custom_field_value)
        assert_that(text_fields_page.get_value_from_custom_text_field(), is_not("Placeholder text"))
        assert_that(text_fields_page.get_value_from_custom_text_field(), equal_to(custom_field_value))

    @allure.title("Check Secure Text Field Feature")
    @allure.description("Test that Secure Text field is working as per requirement")
    @pytest.mark.functional
    @pytest.mark.parametrize("secure_field_value", ["This is Testing Secure Default Value"])
    def test_secure_text_field_functionality(self, secure_field_value):
        """
        In this test, we are handling functionality of 'Secure' Text field, in such a way:
            1. App goes to 'Text Fields' Link and clicks.
            2. Enter value in 'Secure' field.
            3. Make Sure that text field of 'Secure' is not empty.
            4. Check number of string enters is exactly same as it was entered.
            5. Click on 'Cross button' of field.
            6. Verify that 'Placeholder Text' should be displaying.

        """

        home_page = HomeScreen(self.driver)
        text_fields_page = TextFieldScreen(self.driver)
        home_page.click_on_text_fields_link()
        text_fields_page.enter_value_on_secure_field(secure_field_value)
        assert_that(text_fields_page.get_value_from_secure_text_field(), is_not(""))
        length_of_entered_string = len(text_fields_page.get_value_from_secure_text_field())
        length_of_expected_string = len(secure_field_value)
        expected_text_within_secure_field = length_of_expected_string * '•'
        assert_that(text_fields_page.get_value_from_secure_text_field(),
                    equal_to(expected_text_within_secure_field))
        assert_that(length_of_expected_string, equal_to(length_of_entered_string))
        text_fields_page.click_on_cross_button_on_secure_text()
        assert_that(text_fields_page.get_value_from_secure_text_field(), equal_to("Placeholder text"))
