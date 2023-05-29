import unittest
from unittest.mock import patch

from cisc179.SmartPhone import Smartphone


class TestSmartphone(unittest.TestCase):

    def setUp(self):
        self.smartphone = Smartphone("Battery", "Apple", "iPhone 12")

    def test_make_call(self):
        with patch('builtins.print') as mock_print:
            self.smartphone.make_call("1234567890")
            mock_print.assert_called_with("Calling", "1234567890")

    def test_send_message(self):
        with patch('builtins.print') as mock_print:
            self.smartphone.send_message("John", "Hello")
            mock_print.assert_called_with("Sending message to", "John")

if __name__ == '__main__':
    unittest.main()
