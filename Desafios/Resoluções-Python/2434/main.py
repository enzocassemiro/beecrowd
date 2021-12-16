n, s = input().split()
m = s

for i in range(int(n)):
    j = input() 
    s = int(s) + int(j)
    if int(m)>s:
        m = s

print(m)
