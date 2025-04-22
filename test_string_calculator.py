import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()
    
    def test_empty_string(self):
        self.assertEqual(0, self.calculator.add(""))
    
    def test_single_number(self):
        self.assertEqual(1, self.calculator.add("1"))
        self.assertEqual(2, self.calculator.add("2"))
    
    def test_two_numbers(self):
        self.assertEqual(3, self.calculator.add("1,2"))
        self.assertEqual(5, self.calculator.add("2,3"))
    
    def test_multiple_numbers(self):
        self.assertEqual(6, self.calculator.add("1,2,3"))
        self.assertEqual(10, self.calculator.add("1,2,3,4"))
    
    def test_newlines_between_numbers(self):
        self.assertEqual(6, self.calculator.add("1\n2,3"))
        self.assertEqual(7, self.calculator.add("1,2\n4"))
    
    def test_custom_delimiter(self):
        self.assertEqual(3, self.calculator.add("//;\n1;2"))
        self.assertEqual(8, self.calculator.add("//#\n3#5"))
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,2")
        self.assertTrue("negatives not allowed: -1" in str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            self.calculator.add("2,-4,-5")
        self.assertTrue("negatives not allowed: -4, -5" in str(context.exception))

if __name__ == "__main__":
    unittest.main() 