n = int(input())
a=0
g=0
d=0
while True:
    op = int(input())
    if op==1:
        a+=1
    if op==2:
        g+=1
    if op==3:
        d+=1
    if op==4:
        break

print("MUITO OBRIGADO",
f"\nAlcool: {a}",
f"\nGasolina: {g}",
f"\nDiesel: {d}",sep='')
