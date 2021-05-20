import io
import sys
import pytest
import leapYear
from io import StringIO

# https://docs.pytest.org/en/6.2.x/assert.html
# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

def testValidLeapYear(monkeypatch,capsys):
    test_string = StringIO('2020\n')
    monkeypatch.setattr('sys.stdin', test_string)
    leapYear.calcLeapYear()
    out, err = capsys.readouterr()
    assert out == "Enter a year: 2020 is a leap year\n"

def testNonValidLeapYear(monkeypatch,capsys):
    test_string = StringIO('2019\n')
    monkeypatch.setattr('sys.stdin', test_string)
    leapYear.calcLeapYear()
    out, err = capsys.readouterr()
    assert out == "Enter a year: 2019 is not a leap year\n"

