# Python’s built-in unittest module allows you to write automated tests
# to check that your code behaves as expected.

import unittest

# 1. Example function to test
    def add(a, b):
        """Returns the sum of two numbers"""
        return a + b

    def divide(a, b):
        """Returns a / b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# 2. Creating a Test Case
# --------------------------------------------------------------------------------------------------------
    # A test case is a class that inherits from unittest.TestCase
    # and contains test methods. Each method should start with 'test_'

    class TestMathFunctions(unittest.TestCase):

        def test_add(self):
            """Test the add function"""
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-1, 1), 0)
            self.assertEqual(add(0, 0), 0)

        def test_divide(self):
            """Test the divide function"""
            self.assertEqual(divide(10, 2), 5)
            self.assertAlmostEqual(divide(7, 3), 2.3333333, places=5)
            # Test division by zero
            with self.assertRaises(ValueError):
                divide(10, 0)

# 3. Running the tests
# --------------------------------------------------------------------------------------------------------
    # If this script is run directly, it will execute all test cases
        if __name__ == "__main__":
            unittest.main()

# 4. Key Points
# --------------------------------------------------------------------------------------------------------
    # - Each test is a method in a class inheriting from unittest.TestCase
    # - Use self.assertEqual, self.assertAlmostEqual, self.assertRaises, etc.
    # - Tests should be small and independent
    # - Run tests regularly to catch errors early
    # - Can be combined with CI/CD pipelines for automated testing