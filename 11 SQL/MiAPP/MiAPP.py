from tkinter import*
from tkinter import messagebox 
import sqlite3


Ventana1 = Tk()
barraMenu = Menu(Ventana1)
Ventana1.title("ASISTENCIA A HOGARES")
Ventana1.resizable(False,False)
#Ventana1.geometry('310x200')
Ventana1.config(menu = barraMenu,width=300,height=300,bg= "light grey") 
   
bbddMenu = Menu(barraMenu,tearoff=0) 
bbddMenu.add_command(label="Crear Base de Datos") #,command=conexiónBD)
bbddMenu.add_command(label="Crear Asistente")
bbddMenu.add_command(label="Crear Familia")
bbddMenu.add_command(label="Salir") #,command=SalirAplicación) 

borrarMenu = Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Limpiar los TexBoxs") #,command=limpiarTexbox1) 

crudMenu = Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Insertar") #,command=insertar) 
crudMenu.add_command(label="Seleccionar") #,command=seleccionar)
crudMenu.add_command(label="Actualizar") #,command=actualizar)
crudMenu.add_command(label="Eliminar") #,command=eliminar)

AyudaMenu = Menu(barraMenu,tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de....")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)  
barraMenu.add_cascade(label="Borrar Campos",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=AyudaMenu)

#*********************************************************************
miframe1=Frame(Ventana1,width=500,height=400)
miframe1.config(bg="light blue")
miframe1.config(bd=10)  
miframe1.config(relief=GROOVE)
miframe1.pack()
#miframe1.grid(row=0,column=0)
    
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
    
txtIdaxf = Entry(miframe1,textvariable=varIdaxf)
txtIdaxf.grid(row=1,column=1,padx=10,pady=10)

txtIdasist = Entry(miframe1,textvariable=varIdasist)
txtIdasist.grid(row=2,column=1,padx=10,pady=10)

txtNombre = Entry(miframe1,textvariable=varNombre)
txtNombre.grid(row=3,column=1,padx=10,pady=10)
txtNombre.config(fg="black", justify="left")

txtApellido = Entry(miframe1,textvariable=varApellido)
txtApellido.grid(row=4,column=1,padx=10,pady=10)
txtApellido.config(fg="black", justify="left")

txtIdfamily = Entry(miframe1,textvariable=varIdfamily)
txtIdfamily.grid(row=5,column=1,padx=10,pady=10)

txtFamily = Entry(miframe1,textvariable=varFamily)
txtFamily.grid(row=6,column=1,padx=10,pady=10)
txtFamily.config(fg="black", justify="left")

txtFecha = Entry(miframe1,textvariable=varFecha)
txtFecha.grid(row=7,column=1,padx=10,pady=10)
txtFecha.config(fg="black", justify="left")

txtComentarios = Text(miframe1,width=25,height=5)
txtComentarios.grid(row=8,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miframe1,command=txtComentarios.yview)
scrollVert.grid(row=8,column=2,sticky="nsew")
txtComentarios.config(yscrollcommand=scrollVert.set, fg='black',bg='light grey')

lbl= Label(miframe1,text = "Ingrese datos")
lbl.grid(row=0,column=0,padx=10,pady=10)

labelIdaxf = Label(miframe1,text="ID ASIST HOME: ")
labelIdaxf.grid(row=1,column=0,sticky="e",padx=10,pady=10)

labelIdasist = Label(miframe1,text="ID ASISTENTE: ")
labelIdasist.grid(row=2,column=0,sticky="e",padx=10,pady=10)

labelNombre = Label(miframe1,text="NOMBRE ASISTENTE: ")
labelNombre.grid(row=3,column=0,sticky="e",padx=10,pady=10)

labelApellido = Label(miframe1,text="APELLIDO ASISTENTE: ")
labelApellido.grid(row=4,column=0,sticky="e",padx=10,pady=10)

labelIdfamily = Label(miframe1,text="ID FAMILIA: ")
labelIdfamily.grid(row=5,column=0,sticky="e",padx=10,pady=10)

labelFamily = Label(miframe1,text="FAMILIA: ")
labelFamily.grid(row=6,column=0,sticky="e",padx=10,pady=10)

labelFecha = Label(miframe1,text="FECHA: ")
labelFecha.grid(row=7,column=0,sticky="e",padx=10,pady=10)

labelComentarios = Label(miframe1,text="COMENTARIOS: ")
labelComentarios.grid(row=8,column=0,sticky="e",padx=10,pady=10)
    
miframe2 = Frame(Ventana1)
miframe2.config(bg="light grey")
miframe2.pack()
miframe2.config(bd=5)  
miframe2.config(relief=GROOVE)

butCreate = Button(miframe2,text="Insertar") #,command=insertar)
butCreate.grid(row=1,column=0,sticky="e",padx=10,pady=10)

butUpdate = Button(miframe2,text="Actualizar")  #,command=actualizar)
butUpdate.grid(row=1,column=2,sticky="e",padx=10,pady=10)

butRead = Button(miframe2,text="Seleccionar") #,command=seleccionar)
butRead.grid(row=1,column=1,sticky="e",padx=10,pady=10)

butDelete = Button(miframe2,text="Eliminar") #,command=eliminar)
butDelete.grid(row=1,column=3,sticky="e",padx=10,pady=10)

miframe3 = Frame(Ventana1)
miframe3.config(bg="light grey")
miframe3.pack()
miframe3.config(bd=5)  
miframe3.config(relief=GROOVE)
    
butAsist = Button(miframe3,text="New Asist") #,command=insertar)
butAsist.grid(row=1,column=0,sticky="e",padx=15,pady=10)

butFamily = Button(miframe3,text="New Family") #,command=insertar)
butFamily.grid(row=1,column=2,sticky="e",padx=15,pady=10)


Ventana1.mainloop()