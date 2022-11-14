#MAXIMUM PRODUCT SUBARRAY
#Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer
# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Problem link:https://leetcode.com/problems/maximum-product-subarray/description/

# Solution :


def maxProduct(nums) -> int:
        # maximumProduct=nums[0]
        # for i in range(len(nums)):
        #     maximumProduct=max(maximumProduct,nums[i])
        #     currentMax=nums[i]
        #     for j in range(i+1,len(nums)):
        #         currentMax*=nums[j]
        #         maximumProduct=max(maximumProduct,currentMax)
        # return maximumProduct

        #initializing maximum till now
        maximum=nums[0]

        #separate imax and imin for each index
        imax=imin=maximum


        for i in range(1,len(nums)):
            #swap max if nums[i] is negative
            if(nums[i]<0):
                imax,imin=imin,imax
            #update imax and imin
            imax=max(nums[i],imax*nums[i])
            imin=min(nums[i],imin*nums[i])
            #check if maximum changed
            maximum=max(maximum,imax)
        return maximum

        
numbers=[1,2,3,4]
print(maxProduct(numbers))