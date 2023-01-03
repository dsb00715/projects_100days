""" def format_name(f_name, l_name):
    return f_name.title() + l_name.title()


f_name = input("Enter first name:")
l_name = input("Enter last name:")
name = format_name(f_name, l_name)
print(name) """

# ***************************************************************************************************
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """function to find out if year & month is a leap year.

    Args:
        year (int): Enter year number
        month (int): Enter month

    Returns: days
        int: Returns number of days
    """
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = month_days[month - 1]
    if is_leap(year) and month == 2:
        return 29
    return days


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
