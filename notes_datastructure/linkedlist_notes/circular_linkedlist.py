#circular linkedlist has last node connected with the first node hence there is no end or start in this linkedlist

class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class CircularLL:
    def __init__(self) -> None:
        self.head=None
        self.last_node=None
    def append(self,data)->None:
        #if appending at start then make the head new node
        if(not self.head):
            self.head=node(data)
            self.last_node=self.head
            return
        # make last node's next the new node and make the new node the last node of the cll
        self.last_node.next=node(data)
        self.last_node=self.last_node.next
        self.last_node.next=self.head
    def display(self)->None:
        current=self.head
        while(current):
            print(current.data,end=" ")
            current=current.next
            if(current==self.head):
                break
cll=CircularLL()
cll.append(2)
cll.append(4)
cll.append(7)
cll.display()
        