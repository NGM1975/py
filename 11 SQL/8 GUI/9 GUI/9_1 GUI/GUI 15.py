import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Usuarios import *
import sys

#Ejemplo de pantalla hecha objetos

class Aplicación:
    listaUsuarios =[] #variables de clase
    cant=0
    i=0
    def __init__(self):
        global ventana1
        self.ventana1=tk.Tk()
        self.ventana1.title("Ventana hecha con objetos")
        #self.ventana1.iconbitmap("Yo_ok.ico")
        self.ventana1.config(bg="Blue")
        self.ventana1.config(bd='10')
        self.ventana1.config(relief= GROOVE)
        self.labelframe1=ttk.LabelFrame(self.ventana1, text='Usuarios registrados: ')
        #frame 1 para sector login
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)
        self.framelogin()  #invoco al método login de la clase Aplicación
        self.labelframe2=ttk.LabelFrame(self.ventana1, text='Operaciones')
        #frame 2 para las funcionalidades de la aplicación
        self.labelframe2.grid(column=0,row=1,padx=5,pady=10)
        self.frameoperaciones()  #invoco al método operaciones de la clase Aplicación
        self.ventana1.mainloop()

    def framelogin(self):
        self.usu = StringVar()
        self.psw = StringVar()

        self.label1=ttk.Label(self.labelframe1, text="Nombre de Usuario: ")
        self.label1.grid(column=0, row=0,padx=4,pady=4)
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.usu) #asociación
        self.entry1.grid(column=1, row=0,padx=4,pady=4)
        self.label2=ttk.Label(self.labelframe1, text="PassWord: ")
        self.label2.grid(column=0, row=1,padx=4,pady=4)
        self.entry2=ttk.Entry(self.labelframe1, show="*", textvariable=self.psw)
        self.entry2.grid(column=1, row=1,padx=4,pady=4)
        self.botón1=ttk.Button(self.labelframe1, text='Salir de la Aplicación',command = self.fin)
        self.botón1.grid(column=1, row=2,padx=4,pady=4) 

    def frameoperaciones(self):
        self.botón2=ttk.Button(self.labelframe2, text='Agregar Usuario',command = self.ventanaNuevo)
        self.botón2.grid(column=0, row=0,padx=4,pady=4)
        self.botón3=ttk.Button(self.labelframe2, text='Siguiente Usuario',command = self.siguienteUsuario)
        self.botón3.grid(column=1, row=0,padx=4,pady=4)
        self.botón4=ttk.Button(self.labelframe2, text='Anterior Usuario',command = self.anteriorUsuario)
        self.botón4.grid(column=2, row=0,padx=4,pady=4)
    

    def ventanaNuevo(self):
        global ventana2
        ventana2 = Toplevel(self.ventana1)
        #self.ventana1.withdraw
        ventana2.title("Ventana Número Dos...")
        #ventana2.iconbitmap("Yo_Serio.ico")
        miFrame=Frame(ventana2,width=500,height=400)
        miFrame.config(bg="purple")
        miFrame.pack()
        #miFrame.grid(row=0,column=0)
        lbl= Label(miFrame,text = "Por favor ingrese usuario")
        lbl.grid(row=1,column=1,padx=10,pady=10)
        global txtDatos #para poder hacer referencia en salirForm
        txtDatos= Entry(miFrame)
        txtDatos.grid(row=2,column=1,padx=10,pady=10)
        global txtDatosNum #para poder hacer referencia en salirForm
        txtDatosNum= Entry(miFrame)
        txtDatosNum.grid(row=3,column=1,padx=10,pady=10)
        miBotón= Button(miFrame, text='Aceptar',command = self.salirForm)
        miBotón.grid(column=4, row=1,padx=10,pady=10)
        # Deshabilita todas las otras ventanas hasta que esta ventana sea destruida.
        ventana2.grab_set()
        # Indica que la ventana es de tipo modal, lo que significa que la ventana aparece al frente
        ventana2.transient(master=self.ventana1)        
    
        
    def salirForm(self):
        #global ventana2
        aux = messagebox.askyesno(title="Salir", message='¿Dar de alta al Usuario?')
        if aux ==1:
            U = Usuarios(txtDatos.get(),txtDatosNum.get())  #crear nuevo usuario
            self.listaUsuarios.append(U)  #agregar a la lista
            self.cant = self.cant+1
            ventana2.destroy()
            messagebox.showinfo(title='Descarga', message="Ventana 2 destruida")
            self.ventana1.configure(self.framelogin(state = 'normal'))

    def siguienteUsuario(self):
        if self.i<self.cant:
            self.usu.set(self.listaUsuarios[self.i].getNombre())
            self.psw.set(self.listaUsuarios[self.i].getPassw())
            self.i = self.i+1

    def anteriorUsuario(self):
        if self.i>0:
            self.i = self.i-1
            self.usu.set(self.listaUsuarios[self.i].getNombre())
            self.psw.set(self.listaUsuarios[self.i].getPassw())

    def fin(self):
        sys.exit(1)

aplicación1 = Aplicación()