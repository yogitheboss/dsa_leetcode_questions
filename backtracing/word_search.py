#DAY 20
#WORD SEARCH PROBLEM    
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#problem link:https://leetcode.com/problems/word-search/description/


def exist(board, word):
	w=len(word)
	row=len(wordlist)
	col=len(wordlist[0])
    #set to store previous positions
	store=set()
	def dfs(r,c,i):
		if(i==w):
			return True
        # check if indexes outof bound, coming from previous place or char isn't equal
		if(r>row-1 or c>col-1 or r<0 or c<0 or (r,c) in store or word[i]!=wordlist[r][c]):
			return False
        # storing previous position
		store.add((r,c))
		res=(dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1))
        #backtrack previous position
		store.remove((r,c))
		return res


	for j in range(row):
		for k in range(col):
            #call for each char
			if dfs(j,k,0):
				return True
	return False
wordlist=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCB"
print(exist(wordlist,word))