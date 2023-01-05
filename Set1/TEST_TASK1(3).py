import unittest
from TASK1 import function

# All passed - 8/8
class MainTest(unittest.TestCase):
    def testForExampleProperInput1(self):
        self.assertEqual(function("abbcccdddd"), "d c b a")

    def testForExampleProperInput2(self):
        self.assertEqual(function("abcd"), "a b c d")

    def testForExampleProperInput3(self):
        self.assertEqual(function("acdbabeaafgh"), "a b c d e f g h")

    def testForExampleProperInput4(self):
        self.assertEqual(function("iaaaagbbbbcfcddeeh"), "a b c d e f g h i")

    def testForNumberInput(self):
        with self.assertRaises(TypeError):
            function("das1ddw")

    def testForSpaceInput(self):
        with self.assertRaises(TypeError):
            function("asjr hb")

    def testForSymbolInput(self):
        with self.assertRaises(TypeError):
            function("j#fas")

    def testForUpperCaseInput(self):
        with self.assertRaises(SyntaxError):
            function("eruDpd")


if __name__ == "__main__":
    unittest.main()
