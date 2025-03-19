import pandas as pd

class checkUser():
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.checkReturn = self.check()

        
    def check(self):
        user = False
        password = False
        data = pd.read_excel(r".\Data.xlsx")
        
        if self.user in data["USUARIO"].values:
            user = True
        if self.password in data["SENHA"].values:
            password = True

        return True if user==True and password==True else False
    

    def __bool__(self):
        return self.checkReturn
