class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_name(self):
        print("Имя", self.first_name)

    def say_surname(self):
        print("Фамилия", self.last_name)

    def say_fullname(self):
        print("Ф.И.:", self.first_name, self.last_name)
