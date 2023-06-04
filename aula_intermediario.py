#Iniciando
def soma(*args):
    soma = 0
    for n in args:
        soma += n
        print('total e: ', soma, n)
    return soma

print(soma(1,2,3,4,5,6,7,8,9))
