#Day 18
#SPIRAL MATRIX
# Given an m x n matrix, return all elements of the matrix in spiral order.

#  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#problem link:https://leetcode.com/problems/spiral-matrix/description/

#solution:
def spiralOrder(matrix):
        output=[]
        i=0
        while(True):
            #move right 
            j=i
            k=i
            if(k<len(matrix[0])-i):
                while(k<len(matrix[0])-i):
                    output.append(matrix[j][k])
                    k+=1
                k-=1
                #if can't move then return
            else: return output
            #move down
            j+=1
            if(j<len(matrix)-i):
                while(j<len(matrix)-i):
                    output.append(matrix[j][k])
                    j+=1
                j-=1
                #if can't move then return
            else: return output
            #move left
            k-=1
            if(k>=i):
                while(k>=i):
                    output.append(matrix[j][k])
                    k-=1
                k+=1
                #if can't move then return
            else: return output
            #move up
            j-=1
            if(j>i):
                while(j>i):
                    output.append(matrix[j][k])
                    j-=1
                #if can't move then return
            else: return output
            i+=1
        return output
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))