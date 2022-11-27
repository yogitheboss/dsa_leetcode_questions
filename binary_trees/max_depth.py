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



bt=BinaryTree(4)
bt.pushleft(3,bt.root)
bt.pushright(2,bt.root)
bt.pushright(8,bt.root.left)
bt.pushright(4,bt.root.right)

print(depth(bt.root))

