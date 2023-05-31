import os

Dados = []
print('Selecione uma opção')
opcao = input('[I]nserir [A]pagar [L]istar [S]air\n')

while opcao.lower() != 's':
    
    if opcao.lower() == 'i':
        os.system('cls')
        Dados.append(input('Digite o que deseja inserir:\n'))
    elif opcao.lower() == 'a':
        os.system('cls')
        index_str = input('Digite o que deseja apagar:\n')
        try:
            ix = int(index_str)
            del Dados[ix]
        except ValueError:
            print('Valor de index inválido')
        except IndexError:
            print('Valor não existe!')
        except Exception:
            print('Erro desconhecido!')
    elif opcao.lower() == 'l':
        os.system('cls')
        for index, lista in enumerate(Dados):
            print(index, lista)
    else:
        os.system('cls')
        print('Opção invalida!!!')
    opcao = input('[I]nserir [A]pagar [L]istar [S]air \n')
print('Obrigado por usar a lista')
