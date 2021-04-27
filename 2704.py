# reverse list 
# permutation 
# x = 10, y = 3 get 10!/7!
# highest common factor

#Problem 1

# x = [1,2,3,4,5]

# for i in range ((len(x)-1),-1,-1):
#     print (x[i], end = " ")
    
#Problem 2

x = int(input())
y = int(input())

a=1
while x>=1:
    a = a*(x)
    x = x-1
    
b=1   
while y>=1:
    b = b*(y)
    y = y-1

print(a)
print(b)
print(a//b)
