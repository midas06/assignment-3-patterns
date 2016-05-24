from Validator import *
from Person import *
from NewValueHandler import *


class Editor(object):

    def __init__(self):
        self._raw_data = None
        self._good_data = {}

    def set_raw(self, new_data):
        self._raw_data = new_data

    # def edit(self):
    #     while len(self._raw_data) > 0:
    #         s = self._raw_data[0]
    #         (print("Bad data: \n" + s))
    #         self.edit_or_delete(s)
    #     print ("All bad data has been handled")

    def edit(self):
        while len(self._raw_data) > 0:
            bad_obj = self._raw_data[0]
            the_state = bad_obj.get_state()
            print("The following data is invalid: \n" + IncompleteData.to_string(the_state.get_data()))
            print("\nThe current data is:\n" + the_state.get_current_state())
            self.edit_or_delete(bad_obj)
        print ("All bad data has been handled")

    # def edit_or_delete(self, a_string):
    #     i = input("Press 'E' to edit the data, press 'D' to delete it.\n")
    #     if i == 'E' or i == 'e':
    #         self.validate(a_string)
    #     elif i == 'D' or i == 'd':
    #         self.remove_from_raw(a_string)
    #     else:
    #         self.edit_or_delete(a_string)

    def edit_or_delete(self, a_person):
        i = input("Press 'E' to edit the data, press 'D' to delete it.\n")
        if i == 'E' or i == 'e':
            self.validate(a_person)
        elif i == 'D' or i == 'd':
            self.remove_from_raw(a_person)
        else:
            self.edit_or_delete(a_person)

    # def remove_from_raw(self, the_string):
    #     if the_string in self._raw_data:
    #         self._raw_data.remove(the_string)

    def remove_from_raw(self, a_person):
        if a_person in self._raw_data:
            self._raw_data.remove(a_person)

    @staticmethod
    def string_to_list(a_string):
        list_ = [""] * 6
        temp = Validator.clean_input(a_string)

        for i in range(len(temp)):
            list_[i] = temp[i]

        return list_

    # def validate(self, a_string):
    #     list_ = Editor.string_to_list(a_string)
    #
    #     id_ = list_[0]
    #     gender = list_[1]
    #     age = list_[2]
    #     sales = list_[3]
    #     bmi = list_[4]
    #     income = list_[5]
    #
    #     while not DataValidator.has_valid_id(id_):
    #         id_ = IDValueHandler.set_new_value(id_)
    #
    #     while not DataValidator.has_valid_gender(gender):
    #         gender = GenderValueHandler.set_new_value(gender)
    #
    #     while not DataValidator.has_valid_age(age):
    #         age = AgeValueHandler.set_new_value(age)
    #
    #     while not DataValidator.has_valid_sales(sales):
    #         sales = SalesValueHandler.set_new_value(sales)
    #
    #     while not DataValidator.has_valid_bmi(bmi):
    #         bmi = BmiValueHandler.set_new_value(bmi)
    #
    #     while not DataValidator.has_valid_income(income):
    #         income = IncomeValueHandler.set_new_value(income)
    #
    #     p = Person(DataCleaner.clean_id(id_), DataCleaner.clean_gender(gender), DataCleaner.clean_age(age), DataCleaner.clean_sales(sales), DataCleaner.clean_bmi(bmi), DataCleaner.clean_income(income))
    #
    #     self._good_data.update({p.get_id(): p})
    #     self._raw_data.remove(a_string)

    def validate(self, a_person):

        incomplete_data = a_person.get_state().get_data()

        if IncompleteData.id in incomplete_data:
            print(a_person.get_id())
            while not DataValidator.has_valid_id(a_person.get_id()):
                a_person.set_id(IDValueHandler.set_new_value(a_person.get_id()))

        if IncompleteData.gender in incomplete_data:
            print(a_person.get_gender())
            while not DataValidator.has_valid_gender(a_person.get_gender()):
                print(a_person.get_gender())
                a_person.set_gender(GenderValueHandler.set_new_value(a_person.get_gender()))

        if IncompleteData.age in incomplete_data:
            while not DataValidator.has_valid_age(a_person.get_age()):
                a_person.set_age(AgeValueHandler.set_new_value(a_person.get_age()))

        if IncompleteData.sales in incomplete_data:
            while not DataValidator.has_valid_sales(a_person.get_sales()):
                a_person.set_sales(SalesValueHandler.set_new_value(a_person.get_sales()))

        if IncompleteData.bmi in incomplete_data:
            while not DataValidator.has_valid_bmi(a_person.get_bmi()):
                a_person.set_bmi(BmiValueHandler.set_new_value(a_person.get_bmi()))

        if IncompleteData.income in incomplete_data:
            while not DataValidator.has_valid_income(a_person.get_income()):
                a_person.set_income(IncomeValueHandler.set_new_value(a_person.get_income()))

        a_person.set_state(DataComplete())

        self._good_data.update({a_person.get_id(): a_person})
        self._raw_data.remove(a_person)

        print("\n***\nData successfully updated!\n***")

    def export_good_data(self):
        return self._good_data

    def export_bad_data(self):
        return self._raw_data