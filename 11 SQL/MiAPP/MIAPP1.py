from tkinter import *
from tkinter import messagebox
import sqlite3


def conexionBD():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE ASISTENTES (
            idasist integer primary key autoincrement,
            usuario varchar(20) NOT NULL,
            nombre varchar(40) NOT NULL,
            apellido varchar(40) NOT NULL,
            password varchar(20) NOT NULL)
            CREATE TABLE FAMILIAS (
            idfamily integer primary key autoincrement,
            apellido_family varchar(40) NOT NULL)
            CREATE TABLE ASIST_X_FAMILIAS (
            idasf integer primary key NOT NULL,
            idasist integer foreign key,
            idasist2 integer foreign key,
            idfamily integer foreign key,
            fecha date NOT NULL,
            comentarios varchar(100))
            ''')
        messagebox.showinfo("BBDD", "Base de Datos Creada con exito...")
    except:
        messagebox.showwarning("BBDD", "La Base de Datos ya fue creada...")


def SalirAplicacion():
    resp = messagebox.askquestion("Salir", "¿Desea salir de la Aplicacion?")
    if resp == "yes":
        raiz.destroy()


def limpiarTexbox():
    varId.set("")
    varNombre.set("")
    varApellido.set("")
    varNombre2.set("")
    varApellido2.set("")
    varFamilia.set("")
    varFecha.set("")
    txtComentarios.delete("1.0", END)


def conexionBD():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE ASISTENTES (
            idasist integer primary key autoincrement,
            nombre varchar(40) ,
            apellido varchar(40) )
            ''')
        messagebox.showinfo("BBDD", "Base de Datos Creada con exito...")
    except:
        messagebox.showwarning("BBDD", "La Base de Datos ya fue creada...")


def insertar():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    if varIdaxf.get() != '':
        miCursor.execute("INSERT INTO ASIST_X_FAMILIAS VALUES ('" + varIdaxf.get() +
                         "','" + varIdasist.get() +
                         "','" + varIdfamily.get() +
                         "','" + varFecha.get() +
                         "','" + txtComentarios.get("1.0", END) + "')")
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito!!!!")
        limpiarTexbox()
    else:
        messagebox.showwarning(
            'BBDD', 'Verifique todos los campos obligatorios')


def insertarFamilia():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    if varFamily.get() != '':
        miCursor.execute(
            "INSERT INTO FAMILIAS VALUES (NULL,'" + varFamily.get() + "')")
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito!!!!")
        limpiarTexbox()
    else:
        messagebox.showwarning(
            'BBDD', 'Verifique todos los campos obligatorios')


def seleccionar():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    miCursor.execute(
        "SELECT*FROM ASISTENTES AS JOIN ASIST_X_FAMILIAS AF ON AS.idasist = AF.idasist JOIN FAMILIAS F ON AF.idfamily = F.idfamily WHERE idaxf = " + varIdaxf.get())

    datosConsulta = list(miCursor)

    if len(datosConsulta) > 0:
        for asistencia in datosConsulta:
            varIdasist.set(asistencia[0]),
            varNombre.set(asistencia[1]),
            varApellido.set(asistencia[2]),
            varIdfamily.set(asistencia[3]),
            varFamily.set(asistencia[4]),
            varFecha.set(asistencia[5]),
            txtComentarios.insert("1.0", asistencia[6])
    else:
        messagebox.showwarning("BBDD", "Asist_x_Familias inexistente....")
    miConexion.commit()


def actualizar():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    miCursor.execute("UPDATE ASIST_X_FAMILIAS SET idasist = '" + varIdasist.get() +
                     "', idfamily ='" + varIdfamily.get() +
                     "', fecha ='" + varFecha.get() +
                     "', comentarios ='" + txtComentarios.get("1.0", END) +
                     "' WHERE idaxf =" + varIdaxf.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con exito!!!!")
    limpiarTexbox1()


def eliminar():
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()
    miCursor.execute(
        "DELETE FROM ASIST_X_FAMILIAS WHERE idaxf = " + varIdaxf.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro eliminado con exito!!!!")
    limpiarTexbox1()


def ventanaNuevo():

    global Ventana2
    Ventana2 = Toplevel(Ventana1)
    Ventana2.title("REGISTRO DE ASISTENTE")
    #global barraMenu
    barraMenu = Menu(Ventana2)
    Ventana2.config(menu=barraMenu, width=300, height=300)
    Ventana2.geometry('350x300+300+200')
    #global bbddMenu
    bbddMenu = Menu(barraMenu, tearoff=0)
    bbddMenu.add_command(label="Crear Base de Datos", command=conexionBD)

    miframe1 = Frame(Ventana2, width=500, height=400)
    miframe1.config(bg="light blue")
    miframe1.config(bd=15)
    miframe1.config(relief=GROOVE)
    miframe1.pack()
    # miframe1.grid(row=0,column=0)

    global varNombre
    varNombre = StringVar()
    global varApellido
    varApellido = StringVar()

    txtNombre = Entry(miframe1, textvariable=varNombre)
    txtNombre.grid(row=1, column=1, padx=10, pady=10)
    txtNombre.config(fg="black", justify="left")

    txtApellido = Entry(miframe1, textvariable=varApellido)
    txtApellido.grid(row=2, column=1, padx=10, pady=10)
    txtApellido.config(fg="black", justify="left")

    labelNombre = Label(miframe1, text="NOMBRE: ")
    labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    labelApellido = Label(miframe1, text="APELLIDO: ")
    labelApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    lbl = Label(miframe1, text="Ingrese datos")
    lbl.grid(row=0, column=0, padx=10, pady=10)

    miBoton = Button(miframe1, text='Conectar', command=conexionBD)
    miBoton.grid(column=1, row=0, padx=10, pady=10)

    miBoton1 = Button(miframe1, text='Aceptar', command=insertarAsitente)
    miBoton1.grid(column=1, row=3, padx=10, pady=10)

    Ventana2.grab_set()
    Ventana2.transient(master=Ventana1)


def salirForm():
    global Ventana2
    aux = messagebox.askyesno(
        title="Confirmar", message='¿Ingresa Asistente nuevo?')
    if aux == 1:
        Ventana2.destroy()
        messagebox.showinfo(title='Alta', message="Ingreso exitoso")
#        ventana2.configure(framelogin(state = 'normal'))


def insertarAsitente():
    global ventana2
    miConexion = sqlite3.connect("BDAsistHome")
    miCursor = miConexion.cursor()

    U = (varNombre.get(), varApellido.get())

    if varNombre.get() != '':
        miCursor.execute("INSERT INTO ASISTENTES VALUES (NULL,?,?)", U)
        miConexion.commit()
        #messagebox.showinfo("BBDD","Registro insertado con exito!!!!")
        salirForm()
    else:
        messagebox.showwarning(
            'BBDD', 'Verifique todos los campos obligatorios')


def ventanaNuevo1():
    global Ventana3
    Ventana3 = Toplevel(Ventana1)
    Ventana1.withdraw()
    barraMenu = Menu(Ventana3)
    Ventana3.config(menu=barraMenu, width=300, height=300)
    Ventana3.title("ASISTENCIA A HOGAR")
    Ventana3.geometry('350x300+300+200')

    miframe1 = Frame(Ventana3)  # ,width=500,height=400)
    miframe1.config(bg="light blue")
    miframe1.config(bd=15)
    miframe1.config(relief=GROOVE)
    miframe1.pack()
    # miframe1.grid(row=0,column=0)
    barraMenu = Menu(Ventana3)

    bbddMenu = Menu(barraMenu, tearoff=0)
    bbddMenu.add_command(label="Crear Base de Datos", command=conexionBD)
    bbddMenu.add_command(label="Salir", command=SalirAplicacion)

    borrarMenu = Menu(barraMenu, tearoff=0)
    borrarMenu.add_command(label="Limpiar los TexBoxs", command=limpiarTexbox1)

    crudMenu = Menu(barraMenu, tearoff=0)
    crudMenu.add_command(label="Insertar", command=insertar)
    crudMenu.add_command(label="Seleccionar", command=seleccionar)
    crudMenu.add_command(label="Actualizar", command=actualizar)
    crudMenu.add_command(label="Eliminar", command=eliminar)

    AyudaMenu = Menu(barraMenu, tearoff=0)
    AyudaMenu.add_command(label="Licencia")
    AyudaMenu.add_command(label="Acerca de....")

    barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
    barraMenu.add_cascade(label="Borrar Campos", menu=borrarMenu)
    barraMenu.add_cascade(label="CRUD", menu=crudMenu)
    barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

    varIdaxf = StringVar()
    varIdaxf.set(0)
    varIdasist = IntVar()
    varIdasist.set(0)
    varNombre = StringVar()
    varApellido = StringVar()
    varIdfamily = IntVar()
    varIdfamily.set(0)
    varFamily = StringVar()
    varFecha = StringVar()
    varComentarios = StringVar()

    txtIdaxf = Entry(miframe1, textvariable=varIdaxf)
    txtIdaxf.grid(row=0, column=1, padx=10, pady=10)

    txtIdasist = Entry(miframe1, textvariable=varIdasist)
    txtIdasist.grid(row=0, column=1, padx=10, pady=10)

    txtNombre = Entry(miframe1, textvariable=varNombre)
    txtNombre.grid(row=1, column=1, padx=10, pady=10)
    txtNombre.config(fg="black", justify="left")

    txtApellido = Entry(miframe1, textvariable=varApellido)
    txtApellido.grid(row=2, column=1, padx=10, pady=10)
    txtApellido.config(fg="black", justify="left")

    txtIdfamily = Entry(miframe1, textvariable=varIdfamily)
    txtIdfamily.grid(row=0, column=1, padx=10, pady=10)

    txtFamily = Entry(miframe1, textvariable=varFamily)
    txtFamily.grid(row=3, column=1, padx=10, pady=10)
    txtFamily.config(fg="black", justify="left")

    txtFecha = Entry(miframe1, textvariable=varFecha)
    txtFecha.grid(row=4, column=1, padx=10, pady=10)
    txtFecha.config(fg="black", justify="left")

    txtComentarios = Text(miframe1, width=25, height=5)
    txtComentarios.grid(row=5, column=1, padx=10, pady=10)
    scrollVert = Scrollbar(miframe1, command=txtComentarios.yview)
    scrollVert.grid(row=5, column=2, sticky="nsew")
    txtComentarios.config(yscrollcommand=scrollVert.set, fg='white', bg='grey')

    labelIdaxf = Label(miframe1, text="ID ASIST HOME: ")
    labelIdaxf.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    labelIdasist = Label(miframe1, text="ID ASISTENTE: ")
    labelIdasist.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    labelNombre = Label(miframe1, text="NOMBRE ASISTENTE: ")
    labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    labelApellido = Label(miframe1, text="APELLIDO ASISTENTE: ")
    labelApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    labelIdfamily = Label(miframe1, text="ID FAMILIA: ")
    labelIdfamily.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    labelFamily = Label(miframe1, text="FAMILIA: ")
    labelFamily.grid(row=3, column=0, sticky="e", padx=10, pady=10)

    labelFecha = Label(miframe1, text="FECHA: ")
    labelFecha.grid(row=4, column=0, sticky="e", padx=10, pady=10)

    labelComentarios = Label(miframe1, text="COMENTARIOS: ")
    labelComentarios.grid(row=5, column=0, sticky="e", padx=10, pady=10)

    miframe2 = Frame(Ventana3)
    miframe2.pack()

    butCreate = Button(miframe2, text="Insertar", command=insertar)
    butCreate.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    butUpdate = Button(miframe2, text="Actualizar", command=actualizar)
    butUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    butRead = Button(miframe2, text="Seleccionar", command=seleccionar)
    butRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    butDelete = Button(miframe2, text="Eliminar", command=eliminar)
    butDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)

    lbl = Label(miframe1, text="Ingrese datos")
    lbl.grid(row=0, column=0, padx=10, pady=10)

    #miBoton= Button(miframe1, text='Aceptar',command = salirForm)
    #miBoton.grid(column=1, row=0,padx=10,pady=10)

    # Ventana3.grab_set()
    Ventana3.mainloop()


def validar():
    if varPass.get() == "hogar":
        messagebox.showinfo('Ingreso correcto', 'Bienvenido '+varUsuario.get())
        ventanaNuevo1()
    else:
        messagebox.showwarning('¡Atencion!', 'Password incorrecto')


def limpiarTexbox():
    varUsuario.set("")
    varPass.set("")


def limpiarTexbox1():
    varIdaxf.set("")
    varIdasist.set("")
    varNombre.set("")
    varApellido.set("")
    varIdfamily.set("")
    varFamily.set("")
    varFecha.set("")
    txtComentarios.delete("1.0", END)
