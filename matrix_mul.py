matrix1 = [[1,2,3],
          [4,5,6],
          [3,2,1]]

matrix2 = [[1,4,0,2],
          [2,5,1,1],
          [3,6,2,0]]   

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
for r in result:
    print(r)         
