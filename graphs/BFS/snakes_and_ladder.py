from collections import deque

# problem statement: https://leetcode.com/problems/snakes-and-ladders/submissions/884510688/


# n: number of cells in the board
# board: a list of integers of size n where ith element represents -1 if there is no snake or ladder from i, otherwise it represents the cell to which snake or ladder at i takes to.
# return the minimum number of dice throws required to reach last cell from first cell of a given snake and ladder board


board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]  

# Function to find minimum number of dice throws required to reach last cell from first cell of a given snake and ladder board


# Time complexity: O(n^2)
# Space complexity: O(n^2)
# function to convert a cell number to its row and column number
def  minDiceThrows(board):
    length=len(board)
    visited=set()
    def intToCell(num):
        row=(num-1)//length
        col=(num-1)%length
        if row%2==1:
            col=length-1-col
        return (length-1-row,col)


    queue=deque()
    queue.append([1,0]) #square,number of throws
    while queue:
        square,throws=queue.popleft()
        for i in range(1,7):
            nextSquare=square+i
            r,c=intToCell(nextSquare)
            if board[r][c]!=-1:
                nextSquare=board[r][c]
            if nextSquare==length*length:
                return throws+1
            # if square+i is not visited and is not a snake or ladder
            if nextSquare not in visited:
                visited.add(nextSquare)
                queue.append([nextSquare,throws+1])
    return -1
print(minDiceThrows(board))