import io
import sys
import pytest
import leapYear
import unittest
from unittest.mock import patch
from io import StringIO

# https://docs.pytest.org/en/6.2.x/assert.html
# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

# def testValidLeapYear(monkeypatch,capsys):
#     test_string = StringIO('2020\n')
#     monkeypatch.setattr('sys.stdin', test_string)
#     leapYear.calcLeapYear()
#     out, err = capsys.readouterr()
#     assert out == "Enter a year: 2020 is a leap year\n"

# def testNonValidLeapYear(monkeypatch,capsys):
#     test_string = StringIO('2019\n')
#     monkeypatch.setattr('sys.stdin', test_string)
#     leapYear.calcLeapYear()
#     out, err = capsys.readouterr()
#     assert out == "Enter a year: 2019 is not a leap year\n"


class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['2020'])
    def testValidLeapYear(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear()                                    # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['2020 is a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['2019'])
    def testNonValidLeapYear(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        leapYear.calcLeapYear()                                  # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['2019 is not a leap year', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

