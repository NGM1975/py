#widget se llaman los distintos componentes (objetos)
#que podemos colocar dentro de un contenedor tipo ventana
#ejemplo con etiquetas o label
from tkinter import *
ventana = Tk()  #objeto raíz contenedor de objetos
ventana.title("Bienvenido a mi Segunda ventana ")
ventana.iconbitmap("Yo_ok.ico")

ventana.geometry('800x400')
ventana.resizable(False,False)
ventana.config(bg= 'grey')
lbl1 = Label(ventana, text = "Hola.....Label Uno")

lbl1.grid(column=0,row=0,padx=10,pady=10) #padx y pady sirven para establecer marcos

lbl2 = Label(ventana,text = "Bienvenidos a label Dos")

lbl2.grid(column=0,row=1,padx=10,pady=10)

lbl3 = Label(ventana,text = "Bienvenidos a label Tres", font = ("Arial Bold", 30))

lbl3.grid(column=2,row=3,padx=10,pady=10)

ventana.mainloop()