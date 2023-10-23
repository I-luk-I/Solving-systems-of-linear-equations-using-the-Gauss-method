import multipliers
def solution (syst:str)->tuple:
    multiplier_matrix=multipliers.matrix_init(syst)
    x=0
    y=0
    if multiplier_matrix[0][0]!=1:
        divider=multiplier_matrix[0][0]
        for i in range (len(multiplier_matrix[0])):
            multiplier_matrix[0][i]=multiplier_matrix[0][i]/divider
    if multiplier_matrix[1][0]!=0:
        divider_1=multiplier_matrix[1][0]
        for i in range(len(multiplier_matrix[1])):
            if divider_1>0:
                multiplier_matrix[1][i]=multiplier_matrix[0][i]*(-divider_1)+multiplier_matrix[1][i]
            elif divider_1<0:
                multiplier_matrix[1][i]=multiplier_matrix[0][i]*(-divider_1)+multiplier_matrix[1][i]
    y=multiplier_matrix[1][-1]/multiplier_matrix[1][1]
    if multiplier_matrix[0][1]*y>0:
        x=multiplier_matrix[0][2]-(multiplier_matrix[0][1]*y)
    elif multiplier_matrix[0][1]*y<0:
        x=multiplier_matrix[0][2]+(+multiplier_matrix[0][1]*y)
    return (x,y)
print(solution ('4x + y = 3 9x + 5y = 15'))


        
        


