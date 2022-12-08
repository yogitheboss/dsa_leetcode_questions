#DAY 25

# GROUP ANAGRAMS
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#  Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

#problem link:https://leetcode.com/problems/group-anagrams/description/


# solution:
from collections import defaultdict
def groupAnagrams( strs) :
    #creating a default dict where a freq count is mapped to string and placed together
        group=defaultdict(list)
        for i in range(len(strs)):
            count=[0]*26
            for j in range(len(strs[i])):
                count[ord(strs[i][j])-ord('a')]+=1
                #separating based on freq count
            group[tuple(count)].append(strs[i])
        #returning the values (anagram groups, similar freq count groups)
        return group.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))




