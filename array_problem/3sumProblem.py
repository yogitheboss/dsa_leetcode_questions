#Day 13 problem
#3SUM Problem


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
#example:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

#problem link:https://leetcode.com/problems/3sum/description/


# solution:
def threeSum( nums) :
    # list to store the answer
        answer=[]
        #sorting the list
        nums.sort()
        #looping through the array from first element to 3rd last element
        for i in range(len(nums)-2):
            #continue if current element equals the previous element
            if(i !=0 and nums[i]==nums[i-1]):
                continue
            
            j=i+1
            k=len(nums)-1
            #now iterating using two pointers such that one pointer start from next element and other start from last so that if value is greater than 0 then we could reduce the right pointer and if less than 0 then can increase the left pointer
            while(j<k):    
                total=nums[i]+nums[j]+nums[k]
                if(total<0):
                    j+=1
                elif(total==0 ):
                    answer.append([nums[i],nums[j],nums[k]])
                    #checking if the next element is equal 
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    else: j+=1    
                elif(total>0):
                    k-=1
        return answer
numbers=[-8,3,4,2,4,2,2,3]
print(threeSum(numbers))