# Inbuilt functions
y = max(230, 321 , 5467, 12)
print(y)

x = min(230, 321 , 5467, 12)
print("the minimum value is", x)

z = pow(2, 3)
print(z)

# User defined function
def student():
    print("Chris")
student() # This is calling a function

def person():
    print("A person is walking")

person()

# parameters and arguments
def add(num1, num2):
    print(num1+num2)

add(34, 45)

def Employee(fullname, age, position, maritalstatus ):
    print(fullname, age, position, maritalstatus)
Employee("Mark Joe", 34,"Manager","single" )
Employee("Peter Griffin", 45,"Senior","married" )
Employee("Guenevive Beck", 28,"Head hunter","single" )
Employee("Joe Goldberg", 34,"Manager","single" )