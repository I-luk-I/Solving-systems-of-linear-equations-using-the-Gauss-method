import multipliers
import determinant
def solution (syst:str)->str:
    multiplier_matrix=multipliers.matrix_init(syst)
    det=determinant.matrix_determinant(multipliers.matrix_init(syst))
    x=0
    y=0
    if det==0:
        return('The matrix of this system is singular')
    if multiplier_matrix[0][0]!=1:
        divider=multiplier_matrix[0][0]
        for i in range (len(multiplier_matrix[0])):
            multiplier_matrix[0][i]=multiplier_matrix[0][i]/divider
            
    if multiplier_matrix[1][0]!=0:
        divider_1=multiplier_matrix[1][0]
        for i in range(len(multiplier_matrix[1])):
           multiplier_matrix[1][i]=multiplier_matrix[0][i]*(-divider_1)+multiplier_matrix[1][i]
            
    y=multiplier_matrix[1][-1]/multiplier_matrix[1][1]
    if multiplier_matrix[0][1]*y>0:
        x=multiplier_matrix[0][2]-(multiplier_matrix[0][1]*y)
    elif multiplier_matrix[0][1]*y<0:
        x=multiplier_matrix[0][2]+(+multiplier_matrix[0][1]*y)
    return (f'x= {x}, y= {y}, determinant={det}')



        
        


