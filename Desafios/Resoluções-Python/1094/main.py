n = int(input())

total_cobaia = 0
c = 0
r = 0
s = 0

for i in range(n):
    v = input()
    type_cobaia = v[-1:] 
    qtd_cobaia = v[:-2]
    qtd_cobaia = int(qtd_cobaia) 
    total_cobaia += qtd_cobaia

    if type_cobaia == "C":
        c += qtd_cobaia 
    if type_cobaia == "R":
        r += qtd_cobaia 
    if type_cobaia == "S":
        s += qtd_cobaia 

print("Total:",total_cobaia,"cobaias")
print("Total de coelhos:",c)
print("Total de ratos:",r)
print("Total de sapos:",s)
print("Percentual de coelhos:",format(round(((c/total_cobaia)*100),2),'.2f'),"%")
print("Percentual de ratos:",format(round(((r/total_cobaia)*100),2),'.2f'),"%")
print("Percentual de sapos:",format(round(((s/total_cobaia)*100),2),'.2f'),"%")
