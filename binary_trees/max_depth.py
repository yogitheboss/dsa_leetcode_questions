#DAY 23

#MAXIMUM DEPTH OF BINARY TREE
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
 

# problem link:https://leetcode.com/problems/maximum-depth-of-binary-tree/

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

        #getting max of left and right branches
        return max(depth(node.left,length),depth(node.right,length))+1



bt=BinaryTree(4)
bt.pushleft(3,bt.root)
bt.pushright(2,bt.root)
bt.pushright(8,bt.root.left)
bt.pushright(4,bt.root.right)

print(depth(bt.root))

