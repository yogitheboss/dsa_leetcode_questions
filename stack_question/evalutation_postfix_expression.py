#Day 14
# Evaluation of Postfix Expression

#problem statement:Given string S representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like *, /, + and -.
# Example 1:

# Input: S = "231*+9-"
# Output: -4
# Explanation:
# After solving the given expression, 
# we have -4 as result.

# problem link:https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1


#Solution:
def evaluatePostfix(S):
    #making a stack for doing opearations 
       stack=[]
       j=0
       for i in range(len(S)):
        #check if char is a number
           if(ord(S[i])>=48):
               stack.append(int(S[i]))
               j+=1
           #if its an operator
           else:
            #do the arithmetic and store it in the container with smaller index and pop the stack
               if(S[i]=='*'):
                   stack[j-2]=stack[j-1]*stack[j-2]
                   j-=1
                   stack.pop()
               elif(S[i]=='+'):
                   stack[j-2]=stack[j-1]+stack[j-2]
                   j-=1
                   stack.pop()
               elif(S[i]=='-'):
                   stack[j-2]=stack[j-2]-stack[j-1]
                   j-=1
                   stack.pop()
               elif(S[i]=='/'):
                   stack[j-2]=stack[j-2]//stack[j-1]
                   j-=1
                   stack.pop()
           #the first element of the stack now contains the answer
       return stack[0]
print(evaluatePostfix("231*+9-"))