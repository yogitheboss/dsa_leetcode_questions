#DAY 15
#IMPLEMENT STACK USING QUEUES
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

#Problem link: https://leetcode.com/problems/implement-stack-using-queues/description/


#Solution:

class MyStack:
    #contructor
    def __init__(self):
        self.arr=[]
    #pushing element to top
    def push(self, x) -> None:
        self.arr.append(x)    
    #popping element from top
    def pop(self):
        return self.arr.pop()        
    #returning top element
    def top(self):
        return self.arr[-1]
    #checking if stack array empty
    def empty(self):
        return True if not self.arr else False

stack=MyStack()
stack.push(2)
stack.push(24)
print(stack.pop())
print(stack.top())
print(stack.empty())