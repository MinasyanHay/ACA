def Reshape(matrix,r,c):
#    if len(matrix)*len(matirx[0]) != r*c:
#        return "The shape of matrix is not equal r*c."
    Smatrix = []
    for i in matrix:
        Smatrix.extend(i)
    Rmatrix = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(Smatrix[c*i+j])
        Rmatrix.append(row)
    return Rmatrix


matrix = [[1,2],[3,4],[7,8]]
r,c = 2,3
print(Reshape(matrix,r,c))
