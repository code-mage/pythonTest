def main():
    print("Lesson 8 Module 1")
    
def findMaxInList(a):
    max = a[0];
    for val in a:
        if (val>max):
            max = val
    return max

def make_point(x, y):
    def get_x():
        return x
    def get_y():
        return y
    a=(get_x,get_y)
    return a

if __name__ == "__main__":
    main()


#If this isn't commented, it will be printed every time the file is imported.
#print(findMaxInList([23,43,65,23,12,134,5,43]))