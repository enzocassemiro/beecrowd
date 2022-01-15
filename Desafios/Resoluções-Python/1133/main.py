v1 = int(input())
v2 = int(input())

if v2<v1:
    aux = v1
    v1 = v2
    v2 = aux

for i in range(v1+1,v2):
    if i%5==2 or i%5==3:
        print(i)
