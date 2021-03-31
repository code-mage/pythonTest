import Modules.lesson8Module1 as module1

#Do not use this. Very stupid
def myFun(*argv): 
    for arg in argv: 
        print (arg, end=" ")
    print()
    
def add(a,b):
    return a+b
    
def addToA(a,b):
    a = add(a,b)
    return a
    
def addToList(list, value):
    list.append(value)
    return list;

def addToListWithCopy(list, value):
    listCopy = list.copy()
    listCopy.append(value)
    return listCopy;

def add(value, increment = 1):
    return value+increment

def main():
    print("Lesson 8")
    myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
    print(add(56,73))
    #assigning functions
    addb = add
    print(addb(23,45))
    
    #Scope of variables
    a = 13
    b = 43
    c = addToA(13,43)
    print(a,b,c)
    
    #unique problems with lists
    a = [1,2,3]
    b = addToList(a,45)
    print(a)
    print(b)
    
    #unique problems with lists - how to solve
    a = [1,2,3]
    b = addToListWithCopy(a,45)
    print(a)
    print(b)
    
    #Nested functions
    a = module1.make_point(2,3)
    print(a[0]())
    print(a[1]())
    
    #Default values
    s = 23
    print(add(s))
    print(add(s,5))

if __name__ == "__main__":
    main()

print(module1.findMaxInList([23,43,65,23,12,134,5,43]))