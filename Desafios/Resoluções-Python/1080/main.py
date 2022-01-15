biggiest_value = 0 
for i in range(100):
    v = int(input())
    if v > biggiest_value:
        biggiest_value=v
        position = i

print(biggiest_value,"\n",position+1,sep='')
