class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        head = self
        string1 = "";
        while (head != None):
            string1 += str(head.val) + " "
            head = head.next
        return string1
    
    def __str__(self):
        return self.__repr__()
    
    def add(self, val):
        head = self
        while (head.next != None):
            head = head.next
        head.next = ListNode(val)
        
    def __len__(self):
        index = 1
        head = self
        while (head.next != None):
            head = head.next
            index+=1
        return index
    
    def addAtIndex(self, val, index):
        i = 1
        head = self
        while (i < index):
            head = head.next
            i+=1
        
        nextNode = head.next
        newNode = ListNode(val, nextNode)
        head.next = newNode
    
def Main():
    x = range(2,20)
    a = ListNode(1)
    head = a
    for n in x:
        a.next = ListNode(n)
        a = a.next
    print(head)
    
    # Add
    head.add(20)
    head.add(21)
    print(head)
    
    #Length
    print(len(head))
    
    #Add at index
    head.addAtIndex(34, 3)
    print(head)


if __name__=='__main__':  
    Main()        