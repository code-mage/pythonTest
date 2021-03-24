#Printing Hello World
from Todo.one import string1


print("Hello World")

# don't make i a reserved word, like print
i = 10

# print = 78
# print (print)


print (i)

#variable can be reassigned
i = 20

print (i)

# In python, it can be reassigned to a diff type - int to string
i = "Whatever"

print (i)
print ("x")
print ("hello world")
print ("strings")

#Wanna learn more about print in detail - format, add, sep and end

string1 = "To forget the dead"
string2 = "would be akin to killing them"
string3 = "a second time"
#problem1
print(string1, end=" ")
print(string2, end=" ")
print(string3 )
#problem2

#method1

string4=string1+" "+string2+" "+ string3
print(string4)

#mehod 2

print(string1,string2,string3)

#problem 3

string5=string1+"-"+string2+"-"+ string3 
print(string5)

#problem 4

string1 = string1 + string2
string2 = string1[0:(len(string1)-len(string2))]
string1 = string1[len(string2):]

print(string1)
print(string2)
