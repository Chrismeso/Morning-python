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

num = int (input ("Enter any number to test whether it is odd or even:"))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
