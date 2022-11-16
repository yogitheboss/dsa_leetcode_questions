# Day 14
# CONTAINER WITH MOST WATER
#statement: ou are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
# example:Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


#solution:
def maxArea(height) -> int:
    #taking two pointer one at start and other at end.(as maximizing the width of container)
       left=0
       right=len(height)-1
       maxArea=0
       while(right>left):
        #updating maxArea 
           maxArea=max(maxArea,min(height[left],height[right])*(right-left))
           #changing shorter vertical line
           if(height[left]>height[right]):
               right-=1
           else: left+=1
       return maxArea
print(maxArea([1,8,6,2,5,4,8,3,7]))