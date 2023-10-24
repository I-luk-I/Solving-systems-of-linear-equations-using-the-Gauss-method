def matrix_determinant (matrix:list)->int:
    determinant_factor_1=0
    determinant_factor_2=0
    determinant=0
    for i in range (len(matrix)):
        for j in range (len(matrix[i])-1):
            if determinant_factor_1==0:
                determinant_factor_1=matrix[i][j]
            elif determinant_factor_2==0:
                determinant_factor_2=matrix[i][j]
            else:
                if determinant_factor_2 !=None:
                    determinant_factor_2*=matrix[i][j]
                    determinant+=determinant_factor_2
                    determinant_factor_2=None
                else:
                    determinant_factor_1*=matrix[i][j]
    determinant=determinant_factor_1-determinant  
    return determinant












matrix_determinant ('x - 7y = -59 7x + 4y = -42')