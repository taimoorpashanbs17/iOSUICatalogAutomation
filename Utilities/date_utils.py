import calendar
import time
import datetime
from randomtimestamp import random_time
from Utilities.TextFileUtils import write_text_file

_time_file = "time.txt"


def get_current_time_twelve_hours_format() -> str:
    """
        Get Current Time in 12 hours format i.e. if right now is 21:00 in 24 hours, then
            It will return 9:00 PM
            If time is less than 10, it will be returning 9:00, else 10. Slicing is done that way.
    :return: Current time with 12 hours format including PM and AM.
    """

    current_time = time.strftime("%I:%M %p")
    if current_time.startswith("0"):
        return current_time[1:8]
    return current_time


def get_time_ahead_of_current_time(number_of_hours: int) -> str:
    """
        Get the time ahead of some hours , i.e. if user needs to time 10 hours of current time ahead,
        we can have this function.
    :param number_of_hours: Number of hours, which needs to be entered in int.
    :return: Final time with 11:20 PM format.
    """

    nine_hours_from_now = datetime.datetime.now() + datetime.timedelta(hours=number_of_hours)
    time_after = '{:%I:%M %p}'.format(nine_hours_from_now)
    if time_after.startswith("0"):
        final_time = time_after[1:8]
    else:
        final_time = time_after
    return final_time


def generate_random_time():
    """
        Generate Random time from starting time will be current time
        and ending time will be 10 hours ahead of current time.
    """

    time_str = get_current_time_twelve_hours_format()
    time_object = datetime.datetime.strptime(time_str, '%I:%M %p').time()
    generated_time = random_time(start=time_object, text=True, pattern='%I:%M %p')
    if generated_time.startswith("0"):
        final_time = generated_time[1:]
    else:
        final_time = generated_time
    write_text_file(_time_file, final_time)


class DateUtils:
    _current_date = datetime.datetime.now()

    def get_current_date(self) -> int:
        """
            Get current date only, of current date, i.e. if today is 28th February 2023, It will return 23.
        :return: Returns date of current date in int type.
        """

        return self._current_date.day

    def get_current_month_in_text(self) -> str:
        """
            Get Current Month name in abbreviation i.e. if current month is 'February', it should be 'Feb'
        :return: Month name with three string character
        """

        month = self._current_date.month
        return calendar.month_abbr[month]

    def get_current_year(self) -> int:
        """
            Get current year only, of current date, i.e. if today is 28th February 2023, It will return 2023.
        :return: Returns year of current date in int type.
        """

        return self._current_date.year

    def get_current_date_for_date_wheel_picker(self) -> str:
        """
            Get Current Date for Date wheel picker test cases. i.e. if right now date
            is '28th February 2023', then it will return it with 'Feb 28, 2023'
        :return: current time and date for datepicker test case
        """

        date = self.get_current_date()
        month = self.get_current_month_in_text()
        year = self.get_current_year()
        return month+" " + str(date) + ", "+str(year)

    def get_current_date_time_for_time_picker(self) -> str:
        """
            Get Current Date and time for time wheel picker test cases. i.e. if right now time is '9:16 PM' and date
            is '28th February 2023', then it will return it with 'Feb 28, 2023 at 9:16 PM'
        :return: current time and date for datepicker test case
        """

        date = self.get_current_date()
        month = self.get_current_month_in_text()
        year = self.get_current_year()
        current_time = get_current_time_twelve_hours_format()
        return month+" " + str(date) + ", "+str(year)+" at "+current_time

    def get_list_from_current_date(self, date_format: str, range_number: int) -> list:
        """
            Get List of all dates or days as per their format and range number.
            i.e. If User wants dates till next or days and today is '8th February', then using
            "%B %d" and range is 7, will return
            ['February 08', 'February 09', 'February 10', 'February 11', 'February 12', 'February 13', 'February 14']

        :param date_format: Date format, where values needs to be got, most commonly, we are going to use "%B %d"
         and "%A"
         :param range_number: Range of till when you required data.
        :return: List of dates or days, showing the result based on format and range.
        """

        return [(self._current_date + datetime.timedelta(days=d)).strftime(date_format) for d in range(range_number)]
