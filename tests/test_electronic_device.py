import unittest
from cisc179.ElectronicDevice import ElectronicDevice

class TestElectronicDevice(unittest.TestCase):
    def setUp(self):
        self.device = ElectronicDevice("Battery", "ABC Electronics")

    def test_turn_on(self):
        self.device.turn_on()
        self.assertTrue(self.device.is_on)

    def test_turn_off(self):
        self.device.turn_off()
        self.assertFalse(self.device.is_on)

# Run the tests
if __name__ == "__main__":
    unittest.main()
