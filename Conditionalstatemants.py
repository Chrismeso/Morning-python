temperature = 32
if temperature < 25:
    print("Its is cold")
elif temperature > 25:
    print("Its is hot")
else :
    print("Normal")

 # A program that returns the largest number among the three numbers
first = 56
second = 23
third = 78

if first > second and first > third:
    print(first, "Is the largest number")

elif second > first and second > third:
    print(second, "Is the largest number")

else:
    print(third, "Is the largest number")

# A python prgram that checks if a number is even or odd

num = 78
if num  == 0:
    print(num, "is neutral number")

elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

# A python program that returns the area of a rectangle
# A = L * W
Length = 20
Width = 5
area = Length * Width
print("The area is", area)

# A python prgram that determines the area of a trapezium
# A = 0.5 (a+b)*h
a = 10
b = 20
h = 5
area1 = 0.5*(10+20)*5
print("The area is", area1)