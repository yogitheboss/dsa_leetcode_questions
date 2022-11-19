#in doubly linkedlist we have both next and previous pointers
#we can hence travese from left to right or from right to left

class node:
    def __init__(self,data) -> None:
        self.data=data
        self.prev=None
        self.next=None

class doublyLL:
    def __init__(self) -> None:
        self.head=None
        self.last_node=None
    def append(self,data)->None:
        if(not self.head):
            self.head=node(data)
            self.last_node=self.head
            return
        newnode=node(data)
        self.last_node.next=newnode
        newnode.prev=self.last_node
        newnode.next=None
        self.last_node=newnode
    def display(self,command)->None:
        if(command=='left to right'):
            temp=self.head
            while(temp):
                print(temp.data,end=' ')
                temp=temp.next
        else:
            temp=self.last_node
            while(temp):
                print(temp.data,end=' ')
                temp=temp.prev

dll=doublyLL()
dll.append(2)
dll.append(4)
dll.append(6)
dll.display('left to right')
print()
dll.display('right to left')