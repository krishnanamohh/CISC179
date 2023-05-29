import unittest
from cisc179.Camera import Camera

class TestCamera(unittest.TestCase):
    def setUp(self):
        self.camera = Camera("Battery", "Nikon", "24 MP", "5x Optical Zoom")

    def test_display_info(self):
        expected_output = [
            "Camera Information:",
            "Manufacturer: Nikon",
            "Resolution: 24 MP",
            "Zoom Range: 5x Optical Zoom"
        ]
        actual_output = self.camera.display_info()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
