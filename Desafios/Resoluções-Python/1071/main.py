v1 = int(input())
v2 = int(input())
r = []
s = 0

if v1>v2:
    aux = v2
    v2 = v1
    v1 = aux

for i in range(v1,v2):
    if i%2!=0:
        r.append(i)

for results in r:
    s += results

print(s)
