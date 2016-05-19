from DataState import *


class Person(object):

    def __init__(self):
        self._id = None
        self._gender = None
        self._age = None
        self._sales = None
        self._bmi = None
        self._income = None
        self._state = DataState()

    def set_all(self, new_id, new_gender, new_age, new_sales, new_bmi, new_income):
        self._id = new_id
        self._gender = new_gender
        self._age = new_age
        self._sales = new_sales
        self._bmi = new_bmi
        self._income = new_income

    def get_id(self):
        return self._id

    def get_gender(self):
        return self._gender

    def get_age(self):
        return self._age

    def get_sales(self):
        return self._sales

    def get_bmi(self):
        return self._bmi

    def get_income(self):
        return self._income

    def get_state(self):
        return self._state

    def set_id(self, new_id):
        self._id = new_id

    def set_income(self, new_income):
        self._income = new_income

    def set_gender(self, new_gender):
        self._gender = new_gender

    def set_age(self, new_age):
        self._age = new_age

    def set_sales(self, new_sales):
        self._sales = new_sales

    def set_bmi(self, new_bmi):
        self._bmi = new_bmi

    def set_state(self, new_state):
        self._state = new_state

    def is_complete(self):
        return type(self._state) is DataComplete
