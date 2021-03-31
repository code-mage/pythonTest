# Tuple

tuple1 = ("hello","world","1",4,5.6,4)
print (tuple1)
print(tuple1[3])

print(tuple1.__len__())
print(len(tuple1))
print(tuple1.count(4))
print(tuple1.index(4))

#can't override tuple values
#tuple1[3]=3     # That's why it's different from lists

tuple2 = tuple1.__add__((23,45))
print(tuple2)

print(tuple2[1:])
print(tuple2[4:9])





# Sets
a = "saleha"
b = set(a)
print(b)


set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(set1)

print(2 in set1)
set1.remove(2)
print(2 in set1)

print (set1)
set1.pop()
print(set1)
set1.add(89)
print(set1)

set1 = set([1,2,3])
set2 = set([3,4,5])
set3 = set1.union(set2)
print(set3)

set4 = set3.difference(set1)
print(set4)

print(set3.issuperset(set1))
print(set3.issubset(set1))



# Dictionary
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)
  
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict)
print(Dict['Name'])
print(Dict[1])

dict1 = {'Hello': 1, 'World': 2, 'dictionary': 3}
dict1['rt'] = 7
print(dict1)
dict1['Hello'] = 89
print(dict1)
print(dict1.get('Hello'))
print(dict1.get('Hello23'))
print(dict1.__contains__('ry'))
print(dict1.__contains__('rt'))

del dict1['Hello']
print(dict1)
popEl = dict1.pop('rt')
print(popEl, dict1)

dict1 = {'Hello': 1, 'World': 2, 'dictionary': 3}
popEl = dict1.popitem()
print(popEl, dict1)

print(dict1.keys())
print(dict1.values())

#How would keys work in this case
x = dict1.keys()
print(x)
dict1['ut']=45
print(x)