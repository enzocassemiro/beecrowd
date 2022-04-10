first_test = str(input())
second_test = str(input())
third_test = str(input())

if first_test == 'vertebrado':
    
    if second_test == 'ave':
        if third_test == 'carnivoro':
            print('aguia')
        if third_test == 'onivoro':
            print('pomba')
    
    if second_test == 'mamifero':
        if third_test == 'onivoro':
            print('homem')
        if third_test == 'herbivoro':
            print('vaca')

if first_test == 'invertebrado':
    
    if second_test == 'inseto':
        if third_test == 'hematofago':
            print('pulga')
        if third_test == 'herbivoro':
            print('lagarta')
    
    if second_test == 'anelideo':
        if third_test == 'hematofago':
            print('sanguessuga')
        if third_test == 'onivoro':
            print('minhoca')
