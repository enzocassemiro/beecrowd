p = 0
im = 0
np = 0
nn = 0

for i in range(5):
    v = int(input())
    if v%2==0:
        p += 1
    if v%2!=0:
        im += 1
    if v>0:
        np += 1
    if v<0:
        nn += 1

print(f"{p} valor(es) par(es)\n",
      f"{im} valor(es) impar(es)\n",
      f"{np} valor(es) positivo(s)\n",
      f"{nn} valor(es) negativo(s)",sep='')
