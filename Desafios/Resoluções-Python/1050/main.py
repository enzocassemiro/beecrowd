c_ddd = {"61":"Brasilia",
         "71":"Salvador",
         "11":"Sao Paulo",
         "21":"Rio de Janeiro",
         "32":"Juiz de Fora",
         "19":"Campinas",
         "27":"Vitoria",
         "31":"Belo Horizonte"}

ddd = str(input())

if c_ddd.get(ddd) != None: 
    r = print(c_ddd.get(ddd))
else:
    print("DDD nao cadastrado")
