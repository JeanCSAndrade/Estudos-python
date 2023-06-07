perguntas = [{
    'Pergunta': 'Quanto é 2+2?',
    'Opções':['1','3','4','5'],
    'Resposta': '4'
},
{
    'Pergunta': 'Quanto é 5*5?',
    'Opções':['10','25','30','20'],
    'Resposta': '25'
},
{
    'Pergunta': 'Quanto é 10/2?',
    'Opções':['4','6','3','5'],
    'Resposta': '5'
}]

acertou = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    escolha = input('Escolha a opção correta: ')
    resposta = None
    qtd_opc = len(opcoes)

    if escolha.isdigit():
        resposta = int(escolha)
        if resposta is not None:
            if resposta >= 0 and resposta < qtd_opc:
                if opcoes[resposta] == pergunta['Resposta']:
                    print('Acertou 👍')
                    acertou +=1
                else:
                    print('Errou 👎')

print(f'Vc acertou {acertou} de {len(pergunta)}')