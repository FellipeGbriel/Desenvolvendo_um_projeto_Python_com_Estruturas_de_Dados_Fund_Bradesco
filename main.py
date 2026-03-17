from tkinter import *
from gui import Gui
import backend

class Main:

    def __init__(self, window):
        self.gui = Gui(window)

        # Item selecionado
        self.selected_tuple = None

        # Bind da lista
        self.gui.listClientes.bind('<<ListboxSelect>>', self.get_selected_row)

        # Ligando botões às funções
        self.gui.btnViewAll.configure(command=self.view_command)
        self.gui.btnBuscar.configure(command=self.search_command)
        self.gui.btnInserir.configure(command=self.insert_command)
        self.gui.btnUpdate.configure(command=self.update_command)
        self.gui.btnDelete.configure(command=self.delete_command)

        backend.initDB()

    # -------------------------
    # Funções
    # -------------------------

    def get_selected_row(self, event):
        try:
            index = self.gui.listClientes.curselection()[0]
            self.selected_tuple = self.gui.listClientes.get(index)

            # Preenche os campos
            self.gui.entNome.delete(0, END)
            self.gui.entNome.insert(END, self.selected_tuple[1])

            self.gui.entSobrenome.delete(0, END)
            self.gui.entSobrenome.insert(END, self.selected_tuple[2])

            self.gui.entEmail.delete(0, END)
            self.gui.entEmail.insert(END, self.selected_tuple[3])

            self.gui.entCPF.delete(0, END)
            self.gui.entCPF.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.gui.listClientes.delete(0, END)
        for row in backend.view():
            self.gui.listClientes.insert(END, row)

    def search_command(self):
        self.gui.listClientes.delete(0, END)
        for row in backend.search(
            self.gui.txtNome.get(),
            self.gui.txtSobrenome.get(),
            self.gui.txtEmail.get(),
            self.gui.txtCPF.get()
        ):
            self.gui.listClientes.insert(END, row)

    def insert_command(self):
        backend.insert(
            self.gui.txtNome.get(),
            self.gui.txtSobrenome.get(),
            self.gui.txtEmail.get(),
            self.gui.txtCPF.get()
        )
        self.view_command()

    def delete_command(self):
        if self.selected_tuple:
            backend.delete(self.selected_tuple[0])
            self.view_command()

    def update_command(self):
        if self.selected_tuple:
            backend.update(
                self.selected_tuple[0],
                self.gui.txtNome.get(),
                self.gui.txtSobrenome.get(),
                self.gui.txtEmail.get(),
                self.gui.txtCPF.get()
            )
            self.view_command()


# -------------------------
# Inicialização
# -------------------------

if __name__ == "__main__":
    window = Tk()
    app = Main(window)
    window.mainloop()