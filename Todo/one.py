string1 = "To forget the dead"
string2 = "would be akin to killing them"
string3 = "a second time"

# Problem 1
# Multiple print statements, that prints these strings in the same line.
# Output expected - To forget the dead would be akin to killing them a second time
print(string1, end=" ")         #instead of ending the string with a new line, the end parameter ends the string with the value provided in it
print(string2, end=" ")
print(string3 )

# Problem 2
# A single print statement that prints all these three strings seperated by a space
# Output expected - To forget the dead would be akin to killing them a second time
# There are 2 ways to do this

# Method1
print(string1+" "+string2+" "+ string3)

# Method2
print(string1,string2,string3)

# Problem 3
# A single print statement that prints all these three strings seperated by a dash
# Output expected - To forget the dead-would be akin to killing them-a second time

# Method1
print(string1+"-"+string2+"-"+ string3 )

# Method2
print(string1,string2,string3, sep="-")     # sep seperates the strings entered in the statement with the value inside sep.

# Problem 4
# Swap variables string1 and string2
# There are two ways to do this


# Method 1
string1 = string1 + string2
string2 = string1[0:(len(string1)-len(string2))]
string1 = string1[len(string2):]

print(string1)      # should read - would be akin to killing them
print(string2)      # should read - To forget the dead

#Method 2
string4 = string1
string1 = string2
string2 = string4

print(string1)      # should read - To forget the dead
print(string2)      # should read - would be akin to killing them