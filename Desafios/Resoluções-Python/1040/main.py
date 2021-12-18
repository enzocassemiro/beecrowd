n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n1 = round(n1,1)
n2 = round(n2,1)
n3 = round(n3,1)
n4 = round(n4,1)

m = round((n1*0.2),1) + round((n2*0.3),1) + round((n3*0.4),1) + round((n4*0.1),1)

if m >=7.0:
    print("Media:",round(m,1))
    print("Aluno aprovado.")

if m < 5.0:
    print("Media:",round(m,1))
    print("Aluno reprovado.")

if 5.0 <= m <= 6.9:
    r = float(input())
    print("Media:",round(m,1))
    print("Aluno em exame.")
    print("Nota do exame:",round(r,1))
    mf = ((m + r)/2)
    if mf >= 5.0:
        print("Aluno aprovado.")
        print("Media final:",round(mf,1))
    else:
        print("Aluno reprovado.")
        print("Media final:",round(mf,1))
