#input typecasting
print("Try to enter an alphabet")
value1 = input()
value2 = int(value1)
print (value2+1)

print("Please input integers only")
a = int(input())
b = int(input())

#Operator 1
print (a+b);

print (a-b);

print (a*b);

#division later

# Operator 2
print (a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

#Operator 3
a = True
b = False

print(a or b)
print(a and b)
print(not a)

#Do these operators work outside int
#Yes, but don't really use anything execpt +
a = "hello"
b = "world"

print (a+b);
# - & // don't work

#alphabetical
print (a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

#complicated, useless, do you really want to know
print(a or b)
print(a and b)
print(not a)

#cool
h = 6
print(a*6)


# division
a = 5
b = 2
c = -5

# // is integer division. It uses the floor value
print(a//b)
print (c//b)

d = 5.0
e = 2.0
f = -5.0

# / is float division
print(d/e)
print(f/e)

# Guess
val1 = 6.0
val2 = 2.0
val3 = 6
val4 = 2

print(val1/val2)
print(val1//val2)
print(val3/val4)
print(val3//val4)

print(val1/val4)
print(val1//val4)
print(val3/val2)
print(val3//val2)

# Guess again
val1 = 5.0
val2 = 2.0
val3 = 5
val4 = 2

print(val1/val2)
print(val1//val2)
print(val3/val4)
print(val3//val4)

print(val1/val4)
print(val1//val4)
print(val3/val2)
print(val3//val2)

# You don't need to remember it. It's just for fun
# But if you want to - // will awlays give the floor, no matter the argument. And if any one argument is float, the answer will be written as float