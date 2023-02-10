from Screens.BasePage import BasePage
from Utilities.date_utils import DateUtils
from Utilities.MiscUtils import create_dict_using_lists
from Utilities.TextFileUtils import read_text_file, write_text_file

import random


_date_file = "date.txt"
_day_file = "day.txt"


def get_dict_of_day_date() -> dict:
    """
        Getting date and day dictionary here, as it will be getting from today till next days,
        we are deleting first digits, also implementation on dates list is we are going to eliminate '0' from
        the dates like '09' or '08', it will be like '9' or '8'.
    :return: Dictionary will be generated of dates and days for next 8 days.
    """

    get_dates = DateUtils().get_list_from_current_date("%B %d %Y", 8)
    dates = [sub.replace(' 0', ' ') for sub in get_dates]
    days = DateUtils().get_list_from_current_date("%A", 8)
    dates.pop(0)
    days.pop(0)
    dates_days = create_dict_using_lists(dates, days)
    return dates_days


def get_day_date():
    """
        Getting date and day dictionary from where, random date from dictionary will be picked,
        and its day as well and the end , both of them will be stored on different files.
    """

    day_date_dict = get_dict_of_day_date()
    random_date = random.choice(list(day_date_dict))
    day_to_select = day_date_dict[random_date]
    write_text_file(_date_file, random_date)
    write_text_file(_day_file, day_to_select)


def get_date_file_name() -> str:
    """
        Get name of date file
    :return: String name of file.
    """
    return _date_file


class DatePickerScreen(BasePage):
    """
        All Action items of Date Picker Screen will be mentioned there.
    """

    def __int__(self, driver):
        super().__init__(driver)

    def check_header_displaying(self) -> bool:
        """
            Check that Header of 'Date Picker' at top displaying.
        :return: Boolean value of 'True' or 'False'.
        """

        return self.check_element_displaying_or_not('DATE_PICKER_HEADER_CLASS_NAME')

    def go_back_to_home(self):
        """
            Navigate back to Home Page.
        """

        self.go_back()

    def check_date_button_displaying(self) -> bool:
        """
            Check Date Button is displaying or not.
        :return: Boolean value of 'True' or 'False'.
        """

        return self.check_element_displaying_with_index_or_not("DATE_PICKER_BUTTON_CLASS_NAME", 2)

    def check_time_button_displaying(self) -> bool:
        """
            Check Time Button is displaying or not.
        :return: Boolean value of 'True' or 'False'.
        """

        return self.check_element_displaying_with_index_or_not("DATE_PICKER_BUTTON_CLASS_NAME", 3)

    def check_date_button_clickable(self) -> bool:
        """
            Check Date Button is clickable or not.
        :return: Boolean value of 'True' or 'False'.
        """

        return self.check_element_is_clickable_with_index_or_not("DATE_PICKER_BUTTON_CLASS_NAME", 2)

    def check_time_button_clickable(self) -> bool:
        """
            Check Time Button is clickable or not.
        :return: Boolean value of 'True' or 'False'.
        """

        return self.check_element_is_clickable_with_index_or_not("DATE_PICKER_BUTTON_CLASS_NAME", 3)

    def check_time_result_displaying(self) -> bool:
        """
            Check Final Time and Date result is displaying or not.
        :return: Boolean value of 'True' or 'False'.
        """

        return self.check_element_displaying_with_index_or_not("DATE_TIME_TEXT_CLASS_NAME", 1)

    def get_final_time_text(self) -> str:
        """
            Get Final Date and Time result value
        :return: String form of value
        """

        return self.get_attribute_value_of_element_with_index("DATE_TIME_TEXT_CLASS_NAME", 'value', 1)

    def click_on_date_wheel_picker_button(self):
        """
            Click on Date Wheel Picker button.
        """

        self.click_with_index("DATE_PICKER_BUTTON_CLASS_NAME", 2)

    def select_date_for_date_picker(self):
        """
            Execute Method of get_day_date, where it will generate all functionalities of that method,
            then extract values from two different files i.e. 'date.txt' and 'day.txt', from there, it will
            create a xpath, that xpath value will be used within date wheeler method and then, it will tap
            on space.
        """

        get_day_date()
        random_date_generated = read_text_file(_date_file)
        length_of_date = len(random_date_generated)
        date = random_date_generated[: length_of_date-5]
        day = read_text_file(_day_file)
        date_day_xpath = day+", "+date
        self.click_web_element_locator_for_date_wheeler(date_day_xpath)
        self.tap_without_interacting_with_element(142, 181)

    def get_value_date_wheel_picker(self) -> str:
        """
            Get the Value of 'Label' tag of Date Wheel Picker.
        :return: String Value of Date Picker Wheeler.
        """

        return self.get_attribute_value_of_element_with_index("DATE_PICKER_BUTTON_CLASS_NAME", "label", 2)

    def get_current_month_value_fro_date_wheel_picker(self) -> str:
        """
            Get Current month value from
        :return:
        """
        return self.get_attribute_value_of_element_with_index("XCUIElementTypeOther", "label", 19)

    def click_on_time_picker_wheeler(self):
        self.click_with_index("DATE_PICKER_BUTTON_CLASS_NAME", 3)

    def enter_hours(self, hours):
        self.send_text_with_index("TIME_PICKER_WHEELER_CLASS_NAME", 0, hours)

    def enter_minutes(self, mints):
        self.send_text_with_index("TIME_PICKER_WHEELER_CLASS_NAME", 1, mints)

    def enter_am_pm(self, am_pm):
        self.send_text_with_index("TIME_PICKER_WHEELER_CLASS_NAME", 2, am_pm)
        self.tap_without_interacting_with_element(142, 181)
