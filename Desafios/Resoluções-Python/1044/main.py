a,b = input().split()
a = int(a)
b = int(b)

if b > a:
    aux = a
    a = b 
    b = aux

if a%b == 0:
    print('Sao Multiplos')

else:
    print('Nao sao Multiplos')
