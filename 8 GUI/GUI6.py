from tkinter import * # PROBANDO
from Persona import *
from tkinter import messagebox

raíz = Tk()
p = Persona
#creo una ventana raíz
raíz.title("Ventana para creación de objetos tipo usuarios")
raíz.geometry('450x400')
raíz.iconbitmap("Yo_ok.ico")
txtNombre = Entry(raíz)
#creo un textbox y se lo pongo en el contenedor
txtNombre.grid(row=0,column=1,padx=10,pady=10)
#a partir de una grilla hubico la caja de texto en fila 0 columna 1
txtApellido = Entry(raíz)
txtApellido.grid(row=1,column=1,padx=10,pady=10)

txtDirección = Entry(raíz)
txtDirección.grid(row=2,column=1,padx=10,pady=10)

txtPass = Entry(raíz)
txtPass.grid(row=3,column=1,padx=10,pady=10)
txtPass.config(fg="violet")
#muestra letras tipeadas color violeta
txtPass.config(show='*')
#muestra * cuando tipeo sobre el textbox
#Creo los Lables correspondientes
lblNombre = Label(raíz,text='Nombre: ')
lblNombre.grid(row=0,column=0,sticky="e",padx=10,pady=10)
#sticky acomoda al..."este"'e'"oeste"'w' y así sucesivamente
 
lblApellido = Label(raíz,text='Apellido: ')
lblApellido.grid(row=1,column=0,sticky="e",padx=10,pady=10)

lblDirección = Label(raíz,text='Dirección: ')
lblDirección.grid(row=2,column=0,sticky="e",padx=10,pady=10)

lblPass = Label(raíz,text='Password: ')
lblPass.grid(row=3,column=0,sticky="e",padx=10,pady=10)

lblObs = Label(raíz,text='Obsertvaciones: ')
lblObs.grid(row=4,column=0,sticky="e",padx=10,pady=10)

txtObs = Text(raíz,width=20, height=6)
txtObs.grid(row=4,column=1,sticky="e",padx=5,pady=5)

#-----------------Función para crear una persona------------------
def crearPersona():
    global p
    p = Persona(txtNombre.get(),txtApellido.get(),txtDirección.get(),txtPass.get())
    print('Persona dada de alta exitosamente.....')
    messagebox.showinfo(title="Bienvenidos", message="Objeto creadocon éxito")
#-------------------------------------------------------------------
def salirAplicación():
    raíz.destroy()
#--------------------------------------------------------------------
def mostrarPersona():
    global p
    print('**'*50) 
    print('NOMBRE: ',p.getNombre(),'APELLIDO: ',p.getApellido(),'DIRECCIÓN: ',p.getDirección()) 
    print('**'*50)

butAlta = Button(raíz,text = 'Alta Persona',command = crearPersona)
butAlta.grid(column=0,row=5,padx=15,pady=15)

butMostrar = Button(raíz,text = 'Mostrar Persona',command = mostrarPersona)
butMostrar.grid(column=1,row=5,padx=15,pady=15)

butSalir = Button(raíz,text = 'Salir',command = salirAplicación)
butSalir.grid(column=2,row=5,padx=15,pady=15)

raíz.mainloop()