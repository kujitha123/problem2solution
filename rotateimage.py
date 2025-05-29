#rotate image logic:-[i][j]=>[j][n-i-1] of roated matrix
def rotate(matrix):
        n=len(matrix)
        m=len(matrix[0])
        dupMat=[]
        for i in range(n):
            temp=[0]*n
            dupMat.append(temp)
        for i in range(0,n):
            for j in range(0,n):
                dupMat[j][n-i-1]=matrix[i][j]
        for i in range(0,n):
            for j in range(0,n):
                matrix[i][j]=dupMat[i][j]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))