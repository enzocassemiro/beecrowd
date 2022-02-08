v1 = int(input())
r = []
s = 0

for i in range(1,v1+1):
    if i%2==0:
        r.append(i)

for results in r:
    print(f"{results}^2 =",results**2)
