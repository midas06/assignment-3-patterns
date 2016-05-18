from DataCleaner import *


class NewValueHandler(object):

    @staticmethod
    def set_new_value(bad_input):
        pass


class IDValueHandler(NewValueHandler):

    @staticmethod
    def set_new_value(bad_input):
        print("The current ID value is: " + bad_input)
        print("The correct format is: 'A123'")
        new_input = input("Please set a new value:\n")
        return DataCleaner.clean_id(new_input)


class GenderValueHandler(NewValueHandler):

    @staticmethod
    def set_new_value(bad_input):
        print("The current gender value is: " + bad_input)
        print("The correct options are: 'M' or 'F'")
        new_input = input("Please set a new value:\n")
        return DataCleaner.clean_gender(new_input)


class AgeValueHandler(NewValueHandler):

    @staticmethod
    def set_new_value(bad_input):
        print("The current age value is: " + bad_input)
        print("The correct range is: 01 to 99")
        new_input = input("Please set a new value:\n")
        return DataCleaner.clean_age(new_input)


class SalesValueHandler(NewValueHandler):

    @staticmethod
    def set_new_value(bad_input):
        print("The current sales value is: " + bad_input)
        print("The correct range is: 001 to 999")
        new_input = input("Please set a new value:\n")
        return DataCleaner.clean_sales(new_input)


class BmiValueHandler(NewValueHandler):

    @staticmethod
    def set_new_value(bad_input):
        print("The current BMI value is: " + bad_input)
        print("The correct options are: Normal, Overweight, Obesity or Underweight")
        new_input = input("Please set a new value:\n")
        return DataCleaner.clean_bmi(new_input)


class IncomeValueHandler(NewValueHandler):

    @staticmethod
    def set_new_value(bad_input):
        print("The current income value is: " + bad_input)
        print("The correct range is: 00-999")
        new_input = input("Please set a new value:\n")
        return DataCleaner.clean_income(new_input)