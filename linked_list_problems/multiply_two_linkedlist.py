#MULTIPLY TWO LINKEDLIST

# Given elements as nodes of the two linked lists. The task is to multiply these two linked lists, say L1 and L2. 

# Note: The output could be large take modulo 109+7.
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow, the first line of each test case contains an integer N denoting the size of the first linked list (L1). In the next line are the space separated values of the first linked list. The third line of each test case contains an integer M denoting the size of the second linked list (L2). In the forth line are space separated values of the second linked list.

# Output:
# For each test case output will be an integer denoting the product of the two linked list.

# User Task:
# The task is to complete the function multiplyTwoLists() which should multiply the given two linked lists and return the result.

# Constraints:
# 1 <= T <= 100
# 1 <= N, M <= 100

# Example:
# Input:
# 2
# 2
# 3 2
# 1
# 2
# 3
# 1 0 0
# 2
# 1 0 

# Output:
# 64
# 1000

# Explanation:
# Testcase 1: 32*2 = 64.

# Testcase 2: 100*10 = 1000.

# problem link:https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1
#SOLUTION:

MOD = 10**9+7
def multiplyTwoList(head1, head2):
    temp1=head1
    temp2=head2
    value1=temp1.data
    temp1=temp1.next
    value2=temp2.data
    temp2=temp2.next

    # go through the linkedlist  1 and 2 and get the numbers value1 and value2 
    while(temp1):
        value1=(value1*10+temp1.data)%MOD
        temp1=temp1.next
    while(temp2):
        value2=(value2*10+temp2.data)%MOD
        temp2=temp2.next

    # multiply the value1 and value2
    return (value1*value2)%MOD  

class node :
	def __init__ 	(self,data):
		self.data=data
		self.next=None
	
class linkedList :
	def __init__(self):
		self.head=None
	def print(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next	

l1=linkedList()
ele1=node(2)
ele2=node(2)
ele3=node(3)
ele1.next=ele2
ele2.next=ele3
l1.head=ele1
l2=linkedList()
n1=node(9)
n2=node(1)
n1.next=n2
print(multiplyTwoList(ele1,n1))





