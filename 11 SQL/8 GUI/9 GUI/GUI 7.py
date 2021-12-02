from tkinter import *
from tkinter import messagebox

ventana = Tk()  
ventana.title('Bienvenidos a la práctica de Python')
ventana.iconbitmap("Yo_ok.ico")
ventana.geometry('450x400')

lbl = Label(ventana, text="Nombres...")
lbl.grid(column=1,row=0)
txt = Entry(ventana,width=20)
txt.grid(column=1,row=1,padx=10,pady=10)

lbl = Label(ventana, text="Apellido...")
lbl.grid(column=1,row=2)
txt1 = Entry(ventana,width=20)
txt1.grid(column=1,row=3,padx=10,pady=10)

def eventoClick():
    messagebox.showinfo(title='¡¡Saludo!!', message= "Bienvenido SR/A" + txt.get())
    txt.focus()  #pasa el control o foco al objeto designado
    txt1.config(state= "disabled") #el Entry queda desabilitado para ingreso de datos 

btn = Button(ventana, text = "Saludar", command = eventoClick)
btn.grid(column=1,row=4,padx=10,pady=10)

ventana.mainloop()