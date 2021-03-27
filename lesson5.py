a = "hello"
b = ["h","e","l","l","o"]

# a string is basically a list
print(a[1])
print(b[1])
print(a.__len__())
print(b.__len__())
#print(a[5])

a = "hello"
b = "world"
c = a + b
print(c.__len__())
print(c[1:5])
print(c[:7])
print(c[8:])
print(c[:4]+c[4:])

print ("EDITING")
#editing list
a = [1,2,3,4,5]
a[3]=87
for x in a:
    print(x, end=" ")
    
#adding to list
print ("\nAPPEND")
a.append(3)
for x in a:
    print(x, end=" ")
    
print ("\nINSERTING")
a.insert(2, 232)
for x in a:
    print(x, end=" ")
    
print ("\nEXTEND")
a.extend([5,6,7])
for x in a:
    print(x, end=" ")

print ("\nPOP")  
a.pop()
for x in a:
    print(x, end=" ")
    
print ("\nPOP WITH INDEX")  
a.pop(2)
for x in a:
    print(x, end=" ")
    
print ("\nRemove")  
a.remove(87)
for x in a:
    print(x, end=" ")
  
print ("\nAdd")    
a = [1,2,3]
b = [4,5,6]
c = a+b
for x in c:
    print(x, end=" ")
    
print ("\nFind")
a = "people"
print (a.find("e"))

print ("Replace")
a = "people"
print (a.replace("e","r"))