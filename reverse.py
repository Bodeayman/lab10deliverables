import unittest

#A simple algorithm in reversing the list
def reverse(list):
    return list[::-1]

class TestReverseList(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse([0,1,2,3,4]), [4,3,2,1,0])
        self.assertEqual(reverse([]), [])
        self.assertEqual(reverse([40]), [40])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)