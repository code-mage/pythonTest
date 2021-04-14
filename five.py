# Print only odd values in an array

x = [1,2,3,4,5,6,7]
print ("the odd values are ", end="")
for i in x:
    if i % 2 != 0:
        print (i, end=" ")


# find common values between two arrays
x = [1,2,3,4,5]
y = [3,4,5,6,7]

for i in x:
    if i in y:
        print (i, end = " ")
# find max value in an array
x = [2,8,3,6,12,7]
a = x[0]
for i in range(0, len(x)):
    if x[i] > a:
        a = x[i]       
print (a)
    
# Using 3, can you sort an array. O(n^2) will be revisited.

# Given an array, can you find it it is sorted.
# XOR Gate

# Binary

rint("Enter base 10 value")
X = int(input())

while X >= 1:
    Y = X%2
    X = X//2
    Z = Y
    Z1 = str(Z) + str(Y)
    print (Z1, end=" ")