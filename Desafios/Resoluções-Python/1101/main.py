n = 1
m = 1
l = []

while True:
    n, m = input().split()
    n = int(n)
    m = int(m)

    if n==0 or m==0 or n<0 or m<0:
        break
    if n > m:
        aux = m
        m = n
        n = aux
    l.append(n)
    l.append(m)

for i in range(0,len(l),2):
    r = ""
    s = 0
    for i in range(l[i],(l[i+1])+1):
        s+=i 
        r += str(i) + " "
    print(r,f"Sum={s}",sep='')
