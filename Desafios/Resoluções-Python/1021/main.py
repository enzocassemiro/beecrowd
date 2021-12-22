n = [100, 50, 20, 10, 5, 2]
m = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
v = round(float(input()),2)

print("NOTAS:")

for notas in n:
    qtdNotas = int(v/notas)
    v = v-(qtdNotas*notas)
    print(f"{qtdNotas} nota(s) de R$ {notas}.00")

v = round(v,2)

print("MOEDAS:")
for moedas in m:
    qtdMoedas=0

    if v<1 and v>0:
        qtdMoedas = int(v/moedas)
        v = round(v-(qtdMoedas*moedas),2)
        moedas = format(moedas,".2f")
        print(f"{qtdMoedas} moeda(s) de R$ {moedas}")

    elif v/moedas == v and not v==0.00:
        v = v-moedas
        qtdMoedas+=1
        moedas = format(moedas,".2f")
        print(f"{qtdMoedas} moeda(s) de R$ {moedas}")

    else:
        moedas = format(moedas,".2f")
        print(f"{qtdMoedas} moeda(s) de R$ {moedas}")
