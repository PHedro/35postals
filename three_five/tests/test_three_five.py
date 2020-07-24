import unittest

from three_five.three_five import three_five


class TestThreeFive(unittest.TestCase):
    THREE_STR = "Three"
    FIVE_STR = "Five"
    THREE_FIVE_STR = "ThreeFive"

    def test_input_3_outputs_three(self):
        expected = [self.THREE_STR]
        result = three_five(lower=3, upper=4)

        self.assertEqual(expected, result)

    def test_input_5_outputs_five(self):
        expected = [self.FIVE_STR]
        result = three_five(lower=5, upper=6)

        self.assertEqual(expected, result)

    def test_input_1_outputs_1(self):
        expected = [1]
        result = three_five(lower=1, upper=2)

        self.assertEqual(expected, result)

    def test_input_range_one_to_ten_outputs_correctly(self):
        expected = [
            1,
            2,
            self.THREE_STR,
            4,
            self.FIVE_STR,
            self.THREE_STR,
            7,
            8,
            self.THREE_STR,
            self.FIVE_STR,
        ]
        result = three_five(lower=1, upper=11)

        self.assertEqual(expected, result)

    def test_input_range_ten_to_twenty_outputs_correctly(self):
        expected = [
            self.FIVE_STR,
            11,
            self.THREE_STR,
            13,
            14,
            self.THREE_FIVE_STR,
            16,
            17,
            self.THREE_STR,
            19,
            self.FIVE_STR,
        ]
        result = three_five(lower=10, upper=21)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
