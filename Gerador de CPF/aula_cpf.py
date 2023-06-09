import tkinter as tk 
from tkinter import*
import os
import random as r

janela = tk.Tk()
janela.title('Gerador de CPF')
janela.geometry("600x320")
janela.maxsize(600, 200)
janela.minsize(600, 200)
janela.configure(background='#1d1d1d')
        
def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)
def cpf():
        cpf_str = ''
        for i in range(9):
            cpf_str += str(r.randint(0,9))

        def calcula_cpf(cpf, multiplicador):
                valor = 0
                for i in cpf:
                    valor += int(i)*multiplicador
                    multiplicador -= 1
                valor *= 10
                valor %= 11
                valor = valor if valor <= 9 else 0
                return valor

        digito1 = calcula_cpf(cpf_str, 10)
        cpf_str += str(digito1)
        digito2 = calcula_cpf(cpf_str, 11)
        cpf = cpf_str+str(digito2)
        cpf_tela.config(text='O CPF gerado é ' + str(cpf)[:3]+'.'+str(cpf)[3:6]+'.'+str(cpf)[6:9]+'-'+str(cpf)[9:])
def refresh():
      cpf()
      get_saudacao()
tela = tk.Canvas(janela, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(janela, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 16))
saudacao.pack()
cpf_tela = Label(janela, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 14))
cpf_tela.pack(pady=2)
recarregar = Button(janela, command=refresh)
recarregar.config(text='Atualizar', bg='#FFFFFF', fg='#1d1d1d', font=('Montserrat', 16))
recarregar.pack(pady=10)
cpf()
get_saudacao()
janela.mainloop()