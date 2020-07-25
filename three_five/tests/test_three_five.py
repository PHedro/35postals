import io
import unittest
from collections import Counter
from unittest.mock import patch

from three_five.constants import FIVE_STR, THREE_FIVE_STR, THREE_STR
from three_five.three_five import (
    _check_if_range_boundaries_are_valid,
    _is_three_and_five_multiple,
    _three_five_threefive_or_value,
    three_five,
    three_five_generator,
    three_five_print,
)


class TestRangeBoundaries(unittest.TestCase):
    def test_both_valid_int(self):
        self.assertTrue(_check_if_range_boundaries_are_valid(0, 3))

    def test_both_floats_and_upper_greater_than_lower(self):
        self.assertFalse(_check_if_range_boundaries_are_valid(float(0), float(3)))

    def test_upper_float_and_upper_greater_than_lower(self):
        self.assertFalse(_check_if_range_boundaries_are_valid(0, float(3)))

    def test_upper_string_and_upper_greater_than_lower(self):
        self.assertFalse(_check_if_range_boundaries_are_valid(0, "3"))

    def test_both_valid_int_lower_greater_than_upper(self):
        self.assertFalse(_check_if_range_boundaries_are_valid(5, 3))


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
        expected = THREE_STR
        result = _three_five_threefive_or_value(12)
        self.assertEqual(expected, result)

    def test_13(self):
        expected = 13
        result = _three_five_threefive_or_value(13)
        self.assertEqual(expected, result)

    def test_negative_3(self):
        expected = THREE_STR
        result = _three_five_threefive_or_value(-3)
        self.assertEqual(expected, result)

    def test_negative_3_float(self):
        expected = float(-3)
        result = _three_five_threefive_or_value(float(-3))
        self.assertEqual(expected, result)

    def test_negative_5(self):
        expected = FIVE_STR
        result = _three_five_threefive_or_value(-5)
        self.assertEqual(expected, result)

    def test_negative_13(self):
        expected = -13
        result = _three_five_threefive_or_value(-13)
        self.assertEqual(expected, result)

    def test_15(self):
        expected = THREE_FIVE_STR
        result = _three_five_threefive_or_value(15)
        self.assertEqual(expected, result)

    def test_float_15(self):
        expected = float(15)
        result = _three_five_threefive_or_value(float(15))
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

    def test_ASD_is_not_multiple(self):
        result = _is_three_and_five_multiple("ASD")
        self.assertFalse(any(result))

    def test_13_is_not_multiple(self):
        result = _is_three_and_five_multiple(13)
        self.assertFalse(any(result))

    def test_88_is_not_multiple(self):
        result = _is_three_and_five_multiple(88)
        self.assertFalse(any(result))

    def test_31_is_not_multiple(self):
        result = _is_three_and_five_multiple(31)
        self.assertFalse(any(result))

    def test_float_31_is_not_multiple(self):
        result = _is_three_and_five_multiple(float(31))
        self.assertFalse(any(result))

    def test_three_is_multiple(self):
        result_for_three, *_ = _is_three_and_five_multiple(3)
        self.assertTrue(result_for_three)

    def test_float_three_is_not_multiple(self):
        result_for_three, *_ = _is_three_and_five_multiple(float(3))
        self.assertFalse(result_for_three)

    def test_87_is_multiple(self):
        result_for_three, *_ = _is_three_and_five_multiple(87)
        self.assertTrue(result_for_three)

    def test_99_is_multiple(self):
        result_for_three, *_ = _is_three_and_five_multiple(99)
        self.assertTrue(result_for_three)

    def test_five_is_multiple(self):
        _, result_for_five, _ = _is_three_and_five_multiple(5)
        self.assertTrue(result_for_five)

    def test_15_is_multiple_for_both(self):
        result = _is_three_and_five_multiple(15)
        self.assertTrue(all(result))

    def test_45_is_multiple_for_both(self):
        result = _is_three_and_five_multiple(15)
        self.assertTrue(all(result))


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


class TestThreeFivePrint(unittest.TestCase):
    def test_input_0_outputs_0(self):
        expected = "0\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=0, upper=1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_1_to_5_outputs_correctly(self):
        expected = "1\n2\nThree\n4\nFive\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=1, upper=6)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_1_to_4_outputs_correctly(self):
        expected = "1\n2\nThree\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=1, upper=4)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_5_outputs_five(self):
        expected = "Five\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=5, upper=6)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_15_outputs_correctly(self):
        expected = "ThreeFive\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=15, upper=16)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_1_outputs_1(self):
        expected = "1\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=1, upper=2)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_str_4_outputs_empty(self):
        expected = ""
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=3, upper="4")
            self.assertEqual(fake_out.getvalue(), expected)

    def test_input_range_one_to_ten_outputs_correctly(self):
        expected = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            three_five_print(lower=1, upper=11)
            self.assertEqual(fake_out.getvalue(), expected)


class TestThreeFiveGenerator(unittest.TestCase):
    def test_input_0_outputs_0(self):
        expected = [0]
        result = three_five(lower=0, upper=1)

        self.assertEqual(expected, result)

    def test_input_3_outputs_three(self):
        expected = [THREE_STR]
        result = list(three_five_generator(lower=3, upper=4))

        self.assertEqual(expected, result)

    def test_input_float3_outputs_empty(self):
        expected = []
        result = list(three_five_generator(lower=float(3), upper=4))

        self.assertEqual(expected, result)

    def test_input_str_4_outputs_empty(self):
        expected = []
        result = list(three_five_generator(lower=3, upper="4"))

        self.assertEqual(expected, result)

    def test_input_both_floats_outputs_empty(self):
        expected = []
        result = list(three_five_generator(lower=float(3), upper=float(4)))

        self.assertEqual(expected, result)

    def test_input_lower_greater_than_upper_outputs_empty(self):
        expected = []
        result = list(three_five_generator(lower=10, upper=3))

        self.assertEqual(expected, result)

    def test_input_lower_equals_to_upper_outputs_empty(self):
        expected = []
        result = list(three_five_generator(lower=10, upper=10))

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
