import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class StockControlSystem:
    def __init__(self, window):
        self.window = window
        self.window.iconbitmap("img/logo.ico")
        self.window.title('Stock Control System | DPE')
        self.window.geometry('550x400') 
        self.window.resizable(width=False, height=False) 

        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=0)

        # Adicionar o retangulo no top
        self.top = tk.Frame(self.window, width=550 , height=50, bg='#016533', highlightthickness=1, highlightbackground='black')
        self.top.pack(side='top', pady=0.1) 

        # Adicionar nome title
        self.title = tk.Label(self.top, text='DTI SYSTEM', font=('Bevan', 20, 'bold'), bg='#016533', fg='white') 
        self.title.place(x=185, y=1) 

        # Adicionar ola
        self.ola = tk.Label(self.window, text="Olá mundo", font=('Bevan', 18, 'bold'), bg=None)
        self.ola.configure(borderwidth=0)
        self.ola.place(x=242, y=60)



window = tk.Tk()
app = StockControlSystem(window)
window.mainloop()

