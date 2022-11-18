# Day 16
#QUEUE REVERSAL

#Problem link:https://practice.geeksforgeeks.org/problems/queue-reversal/1
# Given a Queue Q containing N elements. The task is to reverse the Queue. Your task is to complete the function rev(), that reverses the N elements of the queue.

# Example 1:
# Input:
# 6
# 4 3 1 10 2 6

# Output: 
# 6 2 10 1 3 4

# Explanation: 
# After reversing the given
# elements of the queue , the resultant
# queue will be 6 2 10 1 3 4.

from queue import Queue

def rev(q):
    Stack = []
    #adding all value of queue in stack and empting the queue    
    while (not q.empty()):
        Stack.append(q.get())
    #readding value from stack to queue but now as stack will pop from last we put last values first
    while (Stack):
        q.put(Stack.pop())
        
    return q

q=Queue(maxsize=4)
q.put('a')
q.put('b')
q.put('c')
q.put('d')

print('reversal before queue',q.queue)
q=rev(q)
print('after reversal queue',q.queue)


# another way : we can use recursion to go throught the queue and check if queue is empty , we could contain value of each queue in each recursion call and after reaching the end we start adding into queue

# rev(queue):
#   if(not queue):return
#   value =queue.val 
#   queue.pop()
#   rev(queue)
#   queue.put(value)

