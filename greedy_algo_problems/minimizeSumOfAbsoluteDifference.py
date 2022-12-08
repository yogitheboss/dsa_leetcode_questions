#Day 21
#MINIMUM SUM OF ABSOLUTE DIFFERENCE OF PAIRS

# You are given two arrays A and B of equal length N. Your task is to pair each element of array A to an element in array B, such that the sum of the absolute differences of all the pairs is minimum.

# Expected Time Complexity: O(N*log(N))
# Expected Auxiliary Space: O(1)

# problem link:https://practice.geeksforgeeks.org/problems/minimum-sum-of-absolute-differences-of-pairs/1


#SOlution:
def findMinSum( A,B,N):
    #substracting lowest values to higher values to get lowest sum. 
        A.sort()
        B.sort()
        sum=0
        for i in range(N):
            sum+=abs(A[i]-B[i])
        return sum

A=[2,3,4,7,32,2]
B=[3,87,4,23,54,3]
print(findMinSum(A,B,6))