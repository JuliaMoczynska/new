import unittest


def square(number):
   
    return number * number


class SquareTest(unittest.TestCase):
   
    def test_square_positive_number(self):
        self.assertEqual(4, square(2))
        self.assertEqual(9, square(3))
        self.assertEqual(1, square(1))
        self.assertEqual(0, square(0))

    def test_square_negative_number(self):
        
        self.assertEqual(1, square(-1))
        self.assertEqual(4, square(-2))

    def test_square_not_a_number(self):
       
        with self.assertRaises(TypeError):
            square("not a number")


if __name__ == "__main__":
   
    unittest.main()
