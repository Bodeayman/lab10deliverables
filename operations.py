import unittest

class Operations:
    #Used the static method , so you can call the function from the class directly
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    #We made the is prime function above with the factorial , and we throw an exception for it
    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not suitable for negative numbers")
        
        if n <= 1:
            return 1
        
        result = 1

        for i in range(2, n + 1):
            result *= i
        return result


#This is the test class that performs the test for the actual operations
class TestOperations(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(Operations.is_prime(2))
        self.assertTrue(Operations.is_prime(7))
        self.assertTrue(Operations.is_prime(19)) 
        
        self.assertFalse(Operations.is_prime(4))
        self.assertFalse(Operations.is_prime(15))
        self.assertFalse(Operations.is_prime(100))    
        self.assertFalse(Operations.is_prime(0))
        self.assertFalse(Operations.is_prime(1))
        self.assertFalse(Operations.is_prime(-5))
    
    def test_factorial(self):
        self.assertEqual(Operations.factorial(0), 1)
        self.assertEqual(Operations.factorial(1), 1)
        self.assertEqual(Operations.factorial(5), 120)
        self.assertEqual(Operations.factorial(6), 720)
        
        with self.assertRaises(ValueError):
            Operations.factorial(-1)
        with self.assertRaises(ValueError):
            Operations.factorial(-10)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)