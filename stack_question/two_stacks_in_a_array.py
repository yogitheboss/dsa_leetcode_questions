#DAY 13
#TWO STACKS IN AN ARRAY

# our task is to implement  2 stacks in one array efficiently.
#You don't need to read input or print anything. You are required to complete the 4 methods push1, push2 which takes one argument an integer 'x' to be pushed into stack one and two and pop1, pop2 which returns the integer poped out from stack one and two. If no integer is present in the array return -1.
#example: Input:
# push1(2)
# push1(3)
# push2(4)
# pop1()
# pop2()
# pop2()

# Output:
# 3 4 -1

# Explanation:
# push1(2) the stack1 will be {2}
# push1(3) the stack1 will be {2,3}
# push2(4) the stack2 will be {4}
# pop1()   the poped element will be 3 
# from stack1 and stack1 will be {2}
# pop2()   the poped element will be 4 
# from stack2 and now stack2 is empty
# pop2()   the stack2 is now empty hence -1 .

#problem link:https://practice.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1


# solution:

#define global variable for the top of both stacks
top1=-1
top2=101


def push1(a,x):
    global top1
    global top2
    #check if there is space between the stacks
    if(top1<top2-1):
        top1+=1
        a[top1]=x
    else: return -1
def push2(a,x):
    global top1
    global top2
    #check if there is space between the stacks
    if(top1<top2-1):
        top2-=1
        a[top2]=x
    else: return -1
def pop1(a):
    global top2
    global top1
    #check if stack is empty
    if top1==-1:
        return -1
    else :
        #shift top pointer to left
        x=a[top1]
        top1-=1
        return x 
def pop2(a):
    global top2
    global top1
    #check if stack empty
    if top2==101:
        return -1
    else :
        #shift top  pointer to right
        x=a[top2]
        top2+=1
        return x 

a=[0]*101
push1(a,2)
push1(a,3)
push1(a,4)
push2(a,34)
push2(a,23)
print(pop1(a))
print(pop2(a))
