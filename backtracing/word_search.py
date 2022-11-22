#DAY 20
#WORD SEARCH PROBLEM    
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#problem link:https://leetcode.com/problems/word-search/description/


def exist(wordlist, word: str) -> bool:
        w=len(word)
        row=len(wordlist)
        col=len(wordlist[0])
        
        def dfs(r,c,i):
            if(i==w):
                return True
            #checking for outofbound or previous match or char doesn't match
            if(r>row-1 or c>col-1 or r<0 or c<0 or wordlist[r][c]=='.'or word[i]!=wordlist[r][c]):
                return False
            temp=wordlist[r][c]
            #making a marker if passed a place
            wordlist[r][c]='.'
            res=(dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1))
            #backtrack to previous state
            wordlist[r][c]=temp
            return res


        for j in range(row):
            for k in range(col):
                if dfs(j,k,0):
                    return True
        return False
wordlist=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCB"
print(exist(wordlist,word))