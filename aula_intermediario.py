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
import datetime as dt
def saudacao(nome):
    hora = dt.datetime.now().time()
    hora = hora.hour
    time = ''
    if hora >= 5 and hora < 12:
        time = 'Bom dia'
    elif hora >= 12 and hora < 18:
        time = 'Boa tarde'
    else:
        time = 'Boa noite'

    def saudar():
        return f'{time}, {nome}'
    return saudar

comprimentar1 = saudacao('Jean')
comprimentar2 = saudacao('Brian')
print(comprimentar1())