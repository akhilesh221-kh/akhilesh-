# Write a Python program to swap two variables using a temporary variable and without
# using a temporary variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, " b =", b)

# Using a temporary variable
temp = a
a = b
b = temp

print("After swapping (using temp variable): a =", a, " b =", b)

# Write a Python Program (WAPP) to make a square of number 6 by using number pattern 6x6.

# WAPP to make a square of number 6 using a 6x6 number pattern

# size of square
n = 6  

for i in range(n):      # loop for rows
    for j in range(n):  # loop for columns
        print(6, end=" ")   # print 6 with a space
    print()   # move to next line

# .Write a program to calculate the factorial of a number using a loop

num = int(input("Enter a number: "))

fact = 1   # initialize factorial as 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):   # loop from 1 to num
        fact = fact * i
    print("Factorial of", num, "is:", fact)
print("Test commit")