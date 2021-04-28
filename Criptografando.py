from tkinter import *

import tkinter as tk
class FirstWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da mainWindow principal
        self.title('Criptografar um código')
        self.configure(background='#F3F3F3')
        self.geometry('1024x768')
        self.state('zoomed')
        
        def criptografia(x):

            #Alfabeto Criptografado FINAL
            alfabetoOriginal =      ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]   
            alfabetoCriptografado = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M",")","!","@","#","$","%","¨","&","*","("]

            #Transforma o texto somente em letras maiúsculas
            textoOriginal = x
            textoOriginal = textoOriginal.upper()
            textoCriptografado = ""

            textoTemporario = ""

            palavraTemp = ""
            letraIsolada = ""
            tamPalavraTemp = 0

            blocos = []
            blocosTemp = []
            blocoTemp = ""

            textoOriginal += " "

            textoEmbaralhado = ""

            #Embaralha os pares das letras de cada palavra
            for cadaLetra in textoOriginal:

                if cadaLetra in alfabetoOriginal:
                    palavraTemp += cadaLetra
                else:

                    tamPalavraTemp = len(palavraTemp)

                    if tamPalavraTemp%2 != 0:
                        letraIsolada = palavraTemp[tamPalavraTemp-1:]
                        palavraTemp = palavraTemp[0:-1]

                    while len(palavraTemp) > 0:
                        blocoTemp = palavraTemp[0:2]
                        blocosTemp += [blocoTemp]
                        blocoTemp = ""
                        palavraTemp = palavraTemp[2:]

                    while len(blocosTemp) > 0:
                        blocos += [blocosTemp[len(blocosTemp)-1]]
                        blocosTemp = blocosTemp[0:-1]

                        if len(blocosTemp) > 0:
                            blocos += [blocosTemp[0]]
                            blocosTemp = blocosTemp[1:]

                    blocos += [letraIsolada]
                    letraIsolada = ""

                    for s in blocos:
                        textoEmbaralhado += s

                    blocos = []

                    textoEmbaralhado += cadaLetra

            i = (len(textoEmbaralhado)-1)

            #Inverte o texto de trás pra frente
            while i >= 0:
                textoTemporario += textoEmbaralhado[i]
                i-=1

            #Altera as letras do alfabeto para o novo
            for letra in textoTemporario:
                if letra in alfabetoOriginal:
                    i = alfabetoOriginal.index(letra)
                    a = alfabetoCriptografado[i]
                else:
                    a = letra

                textoCriptografado += a

            return textoCriptografado    

        def bt_onclick():
            lb2.delete('1.0', END)
            lb2.insert (INSERT,criptografia(ed.get(1.0,END)))

        lb = Label(self, text="Insira o texto para ser criptografado")
        lb.config(font=("Arial", 20))
        lb.pack(side=TOP)
        self["bg"] = '#F3F3F3'

        ed = Text(self, width=120, height = 20)
        ed.config(font=('Arial', 12), wrap = WORD)
        ed.pack(anchor = CENTER)

        bt = Button(self, width=64, text="Criptografar", command=bt_onclick)
        bt.pack(anchor = CENTER)

        lb2 = Text(self, width = 120, height = 20)
        lb2.config(font=('Arial', 12))
        lb2.pack(anchor=CENTER)


class SecondWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da mainWindow principal
        self.title('Descriptografar um código')
        self.configure(background='#F3F3F3')
        self.geometry('1024x768')
        self.state('zoomed')  
        
        def criptografia(x):

            #Alfabeto Criptografado FINAL
            alfabetoOriginal =      ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]   
            alfabetoCriptografado = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M",")","!","@","#","$","%","¨","&","*","("]

            #Transforma o texto somente em letras maiúsculas
            textoOriginal = x
            textoOriginal = textoOriginal.upper()
            textoCriptografado = ""

            textoTemporario = ""
            textoInvertido = ""

            palavraTemp = ""
            letraIsolada = ""
            tamPalavraTemp = 0

            blocos = []
            blocosTemp = []
            blocoTemp = ""

            listaTemp1 = []
            listaTemp2 = []
            listaTemp1C = []

            textoEmbaralhado = ""

            #Altera as letras do alfabeto para o novo
            for letra in textoOriginal:
                if letra in alfabetoOriginal:
                    i = alfabetoOriginal.index(letra)
                    a = alfabetoCriptografado[i]
                else:
                    a = letra

                textoInvertido += a

            #Inverte o texto de trás pra frente
            i = (len(textoInvertido)-1)

            while i >= 0:
                textoTemporario += textoInvertido[i]
                i-=1

            textoTemporario += " "

            #Embaralha os pares das letras de cada palavra
            for cadaLetra in textoTemporario:

                if cadaLetra in alfabetoOriginal:
                    palavraTemp += cadaLetra
                else:       
                    tamPalavraTemp = len(palavraTemp)

                    if tamPalavraTemp%2 != 0:
                        letraIsolada = palavraTemp[tamPalavraTemp-1:]
                        palavraTemp = palavraTemp[0:-1]

                    while len(palavraTemp) > 0:
                        blocoTemp = palavraTemp[0:2]
                        blocosTemp += [blocoTemp]
                        blocoTemp = ""
                        palavraTemp = palavraTemp[2:]

                    while len(blocosTemp) > 0:
                        listaTemp1 += blocosTemp[0:1]
                        blocosTemp = blocosTemp[1:]
                        if len(blocosTemp) > 0:
                            listaTemp2 += blocosTemp[0:1]
                            blocosTemp = blocosTemp[1:]

                    while len(listaTemp1) > 0:
                        listaTemp1C += listaTemp1[len(listaTemp1)-1:]
                        listaTemp1 = listaTemp1[0:-1]

                    blocos = listaTemp2 + listaTemp1C

                    listaTemp1 = []
                    listaTemp2 = []
                    listaTemp1C = []

                    blocos += [letraIsolada]
                    letraIsolada = ""

                    for s in blocos:
                        textoEmbaralhado += s

                    blocos = []

                    textoEmbaralhado += cadaLetra


            return(textoEmbaralhado)  

        def bt_onclick():
            lb2.delete('1.0', END)
            lb2.insert (INSERT,criptografia(ed.get(1.0,END)))

        lb = Label(self, text="Insira o texto para ser descriptografado")
        lb.config(font=("Arial", 20))
        lb.pack(side=TOP)
        self["bg"] = '#F3F3F3'

        ed = Text(self, width=120, height = 20)
        ed.config(font=('Arial', 12), wrap = WORD)
        ed.pack(anchor = CENTER)

        bt = Button(self, width=64, text="Descriptografar", command=bt_onclick)
        bt.pack(anchor = CENTER)

        lb2 = Text(self, width = 120, height = 20)
        lb2.config(font=('Arial', 12))
        lb2.pack(anchor=CENTER)
    
class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da mainWindow principal
        self.master.title('Criptografador')
        self.master.geometry('480x240')
       
        self.configure(borderwidth=4)
        self.configure(background='#F3F3F3')
        
        self.label = Label(self, text="O que você deseja fazer?")
        self.label.config(font=('Verdana',25))
        self.label.pack(side='top', expand=False)

        for name in ("Criptografar um código", "Descriptografar um código"):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(anchor="center", expand=False)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('Criptografar um código'):
            window = FirstWindow()
        if btn_name.endswith('Descriptografar um código'):
            window = SecondWindow()
        
        window.mainloop()


#(WidthxHeight+TopLeft+TopRight
#512x384+512,384
if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop() 
