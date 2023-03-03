

def create_dict_using_lists(list_one: list, list_two: list) -> dict:
    """
        Creating a new dictionary from two lists.
    :param list_one: List one will be treated as key in this dictionary.
    :param list_two: List two will be treated as key_value in this dictionary.
    :return: Generation of dictionary from two lists.
    """

    new_dict = {}
    for key in list_one:
        for value in list_two:
            new_dict[key] = value
            list_two.remove(value)
            break
    return new_dict


def get_final_date_verification(output_date) -> str:
    """
        Get the final date for testing verification on date picker calendar, lots of slicing done for data retrieval.
    :param output_date: The date which needs to be provided
    :return: Final date, for data verification.
    """

    output = output_date[:len(output_date) - 5]
    if output.__contains__(" 0"):
        date = output[-1:]
    else:
        date = output[-2:]
    month = output_date[0:3]
    final_date = month + " " + date
    date_with_space = final_date[-2:-1]
    if date_with_space is " ":
        final_date = month + date
    return final_date


def get_hours(time):
    """
        Getting Hours from time provided, if time was '11:40 PM', then it will return 11,
        if time was '3:20 PM', it will return 3, slicing has been done in that way.
    :param time: Input time in string format.
    :return: Final hour, extracting from hours.
    """

    time_length = len(time)
    if time_length == 7:
        hours = time[0:1]
    else:
        hours = time[0:2]
    return hours
