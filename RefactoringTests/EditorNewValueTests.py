from Editor import *
from NewValueHandler import *
import unittest
import mock


class EditorNewValueCoverageTests(unittest.TestCase):

    def setUp(self):
        self.e = Editor()

    def test_id(self):
        with mock.patch('NewValueHandler.input', return_value='a123'):
            self.assertEqual(IDValueHandler.set_new_value('kj'), 'A123')

    def test_gender(self):
        with mock.patch('NewValueHandler.input', return_value='male'):
            self.assertEqual(GenderValueHandler.set_new_value('kj'), 'M')

    def test_age(self):
        with mock.patch('NewValueHandler.input', return_value='5'):
            self.assertEqual(AgeValueHandler.set_new_value('kj'), '05')

    def test_sales(self):
        with mock.patch('NewValueHandler.input', return_value='30'):
            self.assertEqual(SalesValueHandler.set_new_value('kj'), '030')

    def test_bmi(self):
        with mock.patch('NewValueHandler.input', return_value='normal'):
            self.assertEqual(BmiValueHandler.set_new_value('kj'), 'Normal')

    def test_income(self):
        with mock.patch('NewValueHandler.input', return_value='20'):
            self.assertEqual(IncomeValueHandler.set_new_value('kj'), '20')

if __name__ == "__main__":
    unittest.main(verbosity=2)

