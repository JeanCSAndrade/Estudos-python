import random as r

def calcula_cpf(cpf, multiplicador):
    valor = 0
    for i in cpf:
        valor += int(i)*multiplicador
        multiplicador -= 1
    valor *= 10
    valor %= 11
    valor = valor if valor <= 9 else 0
    return valor

cpf_str = ''
for i in range(9):
    cpf_str += str(r.randint(0,9))

digito1 = calcula_cpf(cpf_str, 10)
cpf_str += str(digito1)
digito2 = calcula_cpf(cpf_str, 11)
cpf = cpf_str+str(digito2)
print(f'O Primeiro digito do seu CPF é {digito1}, e o segundo é {digito2} e seu cpf é {cpf}')