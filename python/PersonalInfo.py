# Personal Information class

class PersonalInfo:
    def __init__(self, name, date,password):
        self.__name = name
        self.__date = date
        self.__password = password

    def set_name(self, name):
        self.__name = name

    def set_age(self, date):
        self.__date = date

    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password
    
    def get_name(self):
        return "Ton nom c'est : " + self.__name


    def get_date(self):
        return "Ta date de naissance c'est : " + self.__date
