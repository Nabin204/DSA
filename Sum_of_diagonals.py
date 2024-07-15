def diagonalSum(mat: list[list[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        sum=0
        for i in range(m):
            sum += mat[i][i]+mat[i][m-i-1]
        if(m%2==0):
            return sum
        else:
            pos=m//2
            return sum-mat[pos][pos]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("Sum of diagonal of given matrix is: ",diagonalSum(matrix))