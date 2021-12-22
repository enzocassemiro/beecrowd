c, q = input().split()
c = int(c)
q = int(q)
p = [4.00,4.50,5.00,2.00,1.50]

print("Total: R$",format(p[c-1]*q,'.2f'))
