#U18/fns/csc1100
#A program that accpet 2 number from the User and print the first number x raised to the power of y (the second number) and print x in log base 2 of x
import math
#first number variable x
x = int(input("Enter the first number: "))
#Second number variable y
y = int(input("Enter the Second number: "))
#the power of x var and y var
power = x**y
print(x, "raised to the power of ",y, "is ",power)

print("log(base 2) of",x, "is: ",math.log2(x))