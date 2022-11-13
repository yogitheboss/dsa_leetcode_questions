#PROBLEM: Given a linked list of 0s, 1s and 2s, sort it
#question: Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

#problem link:https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
#linkedlist problem
# solution:
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
l=linkedList()
ele1=node(2)
ele2=node(2)
ele3=node(1)
ele4=node(0)
ele5=node(2)
ele6=node(1)
ele7=node(0)


ele1.next=ele2
ele2.next=ele3
ele3.next=ele4
ele4.next=ele5
ele5.next=ele6
ele6.next=ele7

l.head=ele1
# l.print()

def segregate(head):
    #taking temperory head pointer
        temp=head
        freq=[0]*3
    #getting frequency 0 1 2
        while(temp):
            freq[temp.data]+=1
            temp=temp.next
        temp=head
    #updating the linkedlist values based on frequency in ascending order    
        while(temp):
            if(freq[0] > 0):
                temp.data=0
                freq[0]-=1
            elif(freq[1]>0):
                temp.data=1
                freq[1]-=1
            elif(freq[2]>0):
                temp.data=2
                freq[2]-=1
            temp=temp.next
        return head

l.head=segregate(ele1)
l.print()