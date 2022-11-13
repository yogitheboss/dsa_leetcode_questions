# PRODUCT EXCEPT SELF


# question
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

#example:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


# link: https://leetcode.com/problems/product-of-array-except-self/description/

# Solution:


nums=[1,2,3,4]

def productExceptSelf(numbers):
    #result array
     result=[1]*len(nums)
     mult=1
    #prefix multiplication  
     for i in range(1,len(nums)):
         mult*=nums[i-1]
         result[i]=mult
     mult=1
    #suffix  multiplied by prefix multiplication  
     for i in reversed(range(len(nums)-1)):
         mult*=nums[i+1]
         result[i]*=mult
    #return result
     return result
     
productnums=productExceptSelf(nums)
print(productnums)
