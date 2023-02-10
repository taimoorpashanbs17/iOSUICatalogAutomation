import logging

from Utilities.LogUtil import Logger
from Utilities import configReader
from appium.webdriver.common.appiumby import AppiumBy

from appium.webdriver.common.touch_action import TouchAction

log = Logger(__name__, logging.INFO)


def get_name(locator_name: str) -> str:
    """
        Get the name of the locator, as we have get name of locator from ini file, where locator names are like
        'OK_CANCEL_BUTTON_XPATH', so it will return the name of locator.
    :param locator_name: Name of the locator from ini file.
    :return: Name of the locator, without dashes and with title format.
    """

    list_of_locators = ['_XPATH', '_ID', '_CLASS_NAME', '_NAME', '_ACCESSIBILITYID']
    for word in list_of_locators:
        locator_name = locator_name.replace(word, "")
    return locator_name.replace("_", " ").title()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = TouchAction(self.driver)

    def get_locator(self, locator: str):
        """
            Get the locator, as there are many options to interact with locator
        :param locator: Name of the locator, we have to pass here.
        :return: Final element, which we can send to perform any activity.
        """

        element = None
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(AppiumBy.XPATH, configReader.read_config("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.read_config("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(AppiumBy.ID, configReader.read_config("locators", locator))
        elif str(locator).endswith("_CLASS_NAME"):
            element = self.driver.find_element(AppiumBy.CLASS_NAME, configReader.read_config("locators", locator))
        elif str(locator).endswith("_NAME"):
            element = self.driver.find_element(AppiumBy.NAME, configReader.read_config("locators", locator))
        return element

    def get_locator_for_list(self, locator: str):
        """
            Get the locator, as there are many options to interact with locator
        :param locator: Name of the locator, we have to pass here.
        :return: Final element, which we can send to perform any activity.
        """

        element = None
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_elements(AppiumBy.XPATH, configReader.read_config("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID,
                                                configReader.read_config("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_elements(AppiumBy.ID, configReader.read_config("locators", locator))
        elif str(locator).endswith("_CLASS_NAME"):
            element = self.driver.find_elements(AppiumBy.CLASS_NAME, configReader.read_config("locators", locator))
        elif str(locator).endswith("_NAME"):
            element = self.driver.find_elements(AppiumBy.NAME, configReader.read_config("locators", locator))
        return element

    def click(self, locator):
        """
            Click on any locator, which user have to interact with.
        :param locator: locator, which user wants to interact.
        """

        locator_name = get_name(locator)
        BasePage(self.driver).get_locator(locator).click()
        log.logger.info("Clicking on " + str(locator_name))

    def click_with_index(self, locator: str, index: int):
        """
             Click on any locator, which user have to interact by passing index, since we are using list here.
         :param locator: locator, which user wants to interact.
         :param index: number of index of element, which we can to index.
         """

        locator_name = get_name(locator)
        BasePage(self.driver).get_locator_for_list(locator)[index].click()
        log.logger.info("Clicking on " + str(locator_name) + " with index : " + str(index))

    def send_text_with_index(self, locator: str, index: int, value: str):
        """
            Enter value on any locator, which user have to interact with. using indexing.
        :param locator: locator, which user wants to interact.
        :param index: number of index of element, which we can to index.
        :param value: String character value, which needs to be entered.
        :return:
        """

        locator_name = get_name(locator)
        BasePage(self.driver).get_locator_for_list(locator)[index].send_keys(value)
        log.logger.info("Typing in " + str(locator_name) + " with index : " + str(index) + " entered the "
                                                                                           "value as"
                                                                                           ": " + str(value))

    def send_text(self, locator: str, value: str):
        """
            Enter value on any locator, which user have to interact with.
        :param locator: locator, which user wants to interact.
        :param value: String character value, which needs to be entered.
        """

        locator_name = get_name(locator)
        BasePage(self.driver).get_locator(locator).send_keys(value)
        log.logger.info("Typing in " + str(locator_name) + " and entered the value as : " + str(value))

    def get_text(self, locator: str):
        locator_name = get_name(locator)
        text = BasePage(self.driver).get_locator(locator).text
        log.logger.info("Getting Text of  " + str(locator_name) + "")
        return text

    def check_element_displaying_or_not(self, locator: str) -> bool:
        """
            Check that element is displaying or not.
        :param locator: locator, which we have to interact with.
        :return: Boolean value of 'True' or 'False'.
        """

        locator_name = get_name(locator)
        displaying_status = BasePage(self.driver).get_locator(locator).is_displayed()
        log.logger.info(locator_name + " is displaying. ")
        return displaying_status

    def check_element_clickable_or_not(self, locator: str) -> bool:
        """
            Check that element is clickable or not.
        :param locator: locator, which we have to interact with.
        :return: Boolean value of 'True' or 'False'.
        """

        locator_name = get_name(locator)
        clickable_status = BasePage(self.driver).get_locator(locator).is_enabled()
        log.logger.info(locator_name + " is clickable. ")
        return clickable_status

    def check_element_displaying_with_index_or_not(self, locator: str, index_number: int) -> bool:
        """
            Check that element is displaying or not, as we are going to have elements with same locators, so we have to
            create list for that.
        :param locator: locator, which we have to interact with.
        :param index_number: Get index number of list, in order to interact with exact element.
        :return: Boolean value of 'True' or 'False'.
        """

        locator_name = get_name(locator)
        displaying_status = BasePage(self.driver).get_locator_for_list(locator)[index_number].is_displayed()
        log.logger.info(locator_name + " with index " + str(index_number) + " is displaying. ")
        return displaying_status

    def check_element_is_clickable_with_index_or_not(self, locator: str, index_number: int) -> bool:
        """
            Check that element is clickable or not, as we are going to have elements with same locators, so we have to
            create list for that.
        :param locator: locator, which we have to interact with.
        :param index_number: Get index number of list, in order to interact with exact element.
        :return: Boolean value of 'True' or 'False'.
        """

        locator_name = get_name(locator)
        clickable_status = BasePage(self.driver).get_locator_for_list(locator)[index_number].is_enabled()
        log.logger.info(locator_name + " with index " + str(index_number) + " is clickable. ")
        return clickable_status

    def go_back(self):
        """
            Navigating back to previous screen
        """

        log.logger.info("Going Back ...")
        self.driver.back()

    def get_attribute_value_of_element(self, locator: str, attribute_name: str) -> str:
        """
            Get Value of any Web Element attribute, for example value, type, href etc.
        :param locator: locator, which we have to interact with.
        :param attribute_name: Name of the attribute, which value we need.
        :return: String value of the attribute.
        """

        locator_name = get_name(locator)
        value = BasePage(self.driver).get_locator(locator).get_attribute(attribute_name)
        log.logger.info(attribute_name.title() + " of " + str(locator_name) + " is " + value)
        return value

    def get_attribute_value_of_element_with_index(self, locator: str, attribute_name: str, index_number: int):
        """
            Get Value of any Web Element attribute, for example value, type, href etc.
        :param locator: locator, which we have to interact with.
        :param attribute_name: Name of the attribute, which value we need.
        :param index_number: Get index number of list, in order to interact with exact element.
        :return: String value of the attribute, which user asked.
        """

        locator_name = get_name(locator)
        value = BasePage(self.driver).get_locator_for_list(locator)[index_number].get_attribute(attribute_name)
        log.logger.info(attribute_name.title() + " of " + str(locator_name) + " with index " + str(index_number) +
                        " is " + value)
        return value

    def scroll_up_down_till_text_shown(self, locator: str, axis_x, axis_y1: int, axis_y2: int):
        """
            Scrolling vertically either top to bottom or bottom to top using axis, as x-axis remains same, since we
            are scrolling vertically.
        :param locator: locator, which we have to interact with.
        :param axis_x: Coordinate values in int, from where to start interact on x-axis.
        :param axis_y1: Starting point of y-axis coordinate.
        :param axis_y2: Ending point of y-axis coordinate.
        """

        i = 0
        locator_name = get_name(locator)
        position = None
        while BasePage(self.driver).get_locator(locator).is_displayed():
            self.action.press(axis_x, axis_y1).wait(2000).press(axis_x, axis_y2).perform()
            i += 0
        if axis_y1 > axis_y2:
            position = "Down"
        elif axis_y1 < axis_y2:
            position = "Up"
        log.logger.info("Scrolling " + position + " to " + str(locator_name))

    def click_web_element_locator_for_date_wheeler(self, date_day: str):
        """
            Separate helper created for Date picker wheeler, so that we can select element on date basis.
        :param date_day: Mentioning date or day or time in order to interact with element.
        :return: Locator, which can be used to interact with element.
        """

        xpath = '//XCUIElementTypeButton[@name="'+date_day+'"]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
        log.logger.info("Clicking on date and day of "+date_day)

    def tap_without_interacting_with_element(self, x_axis: int, y_axis: int):
        """
            Tapping on any area of the screen using coordinates
        :param x_axis: value of x-axis with int.
        :param y_axis: value of y-axis with int.
        """

        TouchAction(self.driver).tap(None, x_axis, y_axis, 1).perform()

    def scroll_up_down(self, axis_x, axis_y1: int, axis_y2: int):
        """
            Scrolling vertically either top to bottom or bottom to top using axis, as x-axis remains same, since we
            are scrolling vertically.
        :param axis_x: Coordinate values in int, from where to start interact on x-axis.
        :param axis_y1: Starting point of y-axis coordinate.
        :param axis_y2: Ending point of y-axis coordinate.
        """

        self.action.press(axis_x, axis_y1).wait(2000).press(axis_x, axis_y2).perform()
