import unittest
from math_v2 import generate_int
from math_v2 import GenerationException

class TestGenerateInt(unittest.TestCase):
    def test_valid_generation(self):
        op1_range = range(1, 10)
        op2_range = range(1, 10)
        op = '+'
        result_range = range(2, 18)

        result = generate_int(op1_range, op2_range, op, result_range)

        self.assertIsNotNone(result)
        self.assertIn(result[0], op1_range)
        self.assertIn(result[1], op2_range)
        self.assertEqual(result[2], op)
        self.assertIn(result[0] + result[1], result_range)

    def test_invalid_op(self):
        op1_range = range(1, 10)
        op2_range = range(1, 10)
        op = '/'
        result_range = range(2, 18)

        with self.assertRaises(GenerationException):
            generate_int(op1_range, op2_range, op, result_range)

    def test_no_valid_combination(self):
        op1_range = range(1, 3)
        op2_range = range(1, 3)
        op = '*'
        result_range = range(10, 20)

        with self.assertRaises(GenerationException):
            generate_int(op1_range, op2_range, op, result_range, max_attempts=100)



if __name__ == '__main__':
    unittest.main()
