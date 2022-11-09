# SET MATRIX ZEROS:
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's



# solution_approach:
a=[[0,1,1],[1,0,1],[1,1,1]]

#boolean for checking if the first row or column have zero as values:
isRow=False
isCol=False

#total rows and columns in matrix
column_length=len(a)
row_length=len(a[0])

#initial values in matrix:
for i in range(column_length):
	for j in range(row_length):
		print(a[i][j],end="")
	print()	

#check if first row or column has zero or not	
for i in range(column_length):
	if(a[i][0]==0):
		isCol=True
for j in range(row_length):
	if(a[0][j]==0):
		isRow=True


#if element inside matrix is zero then making the mark of row and column to set to zero

 # 1 1 1
 # 0 1 1 
 # 1 1 1
 # now after marking:
 # 0 1 1
 # 0 1 1
 # 1 1 1
 # the first zero denotes that this row will be set to zero
for i in range(column_length):
	for j in range(row_length):
		if a[i][j]==0:
			a[i][0]=0
			a[0][j]=0


# now based on markings setting the row and column as zeros
for i in range(1,column_length):
	for j in range(1,row_length):
		if(a[i][0]==0 or a[0][j]==0):
			a[i][j]=0
# now if first row or column contained zero then we are setting the whole row or column as zeros here:
if(isCol):
	for i in range(column_length):
		a[i][0]=0
if(isRow):
	for j in range(row_length):
		a[0][j]=0


# printing the result
for i in range(column_length):
	for j in range(row_length):
		print(a[i][j],end="")
	print()	
