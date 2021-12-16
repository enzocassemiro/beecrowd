n, m = input().split()

for i in range(int(m)):
    n = int(n)
    a = input()
    if a == 'clicou':
        n -= 1
    if a == 'fechou':
        n += 1

print(n)