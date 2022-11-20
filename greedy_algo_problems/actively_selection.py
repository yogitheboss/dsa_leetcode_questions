#Day 18 
# ACTIVELY SELECTION:
# Given N activities with their start and finish day given in array start[ ] and end[ ]. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a given day.
# Note : Duration of the activity includes both starting and ending day.
# Example 1:

# Input:
# N = 2
# start[] = {2, 1}
# end[] = {2, 2}
# Output: 
# 1
# Explanation:
# A person can perform only one of the
# given activities.
# Example 2:

# Input:
# N = 4
# start[] = {1, 3, 2, 5}
# end[] = {2, 4, 3, 6}
# Output: 
# 3
# Explanation:
# A person can perform activities 1, 2
# and 4.

#problem link: https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1

#solution:
start=[1,3,2,5]
end=[2,4,3,6]
n=4
def activitySelection(n,start,end):
    #make a tuple array containing the respective start and end
        activities=[(start[i],end[i]) for i in range(n)]
    #sort the array on basis of second element in tuple
        activities.sort(key=lambda x:x[1])
        
        answer=1
        j=0
        for i in range(1,len(activities)):
            #if start of new range is greater than last finished work day then increment answer
            if(activities[j][1]<activities[i][0]):
                answer+=1
                j=i        
        return answer

print(activitySelection(n,start,end))
