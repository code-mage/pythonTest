#Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        if (self == None):
            return ""
        
        left = ""
        if (self.left != None):
            left = str(self.left)
            
        right = ""
        if (self.right != None):
            right = str(self.right)

        return left+ " " + str(self.val) + " " + right
    
    def __str__(self):
        return self.__repr__()
    
def Main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(root)
    
# Binary Search Tree
# nodes on the left are always smaller, nodes on the right are always larger

# create a BST
# Add values to the BST
# Remove values from the BST
# Find values in the BST
# Flatten the tree and get a sorted list
# use BST to sort the list

if __name__=='__main__':  
    Main()        