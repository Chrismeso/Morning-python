


class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is studying")


accountant = Person("Joe", 34, "Male")
print(accountant.name)
print(accountant.age)



consultanat = Person("Martha", 56, "Female")
print(consultanat.name)
print(consultanat.age)

doctor = Person("Theordre", "45", "Male")
print(doctor.name)
print(doctor.age)
