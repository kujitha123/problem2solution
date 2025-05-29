def searchMatrix(matrix,target):
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col=m-1
        while(row<n and col>=0):
            if(matrix[row][col]==target):
                return True
            elif(target>matrix[row][col]):
                row+=1
            elif(target<matrix[row][col]):
                col-=1
        return False
matrix=[[1,2,3],[4,5,6],[7,8,9]]
target=int(input())
print(searchMatrix(matrix,target))
