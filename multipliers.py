def matrix_init (linear_equation):
    matrix = []
    transform = linear_equation.split(' ')
    unknown_x = []
    unknown_y = []
    right_part = []
    for i in range (len(transform)):
        if 'x' in transform[i]:
            if transform[i-1] == '-'and transform[i][0] == 'x':
                unknown_x.append(-1)
            elif transform[i][0] == 'x':
                unknown_x.append(1)
            elif transform[i-1] == '-':
                unknown_x.append(-(int(transform[i][:-1])))
            else:
                unknown_x.append(int(transform[i][:-1]))
                    
        elif 'y' in transform[i]:
            if transform[i-1] == '-' and transform[i][0] == 'y':
                unknown_y.append(-1)
            elif transform[i][0] == 'y':
                unknown_y.append(1)
            elif transform[i-1] == '-':
                unknown_y.append(-(int(transform[i][:-1])))   
            else:
                unknown_y.append(int(transform[i][:-1]))
        elif  transform[i] == '=':
            right_part.append(int(transform[i+1]))
            
    for i in range(len(unknown_x)):
       matrix.append([unknown_x[i], unknown_y[i], right_part[i]])
    return matrix
