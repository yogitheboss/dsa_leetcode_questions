#DAY 19
#ROTATE ARRAY 

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotatio
# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

#problem link:https://leetcode.com/problems/rotate-image/submissions/


#Solution:

matrix=[[1,2,3],[4,5,6],[7,8,9]]


#function to flip the array
def updown(matrix):
	n=len(matrix)
	for i in range(n//2):
		for j in range(len(matrix[0])):
            #swapping upward elements with downward element
			matrix[i][j],matrix[n-1-i][j]=matrix[n-1-i][j],matrix[i][j]
	return matrix


def print_2d(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j],end=" ")
		print( )

#rotating function        
def rotate(matrix):
	matrix=updown(matrix)
	print_2d(matrix)
    #swapping elements with i,j with j,i elements
	for i in range(len(matrix)):
		for j in range(i,len(matrix)):
			matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
	print_2d(matrix)

rotate(matrix)


