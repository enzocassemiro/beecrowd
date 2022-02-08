count = 0
r = 0
j=7
for i in range(15):
    print('I=',r+1,' J=',j,sep='')
    
    if count == 0:
        first_j = j
    
    count += 1
    j -= 1
    if count == 3:
        r += 2
        count = 0
        j = first_j + 2
