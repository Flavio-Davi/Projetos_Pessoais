import customtkinter as ctk
import querie as qr

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('480x360+420+150')
        self.title('CRUD')
        self.iconbitmap('logo.ico')
        self.resizable(False, False)


    def frame_1(self):
        frame = ctk.CTkFrame(self)
        frame.place(relx=0.04, rely=0.02, relwidth=0.92, relheight=0.94)
        return frame


class Suporte(App):
    def __init__(self):
        super().__init__()
        self.screen = self.frame_1()
        self.chamado()
        self.nata()
        self.campinas()
        self.contrato()


    def chamado(self):
        ch = ctk.CTkEntry(self.screen, placeholder_text='Chamado', width=200)
        ch.place(x=110, y=110)


    def nata(self):
        button = ctk.CTkButton(self.screen, text='Nata')
        button.place(x=150, y=145)

    
    def campinas(self):
        button = ctk.CTkButton(self.screen, text='Campinas')
        button.place(x=150, y=180)


    def contrato(self):
        button = ctk.CTkOptionMenu(self.screen, values=qr.prod())
        button.place(x=150, y=230)


if __name__ == '__main__':
    app = Suporte()
    app.mainloop()
