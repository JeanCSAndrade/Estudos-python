# Criando funções com varios argumentos
# import random as r
# def mult(*args):
#     multiplicados = 1
#     for n in args:
#         multiplicados *= n
#         print(f'numero é {n} total e: {multiplicados} {par(multiplicados)}')
#     return multiplicados

# def par(*args):
#     for n in args:
#         par = n % 2 ==0
#         if par:
#             resultado = 'E é um numero par'
#             return resultado
#         resultado = 'E é um numero impar'
#         return resultado
         
# valores = []
# for _ in range(9):
#     valores.append(r.randint(1, 9))
# multiplicados = mult(*valores)


# criando funções com adiamento de chamada
# import datetime as dt
# def saudacao(nome):
#     hora = dt.datetime.now().time()
#     hora = hora.hour
#     time = ''
#     if hora >= 5 and hora < 12:
#         time = 'Bom dia'
#     elif hora >= 12 and hora < 18:
#         time = 'Boa tarde'
#     else:
#         time = 'Boa noite'

#     def saudar():
#         return f'{time}, {nome}'
#     return saudar

# comprimentar1 = saudacao('Jean')
# comprimentar2 = saudacao('Brian')
# print(comprimentar1())

# exercicio de funções com multiplas funções e adiamento de chamada
# def multiplicador(muliplicador):
#     def calcular(numero):
#         return numero * muliplicador 
#     return calcular

# dobro = multiplicador(2)
# triplo = multiplicador(3)
# quadruplo = multiplicador(4)

# print(dobro(5))
# print(triplo(5))
# print(quadruplo(5))


#inciiando estudos de dicionarios

# dict1 = {'Nome': 'Jean', 'Sobrenome': 'Andrade'}
# dict1['Idade'] = 32

# for tupla in dict1.items():
#     for itens in tupla:
#         print(itens)

valores = [[1,2,3,4,2,3,1,4],
           [1,2,3,4,5,6,7,8],
           [3,2,1,5,7,3,2,1]]

def encontra_duplicado(listas):
    numero_chegado = set()
    default_duplicado = -1
    for numero in listas:
        if numero in numero_chegado:
            default_duplicado = numero
            break
        numero_chegado.add(numero)
    return default_duplicado

for lista in valores:
    print(lista, encontra_duplicado(lista))