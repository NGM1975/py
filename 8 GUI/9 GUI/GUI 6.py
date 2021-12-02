from tkinter import *
from Persona import *
from tkinter import messagebox

raíz = Tk()
p = Persona
#creo una ventana raíz
raíz.title("Ventana para creación de objetos tipo usuarios")
raíz.geometry('450x400')
raíz.iconbitmap("Yo_ok.ico")
#-----------------------Entrys o texboxs-----------------------------------
txtNombre = Entry(raíz)
#creo un texbox y se lo pongo en el contenedor
txtNombre.grid(row=0,column=1,padx=10,pady=10)
#a partir de una grilla hubico la caja de texto en fila 0 columna 1
txtApellido = Entry(raíz)
txtApellido.grid(row=1,column=1,padx=10,pady=10)

txtDirección = Entry(raíz)
txtDirección.grid(row=2,column=1,padx=10,pady=10)

txtPass = Entry(raíz)
txtPass.grid(row=3,column=1,padx=10,pady=10)
txtPass.config(fg="blue")
#muestra letras tipeadas color violeta
txtPass.config(show='*')
#muestra * cuando tipeo sobre el textbox
#--------------------Texts----------------------------------------------------
txtObs = Text(raíz,width=20, height=6)
txtObs.grid(row=4,column=1,sticky="e",padx=5,pady=5)

#--------------Labels---------------------------------------------------------
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

#-----------------Función para crear una persona------------------
def crearPersona():
    global p
    p = Persona(txtNombre.get(),txtApellido.get(),txtDirección.get(),txtPass.get())
    respuesta = messagebox.askyesnocancel(title= "Consulta", message= '¿Confirma alta de Persona?')
    if respuesta == 1:
        messagebox.showinfo(title="Bienvenidos", message="Persona ingresada con éxito")
    else:
        messagebox.showinfo(title="Información...", message="Operación cancelada")
        #limpiarPantalla()
#-------------------------------------------------------------------
def salirAplicación():
    aux = messagebox.askokcancel(title='Confirmación', message="Confirma salir de la Aplicación")
    if aux == 1:
        raíz.destroy()
#-----------------------Función para mostrar persona---------------------------------------------
def mostrarPersona():
    global p
    print('**'*50) 
    messagebox.showinfo(title='Muestra de Persona', message='NOMBRE: '+ p.getNombre() +'\nAPELLIDO: '+ p.getApellido() +'\nDIRECCIÓN: '+ p.getDirección()) 
    print('**'*50)

butAlta = Button(raíz,text = 'Alta Persona',command = crearPersona)
butAlta.grid(column=0,row=5,padx=15,pady=15)

butMostrar = Button(raíz,text = 'Mostrar Persona',command = mostrarPersona)
butMostrar.grid(column=1,row=5,padx=15,pady=15)

butSalir = Button(raíz,text = 'Salir',command = salirAplicación)
butSalir.grid(column=2,row=5,padx=15,pady=15)

raíz.mainloop()