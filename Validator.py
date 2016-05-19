from Person import *
from DataCleaner import *
from DataValidator import *
from FileHandler import *


class Validator:

    def __init__(self):
        self._good_data = {}
        self._bad_data = []
        self._raw_data = None

        self._processed_data = []

    def set_raw_data(self, new_data):
        self._raw_data = new_data

    # def to_obj(self, a_list):
    #     new_person = Person(a_list[0], a_list[1], a_list[2], a_list[3], a_list[4], a_list[5])
    #     return new_person

    # def parse_data(self):
    #     for i in self._raw_data:
    #         a_list = self.clean_input(i)
    #
    #         if self.isvalid(a_list):
    #             p = self.to_obj(a_list)
    #             self._good_data.update({p.get_id(): p})
    #         else:
    #             self._bad_data.append(i)

    def parse_data(self):
        for i in self._raw_data:
            a_list = self.clean_input(i)

            p = Person()

            if self.isvalid(a_list):
                p.set_all(a_list[0], a_list[1], a_list[2], a_list[3], a_list[4], a_list[5])
                p.set_state(DataComplete())

            else:
                invalid_data = self.return_invalid_data(a_list)
                p.set_state(DataIncomplete(incomplete_data=invalid_data, current_state=i))

            self._processed_data.append(p)

    def separate_data(self):
        for p in self._processed_data:
            if p.is_complete():
                self._good_data.update({p.get_id(): p})
            else:
                self._bad_data.append(p)

    def export_good_data(self):
        return self._good_data

    def export_bad_data(self):
        return self._bad_data

    def has_bad_data(self):
        return len(self._bad_data) > 0

    ###
        # clean methods

    @staticmethod
    def clean_input(an_input):
        the_input = an_input.replace(" ", "")
        the_input = the_input.split(",")
        try:
            the_input[0] = DataCleaner.clean_id(the_input[0])
            the_input[1] = DataCleaner.clean_gender(the_input[1])
            the_input[2] = DataCleaner.clean_age(the_input[2])
            the_input[3] = DataCleaner.clean_sales(the_input[3])
            the_input[4] = DataCleaner.clean_bmi(the_input[4])
            the_input[5] = DataCleaner.clean_income(the_input[5])
        except IndexError as e:
            pass
        return the_input


    ###
        # validate methods

    @staticmethod
    def isvalid(a_list):
        if DataValidator.has_valid_id(a_list[0]) and DataValidator.has_valid_gender(a_list[1]) and DataValidator.has_valid_age(a_list[2]) and DataValidator.has_valid_sales(a_list[3]) and DataValidator.has_valid_bmi(a_list[4]) and DataValidator.has_valid_income(a_list[5]):
            return True

        return False

    @staticmethod
    def return_invalid_data(a_list):
        invalid_data = []

        if not DataValidator.has_valid_id(a_list[0]):
            invalid_data.append(IncompleteData.id)

        if len(a_list) < 2 or not DataValidator.has_valid_gender(a_list[1]):
            invalid_data.append(IncompleteData.gender)

        if len(a_list) < 3 or not DataValidator.has_valid_age(a_list[2]):
            invalid_data.append(IncompleteData.age)

        if len(a_list) < 4 or not DataValidator.has_valid_sales(a_list[3]):
            invalid_data.append(IncompleteData.sales)

        if len(a_list) < 5 or not DataValidator.has_valid_bmi(a_list[4]):
            invalid_data.append(IncompleteData.bmi)

        if len(a_list) < 6 or not DataValidator.has_valid_income(a_list[5]):
            invalid_data.append(IncompleteData.income)

        return invalid_data

    def print_bad_data(self):
        for i in self._bad_data:
            print(i.get_state().get_current_state())

    def get_all_bad_data(self):
        result = ""
        for i in self._bad_data:
            result += i + "\n"
        return result

    def empty_bad_data(self):
        self._bad_data = []

    def get_bad_data_len(self):
        return len(self._bad_data)


