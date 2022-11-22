#DAY 20
#MIN SUM FORMED BY DIGITS
# Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of the given array must be used to form the two numbers.

# Any combination of digits may be used to form the two numbers to be summed.  Leading zeroes are permitted.

# If forming two numbers is impossible (i.e. when n==0) then the "sum" is the value of the only number that can be formed.
# Example 1:

# Input:
# N = 6
# arr[] = {6, 8, 4, 5, 2, 3}
# Output:
# 604
# Explanation:
# The minimum sum is formed by numbers 
# 358 and 246

#problem link:https://practice.geeksforgeeks.org/problems/min-sum-formed-by-digits3551/1
# solution:
def minSum( arr, n):
        if(n==1):
            return arr[0]
        #sort array so that we could make number in order
        arr.sort()
        num1=0
        num2=0
        for i in range(n):
            #if even store number in num1
            if(i%2==0):
                print(arr[i])
                num1=num1*10+arr[i]
            #if odd store number in num2
            else:
                print(arr[i])
                num2=num2*10+arr[i]
        return num1+num2
print(minSum([6,8,4,5,2,3],6))