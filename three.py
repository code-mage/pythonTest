import math

a = 9
b = 18

#Operator 1
a += b
print(a)

a =- 45
print(a)

#Operator Mod 
a = 34
b = 7
c = a%b     # The remainder left over when 34 is divided by 7. could be anything from 0 to 6
print(c)
d = a - (a//b)*b
print(d)

#Where does the + operator not work
a = 89
b = "hello"
#c = a+b         #This will not work, you can't apply oeprators to diff types of variables

#What about this
a = 12
b = "23"
#c = a+b         #Will also not work

#To make this work
d = int(b)          #called parsing
c = a+d
print(c)

# == and is
a = "hello"
b = "hello"

print(a == b)
print(a is b)       #We will revisit this when we look at lists

# type function
a = 3
b = "hello"
c = 9.8

print(type(a), type(b), type(c))

# How does import work
# These are already defined by someone in a module named math. You can import it, and use it directly.
a = 10000000
b = 10
c = math.log(a,b)
print(c)
d = math.sqrt(a)
print(d)


#String operations

#Escape quotes
a = "Elie Weisel\'s Night"
print(a)

#Format
name = "John"
age = 36
txt1 = "My name is {fname}, I'm {yourage}".format(fname = name, yourage = age)
txt2 = "My name is {0}, I'm {1}".format(name, age)
print(txt1)
print(txt2)

#Split
txt = "welcome to the party pal"
x = txt.split()
print(x)
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

#Random Operators
a = "oh boy!"
print(a.capitalize())
print(a.join("-"))

#Just try out different string operrators if you want
# you can do a. and let the IDE autocomplete. it will show you a list of operations.