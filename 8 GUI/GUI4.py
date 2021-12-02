#widget se llaman los distintos componentes (objetos)
#Class Entry (textbox)
from tkinter import *
ventana = Tk()  #objeto raíz contenedor de objetos
ventana.title("Ventana para el ingreso de datos...")
#ventana.iconbitmap("Yo_ok.ico")

#fución para controlar ante evento click del botón
def eventoClick():
    res = "Bienvenido SR/A" + txt.get()
    lbl.configure(text= res)
    txt.config(background="black",fg="#03f943",justify = "center")
    #txt.config(state= disabled)

ventana.geometry('800x400')
ventana.resizable(False,False)
ventana.config(bg= 'grey')
#creación de un label
lbl = Label(ventana, text = "Hola....")
lbl.grid(column=3,row=2,padx=10,pady=10,columnspan=3) 
#creación de una entrada de datos
txt = Entry(ventana,width=30)
txt.grid(column=0,row=1,padx=10,pady=10)
#creación de un botón
btn = Button(ventana, text = "Botón 6", command = eventoClick)
btn.grid(column=0,row=2,padx=10,pady=10)


ventana.mainloop()