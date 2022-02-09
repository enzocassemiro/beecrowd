r = []
while True:
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x>y:
        r.append('Decrescente')
    elif x==y:
        break
    else:
        r.append('Crescente')

for results in r:
    print(results)
