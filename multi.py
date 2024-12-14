import unittest

def multi(a, b):
    return a * b

#Testing the multi function
class TestMultiplyNumbers(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multi(3, 4), 12)
        self.assertEqual(multi(5, 0), 0)
        self.assertEqual(multi(0, 5), 0)
        self.assertEqual(multi(-3, 10), -30)
        self.assertEqual(multi(-3, -10), 30)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)