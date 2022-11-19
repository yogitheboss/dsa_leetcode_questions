class node:
    def __init__(self,val:any) -> None:
        self.val=val
        self.next=None

class linkedList:
    def __init__(self,head=None) -> None:
        self.head=head
    def append(self,node)->None:
        current=self.head
        if not self.head:
            self.head=node
            return
        while(current.next):
            current=current.next
        current.next=node



    def delete(self,value)->any:
        #check if head needs to delete
        if(self.head.val==value):
            self.head=self.head.next
            return
        #making temp variable
        current=self.head
        #finding matching value
        while(current):
            #if found get out of loop
            if(current.val==value):
                break
            #store prev value
            prev=current
            current=current.next
        #if no match found return
        if(not current):
            return
        
        #link prev to next of matching node and make the matched node None
        prev.next=current.next
        current=None


    def insert(self,new_node,position)->None:
        #if pos=1 then make new node the head
        if(position==1):
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        count=1
        while(current):
            #find prev correct position and make next of prev next of newnode and make next of prev the new node, hence new node added 
            if(count+1==position):
                new_node.next=current.next
                current.next=new_node
                return
            current=current.next
            count+=1
    
    def print(self):
        current=self.head
        while(current):
            print(current.val)
            current=current.next

e1=node(2)
e2=node(2)
e3=node(2)
e4=node(3)
ll=linkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.delete(2)
ll.insert(e3,3)
ll.print()