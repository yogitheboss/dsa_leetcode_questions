# DAY 21
# FIND THE NUMBER OF ISLANDS
# 
# Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.

# Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

# Input:
# grid = {{0,1},{1,0},{1,1},{1,0}}
# Output:
# 1
# Explanation:
# The grid is-
# 0 1
# 1 0
# 1 1
# 1 0
# All lands are connected
# You don't need to read or print anything. Your task is to complete the function numIslands() which takes the grid as an input parameter and returns the total number of islands.

# Expected Time Complexity: O(n*m)
# Expected Space Complexity: O(n*m)

# Problem link:https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1


#finding separate islands by dfs 
def numIslands(grid):
        count=0

        #checking each element if it has land and depth first searching all connected land and setting markers and increasing counter if new land is found.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0
                    count+=1
                    dfs(grid,i+1,j)
                    dfs(grid,i,j+1)
                    dfs(grid,i-1,j)
                    dfs(grid,i,j-1)
                    dfs(grid,i+1,j+1)
                    dfs(grid,i+1,j-1)
                    dfs(grid,i-1,j+1)
                    dfs(grid,i-1,j-1)
        return count
def dfs(grid,i,j):
    #return if out of bound or already visted gird element
    if(i>len(grid)-1 or j>len(grid[0])-1 or i<0 or j<0 or grid[i][j]==0):
        return
    #setting markers
    grid[i][j]=0
    dfs(grid,i+1,j)
    dfs(grid,i,j+1)
    dfs(grid,i-1,j)
    dfs(grid,i,j-1)
    dfs(grid,i+1,j+1)
    dfs(grid,i+1,j-1)
    dfs(grid,i-1,j+1)
    dfs(grid,i-1,j-1)


gird=[[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
print(numIslands(gird))


