#day 24:
#longest_repeating_character_substring :
# 424. Longest Repeating Character Replacement
#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
#You can perform this operation at most k times.
#Input: s = "ABAB", k = 2
#Output: 4
#Explanation: Replace the two 'A's with two 'B's or vice versa.
#question link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

# solution::

## APPROACH 1:
s='ACABHA'
k=2

# #window start
# left=0
# #window end
# right=0
# #character frequency in a valid window
# freq=[0]*26 
# total_string_length=len(s)
# #window maxLength 
# max_length=0
# #iterating through the entire string characters:
# while(right<total_string_length):
#     #increasing frequency count of character in freq array
#     index=ord(s[right])-ord('A')
#     freq[index]+=1
#     # checking if window is valid, if not then shifting left and 
#     # decreasing respective character count
#     while(right-left+1-max(freq)>k):
#         freq[ord(s[left])-ord('A')]-=1
#         left+=1
#     # updating maximum window length    
#     max_length=max(max_length,right-left+1)
#     right+=1
# print(max_length)



##APPROACH 2:
#window start
left=0
#window end
right=0

#character frequency in a valid window
freq=[0]*26 
total_string_length=len(s)

#window maxLength 
max_length=0

#maximum length of a char in a window(most occuring char)
max_count=0

#iterating through the entire string characters:
while(right<total_string_length):

    #increasing frequency count of character in freq array
    index=ord(s[right])-ord('A')
    freq[index]+=1

    #updating max_count(most occuring char)
    max_count=max(max_count,freq[index])

    # checking if window is valid, if not then shifting left and 
    # decreasing respective character count
    while(right-left+1-max_count>k):
        freq[ord(s[left])-ord('A')]-=1
        left+=1
    # updating maximum window length    
    max_length=max(max_length,right-left+1)
    right+=1
print(max_length)



