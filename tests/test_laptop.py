import unittest
from unittest.mock import patch

from cisc179.Laptop import Laptop


class TestLaptop(unittest.TestCase):
    def setUp(self):
        self.laptop = Laptop("AC power", "Dell", "Windows 10", 8, 15.6, "1920x1080")

    def test_display_info(self):
        expected_output = [
            "Laptop Information:",
            "Power Source: AC power",
            "Manufacturer: Dell",
            "Operating System: Windows 10",
            "RAM: 8",
            "Screen Size: 15.6",
            "Resolution: 1920x1080"
        ]
        actual_output = self.laptop.display_info()

        self.assertEqual(actual_output, expected_output)

    def test_browse_internet(self):
        with patch('builtins.print') as mock_print:
            self.laptop.browse_internet()
            mock_print.assert_called_with("Browsing the internet on the laptop.")


if __name__ == '__main__':
    unittest.main()
