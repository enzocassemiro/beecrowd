f = float(input())

if 0 <= f <= 400:
    print("Novo salario:",format(f + (f * 0.15),'.2f'))
    print("Reajuste ganho:",format((f * 0.15),'.2f'))
    print("Em percentual: 15 %")
elif 400.01 <= f <= 800:
    print("Novo salario:",format(f + (f * 0.12),'.2f'))
    print("Reajuste ganho:",format((f * 0.12),'.2f'))
    print("Em percentual: 12 %")
elif 800.01 <= f <= 1200.00:
    print("Novo salario:",format(f + (f * 0.10),'.2f'))
    print("Reajuste ganho:",format((f * 0.10),'.2f'))
    print("Em percentual: 10 %")
elif 1200.01 <= f <= 2000:
    print("Novo salario:",format(f + (f * 0.07),'.2f'))
    print("Reajuste ganho:",format((f * 0.07),'.2f'))
    print("Em percentual: 7 %")
elif f > 2000:
    print("Novo salario:",format(f + (f * 0.04),'.2f'))
    print("Reajuste ganho:",format((f * 0.04),'.2f'))
    print("Em percentual: 4 %")
