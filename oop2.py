class Student:
    def __init__(self, firtsnmae, course, language):
        self.firstname = firtsnmae
        self.course = course
        self.language = language

    def details(self):
        print(self.firstname, "is sleeping")

c = Student("Caleb", "MIT", "Python")
print(c.firstname)
print(c.course)
c.details()

student2 = Student("Clarence","MIT", "Kotlin")
print(student2.firstname)
print(student2.course)
