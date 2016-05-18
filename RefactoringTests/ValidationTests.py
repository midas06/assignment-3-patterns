from Validator import *
import unittest


class ValidationCoverageTests(unittest.TestCase):

    def setUp(self):
        self.v = Validator()

    def test_bad_id(self):
        the_input = self.v.clean_input("A58,F,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertFalse(output)

    def test_good_id(self):
        the_input = self.v.clean_input("A558,F,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output, True)

    def test_bad_gender(self):
        the_input = self.v.clean_input("A558,D,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertFalse(output)

    def test_good_gender_female(self):
        the_input = self.v.clean_input("A558,F,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output)

    def test_good_gender_male(self):
        the_input = self.v.clean_input("A558,M,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output)

    def test_bad_age(self):
        the_input = self.v.clean_input("A58,F,sdf,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertFalse(output)

    def test_good_age(self):
        the_input = self.v.clean_input("A558,F,49,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output)

    def test_bad_sales(self):
        the_input = self.v.clean_input("A58,F,08,string,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertFalse(output)

    def test_good_sales(self):
        the_input = self.v.clean_input("A558,F,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output)

    def test_bad_bmi(self):
        the_input = self.v.clean_input("A58,F,08,885,superfat,517")
        output = self.v.isvalid(the_input)
        self.assertFalse(output)

    def test_good_bmi(self):
        the_input = self.v.clean_input("A558,F,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output)

    def test_bad_income(self):
        the_input = self.v.clean_input("A58,F,08,885,Normal,NAN")
        output = self.v.isvalid(the_input)
        self.assertFalse(output)

    def test_good_income(self):
        the_input = self.v.clean_input("A558,F,08,885,Normal,517")
        output = self.v.isvalid(the_input)
        self.assertTrue(output)

if __name__ == "__main__":
    unittest.main(verbosity=2)

