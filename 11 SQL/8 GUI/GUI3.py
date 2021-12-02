#widget se llaman los distintos componentes (objetos)
#Botones de acción buttons-----
from tkinter import *
ventana = Tk()  #objeto raíz contenedor de objetos
ventana.title("Bienvenido a mi Tercera ventana ")
#ventana.iconbitmap("Yo_ok.ico")

ventana.geometry('800x400')
ventana.resizable(False,False)
ventana.config(bg= 'grey')
lbl1 = Label(ventana, text = "Label en fila 0 columna 1")

lbl1.grid(column=0,row=0,padx=10,pady=10) #padx y pady sirven para establecer marcos

lbl2 = Label(ventana,text = "Label en fila 0 columna 1")

lbl2.grid(column=1,row=0,padx=10,pady=10)

lbl3 = Label(ventana,text = "Label en fila 3 columna 2", font = ("Arial Bold", 30))

lbl3.grid(column=2,row=3,padx=10,pady=10)
#creacióin de un objeto Button
btn1 = Button(ventana, text = "Boton 1 en fila 4 y Columna 0")
btn1.grid(column=0,row=4)

#otro botón con cambio color fuente y fondo
def eventoClick():
    print("Hiciste click en el botón 5")
    ventana.config(bg="purple")

def eventoClick1():
    print("Hiciste click en el botón 4")
    ventana.config(bg="orange")

def eventoClick2():
    lbl1.configure(text = "Clickeaste en el botón 6 !!",bg ='brown',fg ='white')

def eventoClick3():
    lbl3.configure(text = "Clickeaste en el botón 7 !!",bg ='green',fg ='lightblue')

btn2 = Button(ventana, text = "Boton 2 en fila 5 y Columna 0",bg= "blue", fg= "yellow")
btn2.grid(column=0,row=6,padx=10,pady=10) 

#como controlar el evento click de un botón, comando command
btn4 = Button(ventana, text = "Boton 4",command= eventoClick1)
btn4.grid(column=1,row=5,padx=10,pady=10)

btn5 = Button(ventana, text = "Boton 5",command= eventoClick)
btn5.grid(column=0,row=5,padx=10,pady=10)

btn6 = Button(ventana, text = "Boton 6",command= eventoClick2)
btn6.grid(column=0,row=7,padx=10,pady=10)

btn7 = Button(ventana, text = "Boton 7",command= eventoClick3)
btn7.grid(column=1,row=7,padx=10,pady=10)

ventana.mainloop()