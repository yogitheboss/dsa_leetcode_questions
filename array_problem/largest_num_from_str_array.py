#DAY 15
#LARGEST NUMBER FORMED FROM AN ARRAY(STRING ARRAY)

#problem link:https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1

# Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.

# Example 1:

# Input: 
# N = 5
# Arr[] = {3, 30, 34, 5, 9}
# Output: 9534330
# Explanation: Given numbers are {3, 30, 34,
# 5, 9}, the arrangement 9534330 gives the
# largest value.

# Solution:
import functools
class Solution:
    #making a compare function
    def myCompare(self,x,y):
        return -1 if(x+y>y+x) else 1
    def printLargest(self,arr):
        #sorting based on compare function and joining the array
        arr.sort(key=functools.cmp_to_key(self.myCompare))
        return ''.join(arr)

arr=["3", "30", "34", "5", "9"]
Sol=Solution()
print(Sol.printLargest(arr))