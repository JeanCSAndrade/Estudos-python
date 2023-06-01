cpf_str = input('Digite o seu CPF: \n')
cpf_str = cpf_str.replace('.','')
valor = 0
multiplica = 10
for i in cpf_str[0:9]:
    valor = valor + (int(i)*multiplica)
    print(valor, i, multiplica, int(i)*multiplica)
    multiplica = multiplica-1

valor = valor * 10 
print(valor)   
valor = valor % 11

if valor > 9:
    print('resultado = 0')
else:
    print('resolvado é o valor da conta: ', valor)
    
    
    dasdasdas
