import pytest

from Leap import leapYears

def test_leapYears():

    assert leapYears(2000) == "leap"
    assert leapYears(2100) == "normal"
    assert leapYears(2008) == "leap"
    assert leapYears(2012) == "leap"
    assert leapYears(2016) == "leap"
    assert leapYears(1700) == "normal"
    assert leapYears(1800) == "normal"
    assert leapYears(1900) == "normal"
    assert leapYears(2017) == "normal"
    assert leapYears(2018) == "normal"
    assert leapYears(2019) == "normal"