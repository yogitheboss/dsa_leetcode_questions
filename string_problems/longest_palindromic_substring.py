#LONGEST PALINDROMIC SUBSTRING


# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


#problem link:https://leetcode.com/problems/longest-palindromic-substring/description/


#solution:


#approach: take each index and expand around it till its a valid palindrome
#find the largest length from it.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength=0
        index=0
        if(len(s)==1):
            return s
        for i in range(len(s)-1):
            len1,index1=self.helper(s,i,i)
            if(len1>maxlength):
                index=index1
                maxlength=len1
            len2,index2=self.helper(s,i,i+1)
            if(len2>maxlength):
                index=index2
                maxlength=len2
        return s[index:index+maxlength]

        #function to expand around index if valid substring
    def helper(self,s,i,j):
        while(i>=0 and j<len(s) and s[i]==s[j] ):
            i-=1
            j+=1
        i+=1
        j-=1
        return (j-i+1,i)

s = "babad"
solve=Solution()
print(solve.longestPalindrome(s))