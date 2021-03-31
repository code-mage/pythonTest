string1 = "To forget the dead"
string2 = "would be akin to killing them"
string3 = "a second time"
#problem1
print(string1, end="_")
print(string1)
print(string2)

#problem2

#method1

string4=string1+" "+string2+" "+ string3
print(string4)

#mehod 2

print(string1,string2,string3)
print(string1,string2,string3, sep="-")

#problem 3

string5=string1+"-"+string2+"-"+ string3 
print(string5)

#problem 4

string1 = "hello"
string2 = 8
string3 = string1
string1 = string2
string2 = string3

print(string1)
print(string2)