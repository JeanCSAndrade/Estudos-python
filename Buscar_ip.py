import socket 
import tkinter as tk 
from tkinter import*
import os
# import subprocess

tela = tk.Tk()
tela.geometry('600x300')
tela.minsize(500, 250)
tela.maxsize(600, 300)
tela.title('Meu IP')
tela.configure(background='#1d1d1d')

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)
def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    ipv4.config(text='O seu IP é: '+ip)
def refresh():
    get_ip()
    get_saudacao()
    # comandos = "ipconfig /flushdns", "ipconfig /release", "ipconfig /renew"
    # flush  = subprocess.run(*comandos, 
    #                      stdout=subprocess.PIPE, 
    #                      universal_newlines=True) 
tela = tk.Canvas(tela, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(tela, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 16))
saudacao.pack()
ipv4 = Label(tela, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 14))
ipv4.pack(pady=2)
recarregar = Button(tela, command=refresh)
recarregar.config(text='Atualizar', bg='#FFFFFF', fg='#1d1d1d', font=('Montserrat', 16))
recarregar.pack(pady=10)
get_ip()
get_saudacao()
tela.mainloop()