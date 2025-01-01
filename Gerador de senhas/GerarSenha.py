from customtkinter import *
from tkinter import Spinbox
import string
from random import sample


class GerarSenha():
    def __init__(self):
        self.home()
        self.frames()
        self.front()
        self.screen.mainloop()


    def home(self):
        self.screen = CTk()
        self.screen.geometry("325x350+475+200")
        self.screen.resizable(False, False)
        self.screen.title("Gerador de Senhas Aleatórias")
        self.screen.iconbitmap(r".\shield.ico")
        self.screen.config(background="#87CEEB")


    def frames(self):
        self.frameup = CTkFrame(self.screen, width=325, height=30, fg_color="#ADD8E6", corner_radius=0)
        self.frameup.grid(row=0, column=1, padx=1, pady=0)

        self.framedow = CTkFrame(self.screen, width=325, height=300, fg_color="#ADD8E6", corner_radius=0)
        self.framedow.grid(row=2, column=1, padx=1, pady=25)


    def gerar(self):
        Lmaiusculas = string.ascii_uppercase
        Lminusculas = string.ascii_lowercase
        numeral = string.digits
        pontuacao = string.punctuation
        
        password = ""

        if self.maiuscula.get():
            password += Lmaiusculas
        if self.minuscula.get():
            password += Lminusculas
        if self.numero.get():
            password += numeral
        if self.simbolo.get():
            password += pontuacao
        
        gerada = sample(password, int(self.caracter.get()))

        self.senha.delete(0, END)
        self.senha.insert(0, gerada)


    def copiar(self):
        self.framedow.clipboard_clear()
        self.framedow.clipboard_append(self.senha.get())  


    def front(self):
        textoHome = CTkLabel(self.frameup, text="GERADOR DE SENHAS", font=("Ivy 16 bold", 22), text_color="#0000FF", anchor=CENTER)
        textoHome.place(x=40, y=1)

        self.senha = CTkEntry(self.framedow, width=200, height=30)
        self.senha.place(x=10, y=50)
        copiar = CTkButton(self.framedow, width=70, height=30, text="Copiar", font=("Ivy 16 bold", 15), fg_color="#87CEEB", text_color="#0000FF",command=self.copiar)
        copiar.place(x=220, y=50)

        self.caracter = Spinbox(self.framedow, from_=1, to=50, wrap=True, width=3)
        self.caracter.place(x=10, y=10)

        nCaracter = CTkLabel(self.framedow, text="N° de caracteres", font=("Ivy 16 bold", 15), text_color="#0000FF", anchor=E)
        nCaracter.place(x=50, y=5)

        self.maiuscula = CTkCheckBox(self.framedow, width=100, height=22, text="ABC Letras Maiúsculas", font=("Ivy 16 bold", 15), text_color="#0000FF", corner_radius=20)
        self.maiuscula.place(x=10, y=100)

        self.minuscula = CTkCheckBox(self.framedow, width=100, height=22, text="abc Letras Minúsculas", font=("Ivy 16 bold", 15), text_color="#0000FF", corner_radius=20)
        self.minuscula.place(x=10, y=150)
        
        self.simbolo = CTkCheckBox(self.framedow, width=100, height=22, text="@#$ Símbolos", font=("Ivy 16 bold", 15), text_color="#0000FF", corner_radius=20)
        self.simbolo.place(x=10, y=200)
        
        self.numero = CTkCheckBox(self.framedow, width=100, height=22, text="123 Números", font=("Ivy 16 bold", 15), text_color="#0000FF", corner_radius=20)
        self.numero.place(x=10, y=250)

        self.btGerar = CTkButton(self.framedow, width=100, height=170, text="Gerar", text_color="#0000FF", font=("Ivy 16 bold", 18), command=self.gerar)
        self.btGerar.place(x=220, y=120)


GerarSenha()