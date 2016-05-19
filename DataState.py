from enum import Enum


class DataState(object):

    def __init__(self, incomplete_data=[], current_state=""):
        self.incomplete_data = incomplete_data
        self.current_state = current_state

    def get_data(self):
        pass

    def get_current_state(self):
        pass


class DataComplete(DataState):

    def get_data(self):
        pass

    def get_current_state(self):
        pass


class DataIncomplete(DataState):

    def get_data(self):
        return self.incomplete_data

    def get_current_state(self):
        return self.current_state


class IncompleteData(Enum):
    id = 1
    gender = 2
    age = 3
    sales = 4
    bmi = 5
    income = 6

    @staticmethod
    def to_string(a_list):
        output = ""
        for bad_data in a_list:
            output += bad_data.name + ", "

        output = output[:-2]
        return output