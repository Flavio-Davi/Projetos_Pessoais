import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox
from validarUsuario import checkUser

screen = ctk.CTk()

class login():
    def __init__(self):
        self.screen = screen
        self.home()
        self.frameLogin()
        self.entryData()
        screen.mainloop()


    def home(self):
        screen.title("Login")
        screen.geometry("300x400+420+150")
        screen.resizable(False, False)

    
    def frameLogin(self):
        self.frame = ctk.CTkFrame(screen)
        self.frame.place(relx=0.06, rely=0.02, relwidth=0.87, relheight=0.94)
        img = ctk.CTkImage(Image.open("./avatar_login.png"), size=(80, 80))
        img_view = ctk.CTkLabel(self.frame, image=img, text="")
        img_view.place(relx=0.35, rely=0.01, relwidth=0.25, relheight=0.30)


    def showPassword(self):
        if self.password.cget("show") == "•":
            self.password.configure(show="")
        else:
            self.password.configure(show="•")


    def validateUser(self):
        user = self.user.get()
        password = self.password.get()
        validate = checkUser(user, password)
        
        if validate:
            CTkMessagebox(self.frame, title="Sucesso", icon="check", message=f"Bem vindo {user}", option_1="Continuar", option_2="Sair")
        else:
            CTkMessagebox(self.frame, title="Acesso Negado", icon="cancel",message="Usuário ou senha incorreto", option_1="Tentar novamente", option_2="Sair")


    def entryData(self):
        self.user = ctk.CTkEntry(self.frame, placeholder_text="Usuário")
        self.user.place(relx=0.12, rely=0.35, relwidth=0.77, relheight=0.08)
        self.password = ctk.CTkEntry(self.frame, placeholder_text="Senha", show="•")
        self.password.place(relx=0.12, rely=0.45, relwidth=0.77, relheight=0.08)
        
        buttonShowPassword = ctk.CTkCheckBox(self.frame, text="Mostrar senha", checkbox_width=13, checkbox_height=13, 
                                             width=15, height=15,corner_radius=25, border_width=1, command=self.showPassword)
        buttonShowPassword.place(relx=0.12, rely=0.55, relwidth=0.50, relheight=0.08)
        buttonGo = ctk.CTkButton(self.frame, text="Entrar", command=self.validateUser)
        buttonGo.place(relx=0.26, rely=0.77, relwidth=0.45, relheight=0.08)


login()
