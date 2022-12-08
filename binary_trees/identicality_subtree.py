#Day 25 

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

#problem link:https://leetcode.com/problems/subtree-of-another-tree/description/

#solution
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

def depth(node,length=0):
        if(node==None):
            return 0
        return max(depth(node.left,length),depth(node.right,length))+1
def isSubtree(root,subroot):
    if(root is None):
        return False
    if(isIdentical(root,subroot)):
        return True
    return isSubtree(root.left,subroot) or isSubtree(root.right,subroot)

def isIdentical(root1,root2):
    if(root1 is None and root2 is None ):
        return True
    if(root1 is not None and root2 is not None):
        return (root1.data==root2.data) and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right) 
    return False


bt=BinaryTree(4)
bt.pushleft(3,bt.root)
bt.pushright(2,bt.root)
bt.pushright(8,bt.root.left)
bt.pushright(4,bt.root.right)
bt2=BinaryTree(2)
bt2.pushright(4,bt2.root)

print(isIdentical(bt.root,bt2.root))
print(isSubtree(bt.root,bt2.root))
