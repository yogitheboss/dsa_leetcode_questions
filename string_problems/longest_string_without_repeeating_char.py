#DAY 23

#LONGEST STRING WITHOUT REPEATING CHARACTERS

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#PROBELM LINK:https://leetcode.com/problems/longest-substring-without-repeating-characters/

#SOLUTION :
def lengthOfLongestSubstring(s: str) -> int:
    # a set containing elements of non repeting substr
        nonrepeating_set=set()
        count=0
        left=0
        for i in range(len(s)):

            # if we found a duplicate of current substr then remove from left till we have no further duplicate.
            while(s[i] in nonrepeating_set):
                nonrepeating_set.remove(s[left])
                left+=1
            nonrepeating_set.add(s[i])
            # updating count based on substr length
            count=max(count,i-left+1)
        return count
print(lengthOfLongestSubstring('abcdeabc'))
