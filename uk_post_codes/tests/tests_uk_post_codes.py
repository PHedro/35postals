import unittest

from uk_post_codes.post_code import validate_post_code


class UkPostCodesTestCaseCommonCases(unittest.TestCase):
    def test_EC1A_1BB_is_valid(self):
        test_code = "EC1A 1BB"
        self.assertTrue(validate_post_code(test_code))

    def test_W1A_0AX_is_valid(self):
        test_code = "W1A 0AX"
        self.assertTrue(validate_post_code(test_code))

    def test_M1_1AE_is_valid(self):
        test_code = "M1 1AE"
        self.assertTrue(validate_post_code(test_code))

    def test_B33_8TH_is_valid(self):
        test_code = "B33 8TH"
        self.assertTrue(validate_post_code(test_code))

    def test_CR2_6XH_is_valid(self):
        test_code = "CR2 6XH"
        self.assertTrue(validate_post_code(test_code))

    def test_DN55_1PT_is_valid(self):
        test_code = "DN55 1PT"
        self.assertTrue(validate_post_code(test_code))

    def test_EC1A1BB_is_valid(self):
        test_code = "EC1A1BB"
        self.assertTrue(validate_post_code(test_code))

    def test_W1A0AX_is_valid(self):
        test_code = "W1A0AX"
        self.assertTrue(validate_post_code(test_code))

    def test_M11AE_is_valid(self):
        test_code = "M11AE"
        self.assertTrue(validate_post_code(test_code))

    def test_B338TH_is_valid(self):
        test_code = "B338TH"
        self.assertTrue(validate_post_code(test_code))

    def test_CR26XH_is_valid(self):
        test_code = "CR26XH"
        self.assertTrue(validate_post_code(test_code))

    def test_DN551PT_is_valid(self):
        test_code = "DN551PT"
        self.assertTrue(validate_post_code(test_code))

    def test_EC1A_BBB_invalid(self):
        test_code = "EC1A BBB"
        self.assertFalse(validate_post_code(test_code))

    def test_W1AAAX_invalid(self):
        test_code = "W1AAAX"
        self.assertFalse(validate_post_code(test_code))

    def test_W1A_AX_invalid(self):
        test_code = "W1A AX"
        self.assertFalse(validate_post_code(test_code))

    def test_M1_AE_invalid(self):
        test_code = "M1 AE"
        self.assertFalse(validate_post_code(test_code))

    def test_B338_TH_invalid(self):
        test_code = "B338 TH"
        self.assertFalse(validate_post_code(test_code))

    def test_CR26_XH_invalid(self):
        test_code = "CR26 XH"
        self.assertFalse(validate_post_code(test_code))

    def test_DN55_1PT_invalid(self):
        test_code = "DN55_1PT"
        self.assertFalse(validate_post_code(test_code))

    def test_DN55__1PT_invalid(self):
        test_code = "DN55-1PT"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseAnguilla(unittest.TestCase):
    def test_AI__2640_is_valid(self):
        test_code = "AI-2640"
        self.assertTrue(validate_post_code(test_code))

    def test_AI_2640_is_valid(self):
        test_code = "AI 2640"
        self.assertTrue(validate_post_code(test_code))

    def test_AI2640_is_valid(self):
        test_code = "AI2640"
        self.assertTrue(validate_post_code(test_code))

    def test_AI2_640_invalid(self):
        test_code = "AI2 640"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseAscensionIsland(unittest.TestCase):
    def test_ASCN_1ZZ_is_valid(self):
        test_code = "ASCN 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_ASCN__1ZZ_invalid(self):
        test_code = "ASCN-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_ASCN1ZZ_invalid(self):
        test_code = "ASCN1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_ASCN___1ZZ_invalid(self):
        test_code = "ASCN  1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseBritishIndianOceanTerritory(unittest.TestCase):
    def test_BBND_1ZZ_is_valid(self):
        test_code = "BBND 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_BBND__1ZZ_invalid(self):
        test_code = "BBND-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_BBND1ZZ_invalid(self):
        test_code = "BBND1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_BBND___1ZZ_invalid(self):
        test_code = "BBND  1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseAkrotiriAndDhekelia(unittest.TestCase):
    def test_BFPO_57_is_valid(self):
        test_code = "BFPO 57"
        self.assertTrue(validate_post_code(test_code))

    def test_BFPO__57_invalid(self):
        test_code = "BFPO-57"
        self.assertFalse(validate_post_code(test_code))

    def test_BFPO57_is_valid(self):
        test_code = "BFPO57"
        self.assertTrue(validate_post_code(test_code))

    def test_BFPO___57_invalid(self):
        test_code = "BFPO  57"
        self.assertFalse(validate_post_code(test_code))

    def test_BFPO_58_is_valid(self):
        test_code = "BFPO 58"
        self.assertTrue(validate_post_code(test_code))

    def test_BFPO__58_invalid(self):
        test_code = "BFPO-58"
        self.assertFalse(validate_post_code(test_code))

    def test_BFPO58_is_valid(self):
        test_code = "BFPO58"
        self.assertTrue(validate_post_code(test_code))

    def test_BFPO___58_invalid(self):
        test_code = "BFPO  58"
        self.assertFalse(validate_post_code(test_code))

    def test_BF1_2AT_is_valid(self):
        test_code = "BF1 2AT"
        self.assertTrue(validate_post_code(test_code))

    def test_BF1__2AT_invalid(self):
        test_code = "BF1-2AT"
        self.assertFalse(validate_post_code(test_code))

    def test_BF12AT_is_valid(self):
        test_code = "BF12AT"
        self.assertTrue(validate_post_code(test_code))

    def test_BF1___2AT_invalid(self):
        test_code = "BF1  2AT"
        self.assertFalse(validate_post_code(test_code))

    def test_BF1_2AU_is_valid(self):
        test_code = "BF1 2AU"
        self.assertTrue(validate_post_code(test_code))

    def test_BF1__2Au_invalid(self):
        test_code = "BF1-2AU"
        self.assertFalse(validate_post_code(test_code))

    def test_BF12AU_is_valid(self):
        test_code = "BF12AU"
        self.assertTrue(validate_post_code(test_code))

    def test_BF1___2AU_invalid(self):
        test_code = "BF1  2AU"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseBritishAntarcticTerritory(unittest.TestCase):
    def test_BIQQ_1ZZ_is_valid(self):
        test_code = "BIQQ 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_BIQQ__1ZZ_invalid(self):
        test_code = "BIQQ-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_BIQQ1ZZ_invalid(self):
        test_code = "BIQQ1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_BIQQ___1ZZ_invalid(self):
        test_code = "BIQQ  1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseFalklandIslands(unittest.TestCase):
    def test_FIQQ_1ZZ_is_valid(self):
        test_code = "FIQQ 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_FIQQ__1ZZ_invalid(self):
        test_code = "FIQQ-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_FIQQ1ZZ_invalid(self):
        test_code = "FIQQ1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_FIQQ___1ZZ_invalid(self):
        test_code = "FIQQ  1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseMontserrat(unittest.TestCase):

    # as couldn't find a valid postcode for montserrat will be testing
    # with random codes that the regex provided validates
    def test_FIQQ_1ZZ_is_valid(self):
        test_code = "MSR-1234"
        self.assertTrue(validate_post_code(test_code))

    def test_FIQQ__1ZZ_invalid(self):
        test_code = "MSR 1234"
        self.assertTrue(validate_post_code(test_code))

    def test_FIQQ1ZZ_invalid(self):
        test_code = "MSR1234"
        self.assertTrue(validate_post_code(test_code))

    def test_FIQQ___1ZZ_invalid(self):
        test_code = "MSR  1234"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseCaymanIslands(unittest.TestCase):
    def test_KY1_1301_is_valid(self):
        test_code = "KY1-1301"
        self.assertTrue(validate_post_code(test_code))

    def test_KY1__1301_invalid(self):
        test_code = "KY1 1301"
        self.assertTrue(validate_post_code(test_code))

    def test_KY11301_invalid(self):
        test_code = "KY11301"
        self.assertTrue(validate_post_code(test_code))

    def test_KY1___1301_invalid(self):
        test_code = "KY1  1301"
        self.assertFalse(validate_post_code(test_code))

    def test_KY1_1508_is_valid(self):
        test_code = "KY1-1508"
        self.assertTrue(validate_post_code(test_code))

    def test_KY1__1508_is_valid(self):
        test_code = "KY1 1508"
        self.assertTrue(validate_post_code(test_code))

    def test_KY11508_is_valid(self):
        test_code = "KY11508"
        self.assertTrue(validate_post_code(test_code))

    def test_KY1___1508_invalid(self):
        test_code = "KY1  1508"
        self.assertFalse(validate_post_code(test_code))

    def test_KY1_1112_is_valid(self):
        test_code = "KY1-1112"
        self.assertTrue(validate_post_code(test_code))

    def test_KY1__1112_is_valid(self):
        test_code = "KY1 1112"
        self.assertTrue(validate_post_code(test_code))

    def test_KY11112_is_valid(self):
        test_code = "KY11112"
        self.assertTrue(validate_post_code(test_code))

    def test_KY1___1112_invalid(self):
        test_code = "KY1  1112"
        self.assertFalse(validate_post_code(test_code))

    def test_KY2_2301_is_valid(self):
        test_code = "KY2-2301"
        self.assertTrue(validate_post_code(test_code))

    def test_KY2__2301_is_valid(self):
        test_code = "KY2 2301"
        self.assertTrue(validate_post_code(test_code))

    def test_KY22301_is_valid(self):
        test_code = "KY22301"
        self.assertTrue(validate_post_code(test_code))

    def test_KY2___2301_invalid(self):
        test_code = "KY2  2301"
        self.assertFalse(validate_post_code(test_code))

    def test_KY2_2201_is_valid(self):
        test_code = "KY2-2201"
        self.assertTrue(validate_post_code(test_code))

    def test_KY2__2201_is_valid(self):
        test_code = "KY2 2201"
        self.assertTrue(validate_post_code(test_code))

    def test_KY22201_is_valid(self):
        test_code = "KY22201"
        self.assertTrue(validate_post_code(test_code))

    def test_KY2___2201_invalid(self):
        test_code = "KY2  2201"
        self.assertFalse(validate_post_code(test_code))

    def test_KY2_2401_is_valid(self):
        test_code = "KY2-2401"
        self.assertTrue(validate_post_code(test_code))

    def test_KY2__2401_is_valid(self):
        test_code = "KY2 2401"
        self.assertTrue(validate_post_code(test_code))

    def test_KY22401_is_valid(self):
        test_code = "KY22401"
        self.assertTrue(validate_post_code(test_code))

    def test_KY2___2401_invalid(self):
        test_code = "KY2  2401"
        self.assertFalse(validate_post_code(test_code))

    def test_KY3_2501_is_valid(self):
        test_code = "KY3-2501"
        self.assertTrue(validate_post_code(test_code))

    def test_KY3__2501_invalid(self):
        test_code = "KY3 2501"
        self.assertTrue(validate_post_code(test_code))

    def test_KY32501_is_valid(self):
        test_code = "KY32501"
        self.assertTrue(validate_post_code(test_code))

    def test_KY3___2501_invalid(self):
        test_code = "KY3  2501"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCasePitcairnIslands(unittest.TestCase):
    def test_PCRN_1ZZ_is_valid(self):
        test_code = "PCRN 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_PCRN__1ZZ_invalid(self):
        test_code = "PCRN-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_PCRN1ZZ_is_valid(self):
        test_code = "PCRN1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_PCRN___1ZZ_invalid(self):
        test_code = "PCRN  1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseSouthGeorgiaSouthSandwichIslands(unittest.TestCase):
    def test_SIQQ_1ZZ_is_valid(self):
        test_code = "SIQQ 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_SIQQ__1ZZ_invalid(self):
        test_code = "SIQQ-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_SIQQ1ZZ_is_valid(self):
        test_code = "SIQQ1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_SIQQ___1ZZ_invalid(self):
        test_code = "SIQQ  1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseSaintHelena(unittest.TestCase):
    def test_STHL_1ZZ_is_valid(self):
        test_code = "STHL 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_STHL__1ZZ_invalid(self):
        test_code = "STHL-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_STHL1ZZ_is_valid(self):
        test_code = "STHL1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_STHL___1ZZ_invalid(self):
        test_code = "STHL   1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseTristanCunha(unittest.TestCase):
    def test_TDCU_1ZZ_is_valid(self):
        test_code = "TDCU 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_TDCU__1ZZ_invalid(self):
        test_code = "TDCU-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_TDCU1ZZ_invalid(self):
        test_code = "TDCU1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_TDCU___1ZZ_invalid(self):
        test_code = "TDCU   1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseTurksCaicosIslands(unittest.TestCase):
    def test_TKCA_1ZZ_is_valid(self):
        test_code = "TKCA 1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA__1ZZ_invalid(self):
        test_code = "TKCA-1ZZ"
        self.assertFalse(validate_post_code(test_code))

    def test_TKCA1ZZ_is_valid(self):
        test_code = "TKCA1ZZ"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "TKCA   1ZZ"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseTortolaCentral(unittest.TestCase):
    def test_VG1110_is_valid(self):
        test_code = "VG1110"
        self.assertTrue(validate_post_code(test_code))

    def test_VG__1110_is_valid(self):
        test_code = "VG-1110"
        self.assertTrue(validate_post_code(test_code))

    def test_VG_1110_is_valid(self):
        test_code = "VG 1110"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "VG   1110"
        self.assertFalse(validate_post_code(test_code))

    def test_VG____111_invalid(self):
        test_code = "VG   111"
        self.assertFalse(validate_post_code(test_code))

    def test_VG111_invalid(self):
        test_code = "VG111"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseTortolaEast(unittest.TestCase):
    def test_VG1120_is_valid(self):
        test_code = "VG1120"
        self.assertTrue(validate_post_code(test_code))

    def test_VG__1120_is_valid(self):
        test_code = "VG-1120"
        self.assertTrue(validate_post_code(test_code))

    def test_VG_1120_is_valid(self):
        test_code = "VG 1120"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "VG   1120"
        self.assertFalse(validate_post_code(test_code))

    def test_VG____112_invalid(self):
        test_code = "VG   112"
        self.assertFalse(validate_post_code(test_code))

    def test_VG112_invalid(self):
        test_code = "VG112"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseTortolaWest(unittest.TestCase):
    def test_VG1130_is_valid(self):
        test_code = "VG1130"
        self.assertTrue(validate_post_code(test_code))

    def test_VG__1130_is_valid(self):
        test_code = "VG-1130"
        self.assertTrue(validate_post_code(test_code))

    def test_VG_1130_is_valid(self):
        test_code = "VG 1130"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "VG   1130"
        self.assertFalse(validate_post_code(test_code))

    def test_VG____113_invalid(self):
        test_code = "VG   113"
        self.assertFalse(validate_post_code(test_code))

    def test_VG113_invalid(self):
        test_code = "VG113"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseAnegada(unittest.TestCase):
    def test_VG1140_is_valid(self):
        test_code = "VG1140"
        self.assertTrue(validate_post_code(test_code))

    def test_VG__1140_is_valid(self):
        test_code = "VG-1140"
        self.assertTrue(validate_post_code(test_code))

    def test_VG_1140_is_valid(self):
        test_code = "VG 1140"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "VG   1140"
        self.assertFalse(validate_post_code(test_code))

    def test_VG____114_invalid(self):
        test_code = "VG   114"
        self.assertFalse(validate_post_code(test_code))

    def test_VG114_invalid(self):
        test_code = "VG114"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseVirginGorda(unittest.TestCase):
    def test_VG1150_is_valid(self):
        test_code = "VG1150"
        self.assertTrue(validate_post_code(test_code))

    def test_VG__1150_is_valid(self):
        test_code = "VG-1150"
        self.assertTrue(validate_post_code(test_code))

    def test_VG_1150_is_valid(self):
        test_code = "VG 1150"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "VG   1150"
        self.assertFalse(validate_post_code(test_code))

    def test_VG____115_invalid(self):
        test_code = "VG   115"
        self.assertFalse(validate_post_code(test_code))

    def test_VG115_invalid(self):
        test_code = "VG115"
        self.assertFalse(validate_post_code(test_code))


class UkPostCodesTestCaseJostVanDyke(unittest.TestCase):
    def test_VG1160_is_valid(self):
        test_code = "VG1160"
        self.assertTrue(validate_post_code(test_code))

    def test_VG__1160_is_valid(self):
        test_code = "VG-1160"
        self.assertTrue(validate_post_code(test_code))

    def test_VG_1160_is_valid(self):
        test_code = "VG 1160"
        self.assertTrue(validate_post_code(test_code))

    def test_TKCA___1ZZ_invalid(self):
        test_code = "VG   1160"
        self.assertFalse(validate_post_code(test_code))

    def test_VG____116_invalid(self):
        test_code = "VG   116"
        self.assertFalse(validate_post_code(test_code))

    def test_VG116_invalid(self):
        test_code = "VG116"
        self.assertFalse(validate_post_code(test_code))


if __name__ == "__main__":
    unittest.main()
