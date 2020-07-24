import unittest
from collections import Counter

from three_five.three_five import three_five, three_five_generator

THREE_STR = "Three"
FIVE_STR = "Five"
THREE_FIVE_STR = "ThreeFive"


class TestThreeFive(unittest.TestCase):

    def test_input_3_outputs_three(self):
        expected = [THREE_STR]
        result = three_five(lower=3, upper=4)

        self.assertEqual(expected, result)

    def test_input_5_outputs_five(self):
        expected = [FIVE_STR]
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
            THREE_STR,
            4,
            FIVE_STR,
            THREE_STR,
            7,
            8,
            THREE_STR,
            FIVE_STR,
        ]
        result = three_five(lower=1, upper=11)

        self.assertEqual(expected, result)

    def test_input_range_ten_to_twenty_outputs_correctly(self):
        expected = [
            FIVE_STR,
            11,
            THREE_STR,
            13,
            14,
            THREE_FIVE_STR,
            16,
            17,
            THREE_STR,
            19,
            FIVE_STR,
        ]
        result = three_five(lower=10, upper=21)

        self.assertEqual(expected, result)

    def test_range_one_to_one_hundred_returns_correctly_amount_of_threes(self):
        expected = 27
        result = Counter(three_five()).get(THREE_STR)

        self.assertEqual(expected, result)

    def test_range_one_to_one_hundred_returns_correctly_amount_of_fives(self):
        expected = 14
        result = Counter(three_five()).get(FIVE_STR)

        self.assertEqual(expected, result)

    def test_range_one_to_one_hundred_returns_correctly_amount_of_threefives(self):
        expected = 6
        result = Counter(three_five()).get(THREE_FIVE_STR)

        self.assertEqual(expected, result)


class TestThreeFiveGenerator(unittest.TestCase):

    def test_input_3_outputs_three(self):
        expected = [THREE_STR]
        result = list(three_five_generator(lower=3, upper=4))

        self.assertEqual(expected, result)

    def test_input_5_outputs_five(self):
        expected = [FIVE_STR]
        result = list(three_five_generator(lower=5, upper=6))

        self.assertEqual(expected, result)

    def test_input_1_outputs_1(self):
        expected = [1]
        result = list(three_five_generator(lower=1, upper=2))

        self.assertEqual(expected, result)

    def test_input_range_one_to_ten_outputs_correctly(self):
        expected = [
            1,
            2,
            THREE_STR,
            4,
            FIVE_STR,
            THREE_STR,
            7,
            8,
            THREE_STR,
            FIVE_STR,
        ]
        result = list(three_five_generator(lower=1, upper=11))

        self.assertEqual(expected, result)

    def test_input_range_ten_to_twenty_outputs_correctly(self):
        expected = [
            FIVE_STR,
            11,
            THREE_STR,
            13,
            14,
            THREE_FIVE_STR,
            16,
            17,
            THREE_STR,
            19,
            FIVE_STR,
        ]
        result = list(three_five_generator(lower=10, upper=21))

        self.assertEqual(expected, result)

    def test_range_one_to_one_hundred_returns_correctly_amount_of_threes(self):
        expected = 27
        result = Counter(three_five_generator()).get(THREE_STR)

        self.assertEqual(expected, result)

    def test_range_one_to_one_hundred_returns_correctly_amount_of_fives(self):
        expected = 14
        result = Counter(three_five_generator()).get(FIVE_STR)

        self.assertEqual(expected, result)

    def test_range_one_to_one_hundred_returns_correctly_amount_of_threefives(self):
        expected = 6
        result = Counter(three_five_generator()).get(THREE_FIVE_STR)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
