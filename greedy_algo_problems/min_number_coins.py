#Day 19
#MINIMUM NUMBER OF COINS
# Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
# Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. 
# Example 1:

# Input: N = 43
# Output: 20 20 2 1
# Explaination: 
# Minimum number of coins and notes needed 
# to make 43. 


# Your Task:
# You do not need to read input or print anything. Your task is to complete the function minPartition() which takes the value N as input parameter and returns a list of integers in decreasing order.


#problem link:https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

#Solution:
def minPartition(N):
    #currency array containing all possible currency is ascending order
        currency=[ 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        coin_count=0
        #list to store currency used
        coin_list=[]
        while(N>0):
            #checking if amount is greater than the currency(biggest in list)
            while(currency[-1]<=N):
                #subtracting biggest currency from amount
                N-=currency[-1]
                #appending the type of currency in currency list
                coin_list.append(currency[-1])
                coin_count+=1
            #removing the bigger currency
            currency.pop()
        return coin_list

amount=54

print(minPartition(amount))

