from tkinter import*
from tkinter import messagebox 
import sqlite3

raíz = Tk()

barraMenu = Menu(raíz) #Asignamos la barra de menú a la raíz o ventana ppal
raíz.config(menu = barraMenu,width=300,height=300)  #configuramos la raíz con la barra
raíz.title("Ejemplo de interfase CRUD")
#raíz.iconbitmap("Yo_ok.ico")  
# a continución incluimos los elementos de la barra de menús
bbddMenu = Menu(barraMenu,tearoff=0) #Sin líneas de separación entre menús
bbddMenu.add_command(label="Crear Base de Datos")
bbddMenu.add_command(label="Salir")

borrarMenu = Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Limpiar los TexBoxs")

crudMenu = Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Insertar")
crudMenu.add_command(label="Seleccionar")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Eliminar")

AyudaMenu = Menu(barraMenu,tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de....")

#Ahora hay que asignar estos 4 elementos BBDDMENU, BORRARMENU, CRUDMENU Y AYUDAMENU
# A la barra de elementos del menú barraMenu 

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)  
barraMenu.add_cascade(label="Borrar Campos",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=AyudaMenu)

#+++++++++++++++Ahora crear los labels con los texboxs+++++++++++++++
#******************en dos Frames*************************************
miframe1 = Frame(raíz)
miframe1.pack()

#varId = IntVar()
#varNombre = StringVar()
#varApellido = StringVar()
#varPass = StringVar()
#varDirección = StringVar()
#varObs = StringVar()

txtId = Entry(miframe1) #,textvariable=varId)
txtId.grid(row=0,column=1,padx=10,pady=10)

txtNombre = Entry(miframe1) #,textvariable=varNombre)
txtNombre.grid(row=1,column=1,padx=10,pady=10)
txtNombre.config(fg="blue", justify="center")

txtApellido = Entry(miframe1) #,textvariable=varApellido)
txtApellido.grid(row=2,column=1,padx=10,pady=10)
txtApellido.config(fg="blue", justify="left")

txtPass = Entry(miframe1) #,textvariable=varPass)
txtPass.grid(row=3,column=1,padx=10,pady=10)
txtPass.config(show="*")

txtDirección = Entry(miframe1) #,textvariable=varDirección)
txtDirección.grid(row=4,column=1,padx=10,pady=10)
txtDirección.config(fg="blue", justify="left")

# Ahora la caja de texto
txtComentarios = Text(miframe1,width=28,height=5)
txtComentarios.grid(row=5,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miframe1,command=txtComentarios.yview)
# OJO barra desplazamiento vertical yview
scrollVert.grid(row=5,column=2) #,sticky="nsew")
# Ubicación de la barra desplazamiento, es un widget diferente
txtComentarios.config(yscrollcommand=scrollVert.set)
# Asignación del scrool al text

#**********************Ahora los Labels*****************************

labelId = Label(miframe1,text="ID: ")
labelId.grid(row=0,column=0,sticky="e",padx=10,pady=10)

labelNombre = Label(miframe1,text="NOMBRE: ")
labelNombre.grid(row=1,column=0,sticky="e",padx=10,pady=10)

labelApellido = Label(miframe1,text="APELLIDO: ")
labelApellido.grid(row=2,column=0,sticky="e",padx=10,pady=10)

labelPass = Label(miframe1,text="PASSWORD: ")
labelPass.grid(row=3,column=0,sticky="e",padx=10,pady=10)

labelDirección = Label(miframe1,text="DIRECCIÓN: ")
labelDirección.grid(row=4,column=0,sticky="e",padx=10,pady=10)

labelComentarios = Label(miframe1,text="COMENTARIOS: ")
labelComentarios.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#***********************Ahora los Botones***********************

#def mostrarPrimerRegistro():
#    miConexión = sqlite3.connect("MiBDCRUD")
#    miPuntero = miConexión.cursor()
#    miPuntero.execute("SELECT * FROM USUARIOS WHERE id = 1")
#    listaUsuarios = list(miPuntero)
#    print(listaUsuarios)
#    varId.set(listaUsuarios[0][0])
#    varNombre.set(listaUsuarios[0][1])
#    varApellido.set(listaUsuarios[0][2])
#    varPass.set(listaUsuarios[0][3])
#    varDirección.set(listaUsuarios[0][4])
#    varObs.set(listaUsuarios[0][5])

#a cada Entry asociamos la variable corresapondiente
#txtId = Entry(miframe1,textvariable=varId)

miframe2 = Frame(raíz)
miframe2.pack()
#miframe2.config(bg = "yellow")

butCreate = Button(miframe2,text="Insertar")
butCreate.grid(row=1,column=0,sticky="e",padx=10,pady=10)

butUpdate = Button(miframe2,text="Actualizar")
butUpdate.grid(row=1,column=2,sticky="e",padx=10,pady=10)

butRead = Button(miframe2,text="Seleccionar")
butRead.grid(row=1,column=1,sticky="e",padx=10,pady=10)

butDelete = Button(miframe2,text="Eliminar")
butDelete.grid(row=1,column=3,sticky="e",padx=10,pady=10)


raíz.mainloop()