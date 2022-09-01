from random import shuffle
from itertools import permutations

def quadradoslatino(N):
    tudo = possibilidades(N)
    for b in range(tudo):
        auxiliar = []
        for _ in range(1,N+1):
            auxiliar.append(_)
        shuffle(auxiliar)
        quadrofeito = []
        quadrofeito.append(auxiliar)

        permutacao = permutations(auxiliar)
        for _ in permutacao:
            _ = list(_)
            if analise(quadrofeito, _) == True:
                quadrofeito.append(_)

        for _ in quadrofeito:
                print(_)
        print("\n")


def analise(p,q):
    for w in range(len(p)):    
        for z in range(len(p[0])):
            if p[w][z] == q[z]:
                return False
    return True

def fat(e):
    prod = 1 
    for x in range(1,e+1):
        prod *= x
    return prod

def possibilidades(a):
    return (a-1)*fat(a)

    

Tamanho = int(input('Qual o tamanho do seu quadro? '))
quadradoslatino(Tamanho) 
print((f'As outras possibilidades são:'),possibilidades(Tamanho),"possibilidades")