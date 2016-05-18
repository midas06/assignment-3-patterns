class DataCleaner(object):

    @staticmethod
    def clean_id(an_id):
        an_id = an_id.title()
        if len(an_id) > 4:
            ex = len(an_id) - 4
            an_id = an_id[:-ex]
        return an_id

    @staticmethod
    def clean_gender(a_gender):
        if len(a_gender) > 1:
            ex = len(a_gender) - 1
            a_gender = a_gender[:-ex]
        return a_gender.title()

    @staticmethod
    def clean_age(an_age):
        if len(an_age) == 1:
            an_age = "0" + an_age
        return an_age

    @staticmethod
    def clean_sales(a_sale):
        if len(a_sale) == 1:
            a_sale = "00" + a_sale
        elif len(a_sale) == 2:
            a_sale = "0" + a_sale
        return a_sale

    @staticmethod
    def clean_bmi(an_index):
        return an_index.title()

    @staticmethod
    def clean_income(an_income):
        if len(an_income) == 1:
            an_income = "0" + an_income
        return an_income