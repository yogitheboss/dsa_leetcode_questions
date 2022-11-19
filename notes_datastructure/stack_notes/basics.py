class Stack:
    def __init__(self) -> None:
        self.items=[]
        self.top=0
    def push(self,val:any)->None:
        self.items.append(val)
        self.top+=1
    def pop(self)->any:
        if(self.top>0):
            self.items.pop()
            self.top-=1
    def peek(self)->any:
        if(self.top>0):
            return self.items[-1]
    def __len__(self)->None:
        return self.top
    def clear(self)->None:
        self.items=[]
        self.top=0
    def isEmpty(self)->bool:
        return self.top==0
    def printAll(self)->None:
        print(self.items)
    
