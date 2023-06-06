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


for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print('Opções:')
    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i}) {opcoes}') 
    resposta = input('Digite sua resposta: ')

    if resposta == pergunta['Resposta']:
        print('Resposta correta')
    else:
        print('Resposta errada')
    