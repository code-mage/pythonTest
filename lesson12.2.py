# Balanced BST
class BalancedBSTNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = self.getHeight()
        self.parent = None
        
        if (self.right != None):
            self.right.parent = self
            
        if (self.left != None):
            self.left.parent = self
        
    def getHeight(self):
        if (self.height != None):
            return self.height
        left = 0
        right = 0
        if (self.right != None):
            right = self.right.getHeight()
            
        if (self.left != None):
            left = self.left.getHeight()
            
        return 1 + max(left, right)
    
    def rightTurn(self):
        a = self
        b = self.left
        c = self.right
        
        if (c != None):
            t3 = c.left
            
            a.right = t3
            if (t3 != None):
                t3.parent = a
            a.height = None
            a.height = a.getHeight()
            
            c.left = a
            if (a != None):
                a.parent = c
            c.height = None
            c.height = c.getHeight()
        return c;
    
    def leftTurn(self):
        a = self
        b = self.left
        c = self.right
        
        if (b != None):
            t2 = b.right
            
            a.left = t2
            if (t2 != None):
                t2.parent = a
            a.height = None
            a.height = a.getHeight()
            
            b.right = a
            if (a != None):
                a.parent = b
            b.height = None
            b.height = b.getHeight()
        return b;

    def add(self, val):
        if (val > self.val):
            if (self.right != None):
                self.right.add(val)
            else:
                self.right = BalancedBSTNode(val)
        else:
            if (self.left != None):
                self.left.add(val)
            else:
                self.left = BalancedBSTNode(val)
                
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.val)+ " " + str(self.height) + "\n"
        
        if (self.left != None):
            ret += self.left.__repr__(level+1)
            
        if (self.right != None):
            ret += self.right.__repr__(level+1)

        return ret
        
def Main():
    a = BalancedBSTNode(10);
    a.add(24)
    a.add(9)
    a.add(56)
    a.add(37)
    a.add(26)
    a.add(5)
    
    print(a)
    
    b = a.rightTurn()
    
    print(b)
    
    print(a.size())
        
if __name__=='__main__':  
    Main() 