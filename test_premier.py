import pytest
from io import StringIO
import sys

from premier import fizzBuzz, theCount

def test_fizzBuzz():
    assert fizzBuzz(1) == 1
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(30) == "FizzBuzz"
    assert fizzBuzz(7) == 7