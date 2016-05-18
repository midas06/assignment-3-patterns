from Editor import *
import unittest


class EditorStringTests(unittest.TestCase):
    def setUp(self):
        self.e = Editor()

    def test_1_input(self):
        the_input = "abc male 23000"
        output = self.e.string_to_list(the_input)
        self.assertEqual(output, ["Abcm", "", "", "", "", ""])

    def test_3_bad(self):
        the_input = "abc,male,23000"
        output = self.e.string_to_list(the_input)
        self.assertEqual(output, ["Abc", "M", "23000", "", "", ""])

    def test_good_bad(self):
        the_input = "A123,male,23000"
        output = self.e.string_to_list(the_input)
        self.assertEqual(output, ["A123", "M", "23000", "", "", ""])

    def test_good_bad_2(self):
        the_input = "T109,M,74,861,-,22"
        output = self.e.string_to_list(the_input)
        self.assertEqual(output, ["T109", "M", "74", "861", "-", "22"])

    def test_good_bad_3(self):
        the_input = "A111, female, 1, 1, ob, 22"
        output = self.e.string_to_list(the_input)
        self.assertEqual(output, ["A111", "F", "01", "001", "Ob", "22"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
