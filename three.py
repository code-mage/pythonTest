
#problem 1

print("enter two values")
x, y = input().split()
print("Number of boys: ", x)
print("Number of girls: ", y)

#problem 2
#XOR Gate
print("enter first value")
aInput= int(input())
print("enter second value")
bInput= int(input())
output= aInput^bInput
print("Output is", end=" ")
print(output)

def XOR (aInput, bInput):
    if aInput != bInput:
        return 1
    else:
        return 0
    
print ("output is", XOR(aInput, bInput))

if aInput == 1 and bInput == 1:
    XORGate = "False"
    XORGateNum = 0
if aInput == 1 and bInput == 0:
    XORGate = "True"
    XORGateNum = 1
if aInput == 0 and bInput == 1:
    XORGate = "True"
    XORGateNum = 1
else:
    XORGate = "False"
    XORGateNum = 0

print('XOR Gate output is', XORGate, 'or', XORGateNum)

#problem 3

print ("enter first value")
a = int(input())
print ("enter seconf value")
b = int(input())
print ("enter third value")
c = int(input())
print ("enter fourth value")
d = int(input())

def numConcat(num1, num2):
       
        # Convert both the numbers to
        # strings
        num1 = str(num1)
        num2 = str(num2)
          
        # Concatenate the strings
        num1 += num2
          
        return int(num1)
    
e = (numConcat(a, b))
print(e)
f = (numConcat(c ,d))
print(f)
product = (e*f)
print(product)
