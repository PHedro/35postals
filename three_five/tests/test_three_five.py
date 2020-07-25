import unittest
from collections import Counter

from three_five.constants import FIVE_STR, THREE_FIVE_STR, THREE_STR
from three_five.three_five import (
    _is_three_and_five_multiple,
    _three_five_threefive_or_value,
    three_five,
    three_five_generator,
)


class TestThreeFiveOrValue(unittest.TestCase):
    def test_zero(self):
        expected = 0
        result = _three_five_threefive_or_value(0)
        self.assertEqual(expected, result)

    def test_3(self):
        expected = THREE_STR
        result = _three_five_threefive_or_value(3)
        self.assertEqual(expected, result)

    def test_5(self):
        expected = FIVE_STR
        result = _three_five_threefive_or_value(5)
        self.assertEqual(expected, result)

    def test_12(self):
        expected = 13
        result = _three_five_threefive_or_value(13)
        self.assertEqual(expected, result)

    def test_15(self):
        expected = THREE_FIVE_STR
        result = _three_five_threefive_or_value(15)
        self.assertEqual(expected, result)

    def test_17(self):
        expected = 17
        result = _three_five_threefive_or_value(17)
        self.assertEqual(expected, result)

    def test_45(self):
        expected = THREE_FIVE_STR
        result = _three_five_threefive_or_value(45)
        self.assertEqual(expected, result)

    def test_55(self):
        expected = FIVE_STR
        result = _three_five_threefive_or_value(55)
        self.assertEqual(expected, result)

    def test_42(self):
        expected = THREE_STR
        result = _three_five_threefive_or_value(42)
        self.assertEqual(expected, result)

    def test_89(self):
        expected = 89
        result = _three_five_threefive_or_value(89)
        self.assertEqual(expected, result)

    def test_87(self):
        expected = THREE_STR
        result = _three_five_threefive_or_value(87)
        self.assertEqual(expected, result)


class TestIsThreeAndFiveMultiple(unittest.TestCase):
    def test_zero_is_not_multiple(self):
        result = _is_three_and_five_multiple(0)
        self.assertFalse(any(result))

    def test_zero_is_not_multiple(self):
        result = _is_three_and_five_multiple(0)
        self.assertFalse(any(result))


class TestThreeFive(unittest.TestCase):
    def test_input_0_outputs_0(self):
        expected = [0]
        result = three_five(lower=0, upper=1)

        self.assertEqual(expected, result)

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
    def test_input_0_outputs_0(self):
        expected = [0]
        result = three_five(lower=0, upper=1)

        self.assertEqual(expected, result)

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
