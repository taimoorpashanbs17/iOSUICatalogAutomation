import allure

from TestCases.BaseTest import BaseTest
from Screens.HomeScreen import HomeScreen
from Screens.SlidersScreen import SlidersScreen
from hamcrest import assert_that, equal_to, is_not


class TestSliders(BaseTest):
    @allure.title("Check Sliders Page Navigation")
    @allure.description("Test that Navigation between Sliders Screen and Home Screen is working as per requirement")
    def test_sliders_navigation(self):
        home_page = HomeScreen(self.driver)
        sliders_page = SlidersScreen(self.driver)
        home_page.click_on_sliders_link()
        assert_that(sliders_page.check_header_displaying(), equal_to(True))
        sliders_page.go_back()
        assert_that(home_page.check_ui_catalog_header_displaying(), equal_to(True))

    @allure.title("Check Sliders Page UI Presence")
    @allure.description("Test that UI Elements are displaying within Sliders screen")
    def test_sliders_ui_features(self):
        home_page = HomeScreen(self.driver)
        sliders_page = SlidersScreen(self.driver)
        home_page.click_on_sliders_link()
        assert_that(sliders_page.check_custom_slider_header_displaying(), equal_to(True))
        assert_that(sliders_page.check_tinted_slider_header_displaying(), equal_to(True))
        assert_that(sliders_page.check_default_slider_header_displaying(), equal_to(True))

    @allure.title('Check Sliders Feature')
    @allure.description('Test that all sliders are moving from their positions')
    def test_default_slider_functionality(self):
        home_page = HomeScreen(self.driver)
        sliders_page = SlidersScreen(self.driver)
        home_page.click_on_sliders_link()
        initial_value_of_default_slider = sliders_page.get_default_slider_value()
        sliders_page.move_default_slider('0.67')
        current_value_of_default_slider = sliders_page.get_default_slider_value()
        assert_that(initial_value_of_default_slider, is_not(current_value_of_default_slider))
        initial_value_of_tinted_slider = sliders_page.get_tinted_slider_value()
        sliders_page.move_tinted_slider('0.70')
        current_value_of_tinted_slider = sliders_page.get_tinted_slider_value()
        assert_that(initial_value_of_tinted_slider, is_not(current_value_of_tinted_slider))
        initial_value_of_custom_slider = sliders_page.get_custom_slider_value()
        sliders_page.move_custom_slider('0.20')
        current_value_of_custom_slider = sliders_page.get_custom_slider_value()
        assert_that(initial_value_of_custom_slider, is_not(current_value_of_custom_slider))
