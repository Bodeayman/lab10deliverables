import unittest


#This is the calculation function that we want to test
def calc_discount(price, percentage):
    if price < 0:
        raise ValueError("price cant be negative")
    if percentage < 0 or percentage > 100:
        raise ValueError("discount percentage must be between 0-100")
    
    return price * (1 - percentage / 100)


#This is the test class that we try multiple cases
class TestcalcDiscount(unittest.TestCase):
    def test_calc_discount(self):
        self.assertAlmostEqual(calc_discount(1000, 10), 900)
        self.assertAlmostEqual(calc_discount(100, 20), 80)
        self.assertAlmostEqual(calc_discount(0, 50), 0)
        self.assertAlmostEqual(calc_discount(1000, 0), 1000)
        
        with self.assertRaises(ValueError):
            calc_discount(100, -10)
        with self.assertRaises(ValueError):
            calc_discount(100, 110)
        with self.assertRaises(ValueError):
            calc_discount(-100, 10)

#We call the class down here
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)