from PySimpleGUI import PySimpleGUI as sg
import string
import random

upper = random.choice(string.ascii_letters).upper()
upper2 = random.choice(string.ascii_letters).upper()
simbolos = random.choice(string.punctuation)
simbolos2 = random.choice(string.punctuation)
simbolos3 = random.choice(string.punctuation)
lower = random.choice(string.ascii_letters).lower()
lower2 = random.choice(string.ascii_letters).lower()
numeros = random.choice(string.digits)
numeros2 = random.choice(string.digits)
numeros3 = random.choice(string.digits)

Senha_Gerada = upper+upper2+simbolos+simbolos2+simbolos3+lower+lower2+numeros+numeros2+numeros3

#Layout
sg.theme('Dark')
layout = [
    
    [sg.Text('Senha Gerada'),sg.Output(key=Senha_Gerada,size=(12,0))],
    [sg.Button('Gerar',size=(5,1))]
    
    ]

#Janela
janela = sg.Window('Gerador de Senha', layout)
 
#Arquivo
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Gerar':
        print (Senha_Gerada)

        