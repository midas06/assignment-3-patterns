import re


class DataValidator(object):
    @staticmethod
    def has_valid_id(an_id):
        pattern = re.compile('^([A-Z]{1}[0-9]{3})+$')

        if pattern.match(an_id) is None:
            return False

        return True

    @staticmethod
    def has_valid_gender(a_gender):
        if a_gender == 'M' or a_gender == 'F':
            return True

        return False

    @staticmethod
    def has_valid_age(an_age):
        pattern = re.compile('^([0-9]{2})+$')

        if pattern.match(an_age) is None:
            return False

        return True

    @staticmethod
    def has_valid_sales(a_sale):
        pattern = re.compile('^([0-9]{3})+$')

        if pattern.match(a_sale) is None:
            return False

        return True

    @staticmethod
    def has_valid_bmi(an_index):
        valid = ["Normal", "Overweight", "Obesity", "Underweight"]

        if an_index in valid:
            return True

        return False

    @staticmethod
    def has_valid_income(an_income):
        pattern = re.compile('^([0-9]{2,3})+$')

        if pattern.match(an_income) is None:
            return False
        return True
