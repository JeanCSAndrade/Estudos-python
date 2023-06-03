import tkinter as tk 
from tkinter import*
from tkinter import messagebox
import os
import random as r

janela = tk.Tk()
janela.title('Seu relógio')
janela.geometry("600x320")
janela.maxsize(600, 200)
janela.minsize(600, 200)
janela.configure(background='#1d1d1d')
att_img = PhotoImage(file='refresh.png')
        
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
        cpf_tela.config(text='O CPF gerado é ' + cpf)
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
recarregar.config(image=att_img, width=30)
recarregar.pack(pady=10)
cpf()
get_saudacao()
janela.mainloop()