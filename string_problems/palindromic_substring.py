#Day 27
#Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

#Probelm link:https://leetcode.com/problems/palindromic-substrings/description/

#SOLUTION:
class Solution:
    def countSubstrings(self,s: str) -> int:
            
            def helper(i,j):
                if(i<0 or j>=len(s)):
                    return 0
                if(s[i]==s[j]):
                    return 1+helper(i-1,j+1)
                else:
                    return 0
            count=0
            for i in range(len(s)):
                count+=helper(i,i)
                count+=helper(i,i+1)

            return count

Palindromic=Solution()
print(Palindromic.countSubstrings("aaaa"))