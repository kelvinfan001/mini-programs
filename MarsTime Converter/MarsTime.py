"""
MarsTime Converter Module

Instructions:
Excel dates in a plain text file named 'excel_time.txt' will be converted into
Mars time and written on a plain text file named 'marstime.txt'
"""
from typing import List
import math

path = 'excel_time.txt'
new_path = 'marstime.txt'

time_file = open(path, 'r')
time_file_string = time_file.read()
time_list = time_file_string.split('\n')

marstime_file = open(new_path, 'w')


def remove_time(timelist: list) -> None:
    """
    Remove the time from all times in timelist.

    >>> time = ['42839.33194', '42843.4436', '42844.10072']
    >>> remove_time(time)
    >>> time
    [42839, 42843, 42844]
    """

    for i in range(len(timelist)):
        timelist[i] = int(float(timelist[i]))


def create_mars_format(mars_time_info: list) -> str:
    """
    Return a new date in MarsTime format based on date.

    Precondition:
    date contains four items.
    Index 0 of date contains year;
    Index 1 of date contains period;
    Index 2 of date contains week;
    Index 3 of date contains day.

    >>> create_mars_format([2018, 6, 2, 6])
    'Y2018P6W2D6'
    """

    if len(mars_time_info) != 4:
        raise Exception

    return 'Y{}P{}W{}D{}'.format(str(mars_time_info[0]), str(mars_time_info[1]),
                                 str(mars_time_info[2]), str(mars_time_info[3]))


def convert_2017_base(original_base: int) -> int:
    """
    Return a date in 2017 base based on original_base. (Convert to number of
    days after December 31, 2016.

    >>> convert_2017_base(42839)
    104
    >>> convert_2017_base(42736)
    1
    """

    return original_base - 42735


def convert_mars_time_info(excel_date: int) -> List[int]:
    """
    Return a date in list form in MarsTime information.

    Precondition: excel_year is converted to 2017 base (number of days after
    December 31, 2016)

    >>> convert_mars_time_info(1)
    [2017, 1, 1, 1]
    >>> convert_mars_time_info(104)
    [2017, 4, 3, 6]
    >>> convert_mars_time_info(366)
    [2018, 1, 1, 2]
    >>> convert_mars_time_info(2555)
    [2023, 13, 4, 7]
    >>> convert_mars_time_info(2435)
    [2023, 9, 3, 6]
    >>> convert_mars_time_info(2191)
    [2022, 13, 4, 7]
    >>> convert_mars_time_info(728)
    [2018, 13, 4, 7]
    """

    # get year
    if excel_date in range(1, 365):
        year = 2017
    elif excel_date in range(365, 729):
        year = 2018
    elif excel_date in range(729, 1093):
        year = 2019
    elif excel_date in range(1093, 1464):
        year = 2020
    elif excel_date in range(1464, 1828):
        year = 2021
    elif excel_date in range(1828, 2192):
        year = 2022
    elif excel_date in range(2192, 2556):
        year = 2023
    elif excel_date in range(2556, 2920):
        year = 2024
    elif excel_date in range(2920, 3284):
        year = 2025
    elif excel_date in range(3284, 3655):
        year = 2026
    else:
        raise ValueError

    # get period
    period = math.ceil(convert_to_days_after_year(excel_date) / (4 * 7))

    # get week
    week = math.ceil(convert_to_days_after_period(excel_date) / 7)

    # get day
    day = convert_to_days_after_week(excel_date)

    return [year, period, week, day]


def convert_to_days_after_year(excel_date: int) -> int:
    """
    Return the number of days after a full Mars year.

    >>> convert_to_days_after_year(2)
    2
    >>> convert_to_days_after_year(364)
    364
    >>> convert_to_days_after_year(365)
    1
    """

    if excel_date < 1093:
        if excel_date % 364 == 0:
            return 364
        else:
            return excel_date % 364
    elif 1093 <= excel_date < 1464:
        return excel_date - 1092
    elif 1464 <= excel_date < 3284:
        if (excel_date - 1463) % 364 == 0:
            return 364
        else:
            return (excel_date - 1463) % 364


def convert_to_days_after_period(excel_date: int) -> int:
    """
    Return the number of days after a full Mars period.

    >>> convert_to_days_after_period(2)
    2
    >>> convert_to_days_after_period(366)
    2
    >>> convert_to_days_after_period(2191)
    28
    """
    days_after_year = convert_to_days_after_year(excel_date)

    return 28 if days_after_year % 28 == 0 else days_after_year % 28


def convert_to_days_after_week(excel_date: int) -> int:
    """
    Return the number of days after a full Mars week.

    >>> convert_to_days_after_week(2)
    2
    >>> convert_to_days_after_week(366)
    2
    >>> convert_to_days_after_week(2191)
    7
    """
    days_after_period = convert_to_days_after_period(convert_to_days_after_year(excel_date))

    return 7 if days_after_period % 7 == 0 else days_after_period % 7


if __name__ == '__main__':
    remove_time(time_list)
    mediary_time_list = [convert_2017_base(time) for time in time_list]
    mediary2_time_list = [convert_mars_time_info(time) for time in mediary_time_list]
    final_time_list = [create_mars_format(info) for info in mediary2_time_list]

    # put each Mars time into a string
    s = ''
    for time in final_time_list:
        s += time + '\n'

    marstime_file.write(s)
    time_file.close()
    marstime_file.close()
