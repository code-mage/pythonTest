#ignore this part, we will get to it later.
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Files/text1.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#Ignore this too
file = open(abs_file_path,'w')
file.writelines(["Line1\n","Line2\n","Line3\n","Line4\n","Line5\n","Line6"])
file.close()

#opening file
fo = open(abs_file_path)
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
print ("Closed or not : ", fo.closed)

#reading mode
file = open(abs_file_path, 'r')
for line in file:
    print (line)
file.close()

file = open(abs_file_path, "r") 
print (file.read())
file.close()

file = open(abs_file_path, "r") 
print (file.read(12))
file.close()

file = open(abs_file_path, "r") 
print (file.readline())
print (file.readline())
file.close()

file = open(abs_file_path, "r") 
print (file.readlines())
file.close()

#Append Mode
file = open(abs_file_path,'a')
file.write("\nAdding a new line")
file.close()


file = open(abs_file_path,'a')
file.writelines(["\nLine11","\nLine12","\nLine13"])
file.close()


#Write Mode
file = open(abs_file_path,'w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


file = open(abs_file_path,'w')
file.writelines(["Line1\n","Line2\n","Line3\n","Line4\n","Line5\n","Line6"])
file.close()

#Using with
with open(abs_file_path, "w") as f: 
    f.write("Hello World!!!") 

with open(abs_file_path) as reader:
    print(reader.read(3))
    print(reader.tell())
    print(reader.read(5))
    print(reader.tell())
    reader.seek(0,0)
    print(reader.read(3))


with open(abs_file_path) as reader:
    print(reader.readline(3))
    print(reader.tell())
    print(reader.readline(5))
    print(reader.tell())
    reader.seek(0,0)
    print(reader.readline(3))


# Exception Handling
try:
    #file = open("a.txt",'r')
    file = open(abs_file_path,'r')
except(FileNotFoundError):
    print("File not found. Enter a valid file")
else:
    print("File found")
finally:
    print("Exit Loop")
    
#Handle all exceptions
try:
    a = 3/0
except Exception as e:
    print("Any random exception")
    print(e.__class__)
    
    
#Handle multiple exceptions
try:
    #a = 3/0
    b = "2"+45
except (TypeError, ZeroDivisionError):
    print("Caught")
    
#Throw an exception
try:
    raise MemoryError("random reasons")
except MemoryError:
    print("caught")

#Ignore this. This is just for file sanity
file = open(abs_file_path,'w')
file.writelines(["Line1\n","Line2\n","Line3\n","Line4\n","Line5\n","Line6"])
file.close()