import unittest

from uk_post_codes.format import format_post_code


class BaseFormatterTestCase(unittest.TestCase):
    def test_valid_postal_code(self):
        expected = "EC1A 1BB"
        result = format_post_code("e- c1 a £-  1! ?* b %%&^ b")
        self.assertEqual(expected, result)

    def test_valid_postal_code_2(self):
        expected = "W1A 0AX"
        result = format_post_code("w- 1 a £-  0! ?* a %%&^ x")
        self.assertEqual(expected, result)

    def test_valid_postal_code_3(self):
        expected = "M1 1AE"
        result = format_post_code("m- 1  £-  1! ?* a %%&^ e")
        self.assertEqual(expected, result)

    def test_valid_postal_code_4(self):
        expected = "B33 8TH"
        result = format_post_code("b- 33  £-  8! ?* t %%&^ h")
        self.assertEqual(expected, result)

    def test_valid_postal_code_5(self):
        expected = "CR2 6XH"
        result = format_post_code("CR2   6 X H")
        self.assertEqual(expected, result)

    def test_valid_postal_code_6(self):
        expected = "DN55 1PT"
        result = format_post_code("DN55-1PT")
        self.assertEqual(expected, result)

    def test_invalid_postal_code(self):
        expected = ""
        result = format_post_code("e- c1 a £-  1! ?*  %%&^ b")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_2(self):
        expected = ""
        result = format_post_code("w- 1  44£-  0! ?* a %%&^ x")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_3(self):
        expected = ""
        result = format_post_code("1PTDN55")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_4(self):
        expected = ""
        result = format_post_code("DN-1PT")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_5(self):
        expected = ""
        result = format_post_code("DN1PT")
        self.assertEqual(expected, result)


class BermudaFormatterTestCase(unittest.TestCase):
    def test_valid_postal_code(self):
        expected = "CC 99"
        result = format_post_code("C  C - 9  ?*  9")
        self.assertEqual(expected, result)

    def test_valid_postal_code_without_spaces(self):
        expected = "CC 99"
        result = format_post_code("CC99")
        self.assertEqual(expected, result)

    def test_invalid_postal_code(self):
        expected = ""
        result = format_post_code("99CC")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_length(self):
        expected = ""
        result = format_post_code("CC9")
        self.assertEqual(expected, result)


class CaymanFormatterTestCase(unittest.TestCase):
    def test_valid_postal_code(self):
        expected = "KY1-1234"
        result = format_post_code("k- Y 1 £- 1 2! ?3*  4 %%&^ ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_without_spaces(self):
        expected = "KY1-1234"
        result = format_post_code("KY11234")
        self.assertEqual(expected, result)

    def test_invalid_postal_code(self):
        expected = ""
        result = format_post_code("KY51234")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_2(self):
        expected = ""
        result = format_post_code("KY33234")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_length(self):
        expected = ""
        result = format_post_code("KY1123")
        self.assertEqual(expected, result)


class MontserratFormatterTestCase(unittest.TestCase):
    def test_valid_postal_code(self):
        expected = "MSR-1234"
        result = format_post_code("m- s R1 £-  2! ?3*  4 %%&^ ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_without_spaces(self):
        expected = "MSR-1234"
        result = format_post_code("MSR1234")
        self.assertEqual(expected, result)

    def test_invalid_postal_code(self):
        expected = ""
        result = format_post_code("MSR51234")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_2(self):
        expected = ""
        result = format_post_code("MS3234")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_3(self):
        expected = ""
        result = format_post_code("3234MSR")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_length(self):
        expected = ""
        result = format_post_code("MSR112354")
        self.assertEqual(expected, result)


class UpToFourFormatterTestCase(unittest.TestCase):
    def test_valid_postal_code(self):
        expected = "AI-2640"
        result = format_post_code("a- i 26 £-  4! ?*  0 %%&^ ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_1ZZ(self):
        expected = "ASCN-1ZZ"
        result = format_post_code("a- sc n £-  1z! ?*   %%&^z ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_BFPO(self):
        expected = "BFPO-58"
        result = format_post_code("B- Fp O £-  5! ?*   %%&^8 ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_BF1(self):
        expected = "BF1-2AU"
        result = format_post_code("B F1 £-  2! ?a*   %%&^u ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_VG(self):
        expected = "VG-1120"
        result = format_post_code("vg1 £-  1! ?*   %%&^20 ")
        self.assertEqual(expected, result)

    def test_valid_postal_code_without_spaces(self):
        expected = "VG-1120"
        result = format_post_code("VG1120")
        self.assertEqual(expected, result)

    def test_invalid_postal_code(self):
        expected = ""
        result = format_post_code("VG112")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_2(self):
        expected = ""
        result = format_post_code("TKCA1z")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_3(self):
        expected = ""
        result = format_post_code("2auBF1")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_length(self):
        expected = ""
        result = format_post_code("BF2au")
        self.assertEqual(expected, result)

    def test_invalid_postal_code_length_2(self):
        expected = ""
        result = format_post_code("ai999999")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
