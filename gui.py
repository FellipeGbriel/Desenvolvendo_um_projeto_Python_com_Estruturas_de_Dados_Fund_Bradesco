from tkinter import *

class Gui:

    def __init__(self, window):
        self.window = window
        self.window.wm_title("PySQL")

        # Configurações
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        # Variáveis
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels
        self.lblNome = Label(window, text="Nome")
        self.lblSobrenome = Label(window, text="Sobrenome")
        self.lblEmail = Label(window, text="Email")
        self.lblCPF = Label(window, text="CPF")

        # Entradas
        self.entNome = Entry(window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(window, textvariable=self.txtCPF, width=self.width_entry)

        # Lista + Scroll
        self.listClientes = Listbox(window, width=50)
        self.scrollClientes = Scrollbar(window)

        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        # Botões
        self.btnViewAll = Button(window, text="Ver todos")
        self.btnBuscar = Button(window, text="Buscar")
        self.btnInserir = Button(window, text="Inserir")
        self.btnUpdate = Button(window, text="Atualizar")
        self.btnDelete = Button(window, text="Deletar")
        self.btnClose = Button(window, text="Fechar", command=window.quit)

        # Layout (grid)
        self.lblNome.grid(row=0, column=0)
        self.lblSobrenome.grid(row=1, column=0)
        self.lblEmail.grid(row=2, column=0)
        self.lblCPF.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=6)
        self.scrollClientes.grid(row=0, column=3, rowspan=6)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDelete.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        
