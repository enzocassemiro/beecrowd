r = []
while True:
    x, m = input().split()
    x = int(x)
    m = int(m)
    if x==0 and m==0:
        break
    r.append(x*m)

for v in r:
    print(v)
    