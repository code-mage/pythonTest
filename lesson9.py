# creates a class named Point
from typing import Tuple


class Point:  
    name = "Point"
    
    #explian self
    def Set(self, name):     
        self.name = name;
        
class GraphPoint2D: 
    #protected 
    _x = 0
    _y = 0
    
    #private
    __name="2D"
    
    
    #Init
    def __init__(self, x = 0, y=0) -> None:
        self._x = x
        self._y = y
        
    def __del__(self):
        print("die")
    
    def getPoint(self) -> Tuple:
        return (self._x, self._y)
    
    def setX(self, x):
        self._x = x
    
    def setY(self, y):
        self._y = y
        
    def getType(self):
        return self.__name
        
        
class GraphPoint3D(GraphPoint2D): 
    _z = 0 
    
    def __init__(self, x = 0, y=0, z=0) -> None:
        self._z = z
        super().__init__(x,y)
    
    def getPoint(self) -> Tuple:
        return (self._x, self._y, self._z)
    
    def setZ(self, z):
        self._z = z
        
    #This should fail
    def getType(self):
        return self.__name
  
def Main():
    # Creating an object of the Point. 
    point1 = Point() 

    # Accessing the attributes of Point
    print(point1.name)
    point1.name = "Point1"
    print(point1.name)
    
    point2 = Point()
    print(point2.name)
    
    point2.Set("Point2")
    print(point2.name)
    
    print(Point.name)
    Point.name = ("NewName")
    print(point2.name)
    print(Point.name)
    
    
    p1 = GraphPoint2D(2,4)
    print(p1.getPoint())
    p1.setY(56)
    print(p1.getPoint())
    
    p2 = GraphPoint3D(2,3,6)
    print(p2.getPoint())
    p2.setX(578)
    p2.setZ(5468)
    print(p2.getPoint())
    
    print(p1.getType())
    #This shoould fail
    #print(p2.getType())
     
# telling python that there is main in the program.
if __name__=='__main__':  
    Main()