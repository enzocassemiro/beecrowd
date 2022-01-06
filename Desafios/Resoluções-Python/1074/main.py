n = int(input())
r = []

for i in range(n):
    v = int(input())
    if v == 0:
        r.append("NULL")
    if v < 0 and ((v*-1)%2)!=0:
        r.append("ODD NEGATIVE")
    if v < 0 and ((v*-1)%2)==0:
        r.append("EVEN NEGATIVE")
    if v > 0 and ((v*-1)%2)!=0:
        r.append("ODD POSITIVE")
    if v > 0 and ((v*-1)%2)==0:
        r.append("EVEN POSITIVE")

for i in range(len(r)):
    print(r[i])
