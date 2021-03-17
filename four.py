# if conditions

from typing import Any


if (True):
    print("true")
    
if (False):
    print("false")
    
a = 10
b = 10

if (a == b):
    print("Equal")
    
if (a is b):
    print ("Equal")
else:
    print ("Not Equal")
    
a = False
b = True

if (a):
    print("a")
elif (b):
    print("b")
else:
    print("c")
    
    
#Lists
a = [1,2,3,4,5]
b = ["a","b","c","d","e"]

#index - starts at 0
print(a[2])
print(a.__len__())
#print(a[5])

#Loops
for x in a:
    print(x)
    
for x in range(0,b.__len__()):
    print(x)
    print(b[x])
    
#While Loop
i = 1
while i < 6:
  print(i)
  i += 1

#break and continue
b = 0
while b < 10:
    b += 1
    if (b == 3):
        print("b is three")
        continue
    if (b == 8):
        break
    print(b)
    
    
# nested loops
a = [1,2,3,4,5]
b = [1,2,3,4,5]

for i in a:
    for j in b:
        print(i*j)
        
        
# Any and All operators
a = [True, True, False]

print(any(a))
print(all(a))
    
    
