import unittest
from tires.OctoprimeTires import OctoprimeTires

class testOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        array = [1, .5, 2, 1]

        tires = OctoprimeTires(array)
        self.assertTrue(tires.needs_service())
    
    def test_tires_should_not_be_serviced(self):
        array = [0.1, 0.45, 0.2, 0.6]

        tires = OctoprimeTires(array)
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()