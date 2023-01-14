import unittest
from tires.CarriganTires import CarriganTires

class testCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        array = [0.3, 0.1, 0.56, 0.9]

        tires = CarriganTires(array)
        self.assertTrue(tires.needs_service())
    
    def test_tires_should_not_be_serviced(self):
        array = [0.1, 0.45, 0.2, 0.6]

        tires = CarriganTires(array)
        self.assertFalse(tires.needs_service())

if __name__ == "__main__":
    unittest.main()