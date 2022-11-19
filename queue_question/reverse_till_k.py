#Day 17

#problem link:https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1

# Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.
# Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.

# Example 1:

# Input:
# 5 3
# 1 2 3 4 5

# Output: 
# 3 2 1 4 5

# Explanation: 
# After reversing the given
# input from the 3rd position the resultant
# output will be 3 2 1 4 5.

# Your Task:
# Complete the provided function modifyQueue that takes queue and k as parameters and returns a modified queue. The printing is done automatically by the driver code.

# Expected Time Complexity : O(N)
# Expected Auxiliary Space : O(K)

# from queue import Queue
# q=Queue()
# q.put(23)
# q.put(23)
# q.put(23)
# q.put(23)
# q.get()
# print(q.queue)

# list=[2,34]
# print(list.pop(0))

#solution:

q=[1,2,3,4,5]
k=3
def modifyQueue(q,k):
    #making a stack
    stack=[]
    #pushing first k values in a stack and removing from queue
    for i in range(k):
        stack.append(q.pop(0))
    #now pushing k values from stack to the queue 
    while(stack):
        q.append(stack.pop())
    #now shifting length-k values from start to end 
    for i in range(len(q)-k):
        q.append(q.pop(0))
    return q
q=modifyQueue(q,k)
print(q)


#example  queue=1 2 3 4 5 
#           taking value from queue to stack:stack 1 2 3 
#                                               queue 4 5
#           pushing value from stack to queue:queue: 4 5  3 2 1 ,stack:[]      
#           now shift 4 ,5 from start to end: queue: 3 2 1 4 5

