import os

cpf_str = input('Digite os 9 primeiros digitos do seu cpf: \n')
cpf_str = cpf_str.replace('.','').replace('-','')
valor1 = 0
valor2 = 0
multiplica = 10
for index, i in enumerate(cpf_str[0:9]):
    valor1 = valor1 + (int(i)*multiplica)
    multiplica = multiplica-1 if index < 8 else multiplica+9

valor1 = valor1 * 10  
valor1 = valor1 % 11
digito1 = valor1 if valor1 <= 9 else 0
cpf = cpf_str + str(digito1)

for i in cpf:
    valor2 = valor2 + (int(i)*multiplica)
    multiplica -= 1

valor2 = valor2 * 10  
valor2 = valor2 % 11

digito2 = valor2 if valor1 <= 9 else 0
cpf = cpf + str(digito2)
print(f'O Primeiro digito do seu CPF é {digito1}, e o segundo é {digito2} e seu cpf é {cpf}')



teste git
