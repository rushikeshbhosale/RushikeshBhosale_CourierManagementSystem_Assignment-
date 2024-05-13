# entity/CourierCompanyCollection.py

class CourierCompanyCollection:
    def __init__(self):
        self.__companies = []

    def add_company(self, company):
        self.__companies.append(company)

    def remove_company(self, company):
        self.__companies.remove(company)

    def get_companies(self):
        return self.__companies

    def __str__(self):
        return f"Companies: {self.__companies}"
