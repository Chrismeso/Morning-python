# A class is blueprint of an object,
# An obeject is an instance of a class

class Person:
    #Properties/AAttribute/Variable/Characteristics
    name = "Patrick"
    age = 18
    height = 21

    #Functons/Method/Behaviour
    def walk(self):
        print("person is walking")

accountant = Person() # Creating an object
accountant.walk()

teacher = Person()
teacher.walk()