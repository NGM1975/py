from tkinter import*
from tkinter import messagebox 
import sqlite3

#*****************************Funciones***********************^****
#^^^^^^^^^^^^Función de crear la BBDD si no existe^^^^^^^^^^^^^^^^^
def conexiónBD():
    miConexión = sqlite3.connect("BDUsuarios")
    miCursor = miConexión.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE USUARIOS (
            id integer primary key autoincrement,
            nombre varchar(50),
            apellido varchar(50),
            password varchar(20),
            dirección varchar(50),
            comentarios varchar(100))
            ''')
        messagebox.showinfo("BBDD","Base de Datos Creada con éxito...")
    except:
        messagebox.showwarning("BBDD","La Base de Datos ya fue creada...")

#++++++++++++++Función para solicitar la confirmación de usuario+++++++++++++++++
def SalirAplicación():
    resp = messagebox.askquestion("Salir","¿Desea salir de la Aplicación?")
    if resp == "yes":
        raíz.destroy()

#++++++++++Función para liumpiar todas las cajas de texto ENTRYS
def limpiarTexbox():
    varId.set("")
    varNombre.set("")
    varApellido.set("")
    varPass.set("")
    varDirección.set("")
    txtComentarios.delete("1.0",END) # Borra desde el primer caracter hasta el final

#+++++++Función para crear e INSERTAR un nuevo registro
def insertar():
    miConexión = sqlite3.connect("BDUsuarios")
    miCursor = miConexión.cursor()
# Este insert debería hacerlo con los "COMODINES ????" para evitar  inyección SQL
    if varNombre.get() != '':
        miCursor.execute("INSERT INTO USUARIOS VALUES (NULL,'" + varNombre.get() +
        "','" + varApellido.get() +
        "','" + varPass.get() +
        "','" + varDirección.get() +
        "','" + txtComentarios.get("1.0",END) + "')")

        miConexión.commit()
        messagebox.showinfo("BBDD","Registro insertado con Éxito!!!!")
        limpiarTexbox()
    else:
        messagebox.showwarning('BBDD','Verifique todos los campos obligatorios')

#++++++++++++++Función para leer desde BBDD*************
def seleccionar():
    miConexión=sqlite3.connect("BDUsuarios")
    miCursor=miConexión.cursor()
    # busqueda a partir del ID de usuario
    miCursor.execute("SELECT*FROM USUARIOS WHERE id = " +varId.get())
    datosConsulta = list(miCursor)
    #datosConsulta = miCursor.fetchall() 

    if len(datosConsulta) > 0:
        for usuario in datosConsulta:
            varId.set(usuario[0]),
            varNombre.set(usuario[1]),
            varApellido.set(usuario[2]),
            varPass.set(usuario[3]),
            varDirección.set(usuario[4]),
            txtComentarios.insert("1.0",usuario[5])
    else:
        messagebox.showwarning("BBDD","Usuario inexistente....")
    miConexión.commit()

#++++++++++++Función para hacer el update***************
#**************Función para pisar un registro+++++++++++++++
def actualizar():
    miConexión=sqlite3.connect("BDUsuarios")
    miCursor=miConexión.cursor()  
    miCursor.execute("UPDATE USUARIOS SET nombre = '" + varNombre.get()+
        "', apellido ='" + varApellido.get() +
        "', password ='" + varPass.get() +
        "', dirección ='" + varDirección.get() +
        "', comentarios ='" + txtComentarios.get("1.0",END) +
        "' WHERE id =" + varId.get())
    
    miConexión.commit()
    messagebox.showinfo("BBDD","Registro actualizado con Éxito!!!!")
    limpiarTexbox()

#*********--------------------+++++++++++++**************^^^^^^^^^^^^^^
raíz = Tk()
raíz.config(bg = "light blue")
barraMenu = Menu(raíz) #Asignamos la barra de menú a la raíz o ventana ppal
raíz.config(menu = barraMenu,width=300,height=300)  #configuramos la raíz con la barra
raíz.title("Ejemplo de Interfase Actualización...")
raíz.iconbitmap("Yo_ok.ico")  
# a continución incluimos los elementos de la barra de menús
bbddMenu = Menu(barraMenu,tearoff=0) #Sin líneas de separación entre menús
bbddMenu.add_command(label="Crear Base de Datos",command=conexiónBD)
bbddMenu.add_command(label="Salir",command=SalirAplicación) 

borrarMenu = Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Limpiar los TexBoxs",command=limpiarTexbox) 

crudMenu = Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Insertar",command=insertar) 
crudMenu.add_command(label="Seleccionar",command=seleccionar)
crudMenu.add_command(label="Actualizar",command=actualizar)
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

# Declaramos variables del tipo StringVar() para asociarlo a cada uno de los txtBox
varId = StringVar()
varId.set(0)
varNombre = StringVar()
varApellido = StringVar()
varPass = StringVar()
varDirección = StringVar()
varComentarios = StringVar()

# A cada ENTRY asociamos la variable correspondiente
txtId = Entry(miframe1,textvariable=varId)
txtId.grid(row=0,column=1,padx=10,pady=10)

txtNombre = Entry(miframe1,textvariable=varNombre)
txtNombre.grid(row=1,column=1,padx=10,pady=10)
txtNombre.config(fg="black", justify="left")

txtApellido = Entry(miframe1,textvariable=varApellido)
txtApellido.grid(row=2,column=1,padx=10,pady=10)
txtApellido.config(fg="black", justify="left")

txtPass = Entry(miframe1,textvariable=varPass)
txtPass.grid(row=3,column=1,padx=10,pady=10)
txtPass.config(fg="black",show="*")

txtDirección = Entry(miframe1,textvariable=varDirección)
txtDirección.grid(row=4,column=1,padx=10,pady=10)
txtDirección.config(fg="black", justify="left")

# Ahora la caja de texto
txtComentarios = Text(miframe1,width=25,height=5)
txtComentarios.grid(row=5,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miframe1,command=txtComentarios.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
txtComentarios.config(yscrollcommand=scrollVert.set, fg='white',bg='grey')

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

butCreate = Button(miframe2,text="Insertar",command=insertar)
butCreate.grid(row=1,column=0,sticky="e",padx=10,pady=10)

butUpdate = Button(miframe2,text="Actualizar",command=actualizar)
butUpdate.grid(row=1,column=2,sticky="e",padx=10,pady=10)

butRead = Button(miframe2,text="Seleccionar",command=seleccionar)
butRead.grid(row=1,column=1,sticky="e",padx=10,pady=10)

butDelete = Button(miframe2,text="Eliminar")
butDelete.grid(row=1,column=3,sticky="e",padx=10,pady=10)


raíz.mainloop()