n = int(input())
r = []
for i in range(n):
    v1, v2 , v3 = input().split()
    v1 = round(float(v1),1)
    v2 = round(float(v2),1)
    v3 = round(float(v3),1)
    m = round((((v1*0.2)+(v2*0.3)+(v3*0.5))),1)
    r.append(m)

for results in r:
    print(results)
