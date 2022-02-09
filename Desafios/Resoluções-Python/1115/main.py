r = []
while True:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x==0 or y==0:
        break
    # 1 quadrante  x+ y+   
    if x>0 and y>0:
        r.append("primeiro")
    # 2 quadrante  x- y+   
    if x<0 and y>0:
        r.append("segundo")
    # 3 quadrante  x- y-   
    if x<0 and y<0:
        r.append("terceiro")
    # 4 quadrante  x+ y-   
    if x>0 and y<0:
        r.append("quarto")

for results in r:
    print(results)
