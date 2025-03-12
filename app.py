import contacto as ct
import dbcontacto as dbet
import tkinter as tk

class App(tk.Tk):
    def __init__(self):  # Corrección aquí
        super().__init__()  # Corrección aquí
        self.config(width=700, height=500)
        self.title("Contacto")
        self.abct = dbet.dbcontacto()

        # Campos de entrada
        self.entry_id = tk.Entry(self)
        self.entry_id.pack()

        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        self.entry_direccion = tk.Entry(self)
        self.entry_direccion.pack()

        # Botón para guardar
        self.button_salvar = tk.Button(self, text="Guardar", command=self.button_salvar_clicked)
        self.button_salvar.pack()

    def button_salvar_clicked(self):
        ct_obj = ct.Contacto()
        ct_obj.setID(int(self.entry_id.get()))
        ct_obj.setNombre(self.entry_nombre.get())
        ct_obj.setDireccion(self.entry_direccion.get())

        self.abct.salvar(ct_obj)

# Ejecutar la aplicación
app = App()
app.mainloop()