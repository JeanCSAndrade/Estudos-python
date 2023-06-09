import random
import os
import time 
from getpass import getpass
Palavra_secreta = getpass('Qual a palavra').lower()
letras_digitadas = set()
# def selecionar_palavra():
#     return random.choice(palavras)

def desenhar_forca(tentativas):
    match tentativas:
        case 0:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |')
            print(' |')
            print(' |')
            print('_|___')
        case 1:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |      \ ')
            print(' |')
            print(' |')
            print('_|___') 
        case 2:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |      \|')
            print(' |')
            print(' |')
            print('_|___')
        case 3:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |      \|/')
            print(' |')
            print(' |')
            print('_|___')
        case 4:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |      \|/')
            print(' |       |')
            print(' |')
            print('_|___')
        case 5:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |      \|/')
            print(' |       |')
            print(' |      /')
            print('_|___')
        case 6:
            print('  _______ ')
            print(' |/      |')
            print(' |      (_)')
            print(' |      \|/')
            print(' |       |')
            print(' |      / \\')
            print('_|___')
# Função principal do jogo
def jogo_da_forca():
    palavra = Palavra_secreta
    letras_corretas = []
    tentativas = 0
    print('Bem-vindo ao Jogo da Forca!')
    print('A palavra possui', len(palavra), 'letras.')
    time.sleep(2)
    print('Vamos começar!!!!!!')
    time.sleep(1)
    while True:
        os.system('cls')
        desenhar_forca(tentativas)
        # Exibir as letras já descobertas e os espaços para as letras desconhecidas
        for letra in palavra:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('\n')

        if tentativas == 6:
            print('Você perdeu! A palavra correta era:', palavra)
            break

        if '_' not in ''.join([letra if letra in letras_corretas else '_' for letra in palavra]):
            print('Parabéns! Você acertou a palavra:', palavra)
            break
        print(f'Você já digitou as letras: ', end='')
        for _ in letras_digitadas:
            print(_, end='')
        letra = input('\nDigite uma letra: ').lower()
        if letra in letras_digitadas:
            print('Você já tentou essa letra. Tente outra vez.')
            time.sleep(1)
            continue
        else:
            letras_digitadas.add(letra)

        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra.')
            continue

        if letra in palavra:
            print('Letra correta!')
            letras_corretas.append(letra)
        else:
            print('Letra incorreta!')
            tentativas += 1

jogo_da_forca()
