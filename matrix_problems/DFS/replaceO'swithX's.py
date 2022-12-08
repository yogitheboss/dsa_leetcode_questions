# Day 22 
# Replace O's with X's

# Given a matrix mat of size N x M where every element is either ‘O’ or ‘X’.
# Replace all ‘O’ with ‘X’ that are surrounded by ‘X’.
# A ‘O’ (or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left and just right of it

# Input: n = 5, m = 4
# mat = {{'X', 'X', 'X', 'X'}, 
#        {'X', 'O', 'X', 'X'}, 
#        {'X', 'O', 'O', 'X'}, 
#        {'X', 'O', 'X', 'X'}, 
#        {'X', 'X', 'O', 'O'}}
# Output: ans = {{'X', 'X', 'X', 'X'}, 
#                {'X', 'X', 'X', 'X'}, 
#                {'X', 'X', 'X', 'X'}, 
#                {'X', 'X', 'X', 'X'}, 
#                {'X', 'X', 'O', 'O'}}
# Your Task:
# You do not need to read input or print anything. Your task is to complete the function fill() which takes n, m and mat as input parameters ad returns a 2D array representing the resultant matrix.

# Expected Time Complexity: O(n*m)
# Expected Auxiliary Space: O(n*m)

# Problem link: https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1

def helper(mat,i,j):
    if(i<0 or j<0 or i>len(mat)-1 or j>len(mat[0])-1 or mat[i][j]=='-' ):
        return
    if(mat[i][j]=='X'):
        return
    mat[i][j]='-'
    helper(mat,i+1,j)
    helper(mat,i,j+1)
    helper(mat,i,j-1)
    helper(mat,i-1,j)
def fill( n, m, mat):
        for i in range(n):
            if(mat[i][0]=='O'):
                helper(mat,i,0)
            if(mat[i][m-1]=='O'):
                helper(mat,i,m-1)
        for j in range(m):
            if(mat[0][j]=='O'):
                helper(mat,0,j)
            if(mat[n-1][j]=='O'):
                helper(mat,n-1,j)
                
        for i in range(n):
            for j in range(m):
                if(mat[i][j]=='-'):
                    mat[i][j]='O'
                else:
                    mat[i][j]='X'
                    
        return mat



n = 5
m = 4
mat = [['X', 'X', 'X', 'X'],['X', 'O', 'X', 'X'],['X', 'O', 'O', 'X'],['X', 'O', 'X', 'X'],['X', 'X', 'O', 'O']]
mat2=fill(n,m,mat)
print(mat)