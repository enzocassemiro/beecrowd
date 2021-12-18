notas = [100,50,20,10,5,2,1]
vRecebido = int(input())
print(vRecebido)

for notas in notas:
    qtdNotas = int(vRecebido/notas)
    vRecebido = vRecebido-(qtdNotas*notas)
    print("{} nota(s) de R$ {},00".format(qtdNotas,notas))
