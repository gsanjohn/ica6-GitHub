# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
import pytest


def my_adder(a, b, c):
    """
    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author:
    date:
    """

    # this is the summation
    out = a + b + c

    return out


@pytest.mark.parametrize("a, b, c, sum", [(1, 1, 1, 3), (2, 2, 2, 6), (1, 2, 3, 6)])
def test_my_adder(a, b, c, sum):
    output = my_adder(a, b, c)
    assert output == sum


def my_thermo_stat(temp, desired_temp):
    """
    Changes the status of the thermostat based on
    temperature and desired temperature
    author
    date
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status


@pytest.mark.parametrize(
    "temp, desired_temp, expected", [(50, 75, "Heat"), (90, 75, "AC"), (75, 75, "off")]
)
def test_my_thermo_stat(temp, desired_temp, expected):
    output = my_thermo_stat(temp, desired_temp)
    assert output == expected


def have_digits(s):
    """
    Checks if a string has digits in it
    """

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out


@pytest.mark.parametrize("s, expected", [("G6", 1), ("hello", 0)])
def test_have_digits(s, expected):
    output = have_digits(s)
    assert output == expected
