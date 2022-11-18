#DAY 16
#OVERLAPPING INTERVALS
# Given a collection of Intervals, the task is to merge all of the overlapping Intervals.
# Example 1:

# Input:
# Intervals = {{1,3},{2,4},{6,8},{9,10}}
# Output: {{1, 4}, {6, 8}, {9, 10}}
# Explanation: Given intervals: [1,3],[2,4]
# [6,8],[9,10], we have only two overlapping
# intervals here,[1,3] and [2,4]. Therefore
# we will merge these two and return [1,4],
# [6,8], [9,10].

# Your Task:
# Complete the function overlappedInterval() that takes the list N intervals as input parameters and returns sorted list of intervals after merging.

#problem link:https://practice.geeksforgeeks.org/problems/8a644e94faaa94968d8665ba9e0a80d1ae3e0a2d/1

arr=[[1,2],[3,4],[4,6],[5,8]]

def overlappedInterval(arr):
        result=[]
        #sorting based on first index of each interval 
        arr.sort(key=lambda x: x[0])
        for i in range(len(arr)):
            #if result empty or non overlapping interval  
            if not result or result[-1][1]<arr[i][0]:
                result.append([arr[i][0],arr[i][1]])
            else: 
                #if overlapping interval then update the 2nd index of interval to greater value
                result[-1][1]=max(result[-1][1],arr[i][1])
        return result

print(overlappedInterval(arr))
