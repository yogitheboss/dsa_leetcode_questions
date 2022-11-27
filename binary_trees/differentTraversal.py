#Day 24

#problem link : https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1

# Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.
# Example 1:

# Input :
#         1
#       /   \
#      3     2

# Output: 3 2 1
# Explanation:
# Traversing level 1 : 3 2
# Traversing level 0 : 1
# Example 2:

# Input :
#        10
#       /  \
#      20   30
#     / \ 
#    40  60

# Output: 40 60 20 30 10
# Explanation:
# Traversing level 2 : 40 60
# Traversing level 1 : 20 30
# Traversing level 0 : 10


#Solution:
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,data) -> None:
        self.root=Node(data)

    def pushleft(self,data,node):
        n=Node(data)
        if(node==None):
            return 'root is not defined'
        else:
            node.left=n
    def pushright(self,data,node):
        n=Node(data)
        if(node==None):
            return 'root is not defined'
        else:
            node.right=n
    def traversalInOrder(self,node):
        if(node==None):
            return
        self.traversalInOrder(node.left)
        print(node.data,end=' ')
        self.traversalInOrder(node.right)
    def traversalPostOrder(self,node):
        if(node==None):
            return
        self.traversalPostOrder(node.left)
        self.traversalPostOrder(node.right)
        print(node.data,end=' ')
    def traversalPreOrder(self,node):
        if(node==None):
            return
        
        print(node.data,end=' ')
        self.traversalPreOrder(node.left)
        self.traversalPreOrder(node.right)
def depth(node,length=0):
        if(node==None):
            return 0
        return max(depth(node.left,length),depth(node.right,length))+1

def printLevel(root,level):
    if(root is None):
        return
    if(level==1):
        print(root.data,end=" ")
        return 
    printLevel(root.left,level-1)
    printLevel(root.right,level-1)

def printLevelOrder(root):
    height=depth(root)
    for i in range(1,height+1):
        printLevel(root,i)
def printReversalLevelOrder(root):
    height=depth(root)
    for i in reversed(range(1,height+1)):
        printLevel(root,i)

bt=BinaryTree(4)
bt.pushleft(3,bt.root)
bt.pushright(2,bt.root)
bt.pushright(8,bt.root.left)
bt.pushright(4,bt.root.right)
print('\nInorder traversal')
bt.traversalInOrder(bt.root)
print('\nPostOrder traversal')
bt.traversalPostOrder(bt.root)
print('\nPreOrder traversal')
bt.traversalPreOrder(bt.root)
print('\nPrint level order')
printLevelOrder(bt.root)
print('\nPrint reverse level order')
printReversalLevelOrder(bt.root)

