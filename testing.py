import unittest

# Function to test
def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

# Unit test class
class TestRectangleArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_rectangle_area(3, 4), 12)

    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(0, 4)
            calculate_rectangle_area(3, 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-3, 4)
            calculate_rectangle_area(3, -4)

if __name__ == '__main__':
    unittest.main()