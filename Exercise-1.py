class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
    
def preorderPrint(root):
    
    if root:
        print(root.val, end = "--->")
    else:
        print("No nodes!")
    if root.left:
        preorderPrint(root.left)
    if root.right:
        preorderPrint(root.right)

def inorderPrint(root):
    
    if root:
        if root.left:
            inorderPrint(root.left)
        print(root.val, end = "--->")
        if root.right:
            inorderPrint(root.right)
    else:
        print("No Nodes!")
        
def postorderPrint(root):
    
    if root:
        if root.left:
            postorderPrint(root.left)
        if root.right:
            postorderPrint(root.right)
        print(root.val, end = "--->")
    else:
        print("No Nodes!")


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(17)
root.right.left = TreeNode(6)
root.right.right = TreeNode(3)

print("\nPreorder: ", end = "")
preorderPrint(root)

print("\nInorder: ", end = "")
inorderPrint(root)

print("\nPostorder: ", end = "")
postorderPrint(root)
