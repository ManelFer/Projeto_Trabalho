import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

class StockControlSystem:
    def __init__(self, window):
        self.window = window
        self.window.iconbitmap("img/logo.ico")
        self.window.title('Stock Control System | DPE')
        self.window.geometry('550x200') 
        self.window.resizable(width=False, height=False) 

        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=0)

        # Adicionar o retangulo no top
        self.top = tk.Frame(self.window, width=550 , height=50, bg='#016533', highlightthickness=1, highlightbackground='black')
        self.top.pack(side='top', pady=0.1) 

        # Adicionar nome title
        self.title = tk.Label(self.top, text='DTI SYSTEM', font=('Bevan', 20, 'bold'), bg='#016533', fg='white') 
        self.title.place(x=185, y=1) 

        # Adicionar Login
        self.Login = tk.Label(self.window, text="Login", font=('Bevan', 18, 'bold'), bg=None)
        self.Login.configure(borderwidth=0)
        self.Login.place(x=242, y=60)

        # Adicionar campo de usuario
        icon = tk.PhotoImage(file="img/user.png") 
        self.UserLabel = tk.Label(self.window, text="Name: ", font=('Bevan', 16, 'bold'), bg=None)
        self.UserLabel.place(x=154, y=100)
        self.entry_username = tk.Entry(self.window, width=26, highlightthickness=1, highlightbackground='black')
        self.entry_username.place(x=240, y=105)
            # Adicionar o icon
        self.IconLabel = tk.Label(self.window, image=icon, bg='white', width=11, height=11)
        self.IconLabel.image = icon
        self.IconLabel.place(x=380, y=107)

        # Adicionar campo de senha
        icon = tk.PhotoImage(file="img/cadeado.png")
        self.PassLabel = tk.Label(self.window, text="Senha: ", font=('Bevan', 16, 'bold'), bg=None)
        self.PassLabel.place(x=154, y=133)
        self.entry_password = tk.Entry(self.window, width=26, highlightthickness=1, highlightbackground='black', show="*")
        self.entry_password.place(x=240, y=138)
            # Adicionar o icon
        self.IconPass = tk.Label(self.window, image=icon, bg='white', width=11, height=11)
        self.IconPass.image = icon
        self.IconPass.place(x=380, y=140)
        
        # Adicionar botão Login
        self.LoginButton = tk.Button(self.window, text="Login", font=("Bevan", 7, 'bold'), width=7, bg='#016533', fg='white', highlightthickness=1, highlightbackground='black', command=self.login)
        self.LoginButton.place(x=405, y=138)

    def login(self):
        UserLogin = self.entry_username.get()
        PassLogin = self.entry_password.get()
        database.cursor.execute("""
                                    SELECT * FROM Users
                                    WHERE (User = ? and Password = ?)
                                    """, (UserLogin, PassLogin))
        print("Selecionou")
        VerifyLogin = database.cursor.fetchone()
        # ação para entrar em outra janela
        try:
            if VerifyLogin:
                messagebox.showinfo(title="Aviso de Login", message="Acesso Confirmado")
                window.after(100, window.destroy)
                import perfil
                perfil.main()
            else:
                messagebox.showinfo(title="Aviso Login", message="Acesso Negado")
        except:
            pass

window = tk.Tk()
app = StockControlSystem(window)
window.mainloop()
