def transpose(matrix: list[list[int]]) -> list[list[int]]:
    x=[]
    column = len(matrix[0])
    for i in range(column):
        p=[]
        for j in matrix:
            p.append(j[i])
        x.append(p)
    return x
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
transpose1=transpose(matrix1)
print(transpose1)

matrix2 = [[1,2,3],[4,5,6]]
transpose2 = transpose(matrix2)
print(transpose2)
