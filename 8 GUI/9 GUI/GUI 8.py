from tkinter import *
from tkinter.ttk import *  #para el combobox
from tkinter import messagebox

ventana = Tk()  
ventana.title('Bienvenidos a la práctica de Combobox')
ventana.iconbitmap("Yo_ok.ico")
ventana.geometry('450x400')

lbl = Label(ventana, text="Nombres...")
lbl.grid(column=0,row=0,sticky='e')  #sticky puede ser n s e w ne nw se y sw
txt = Entry(ventana,width=20)
txt.grid(column=1,row=0,padx=10,pady=10)

lbl1 = Label(ventana, text="Dirección calle y número...")
lbl1.grid(column=0,row=1,sticky='e')
txt1 = Entry(ventana,width=20)
txt1.grid(column=1,row=1,padx=10,pady=10)

lbl2 = Label(ventana, text="Localidad...")
lbl2.grid(column=0,row=2,sticky='e',padx=10,pady=10)

comboLoc = Combobox(ventana)
comboLoc['values']=('Mar del Plata','Miramar','Necochea','Balcarce','Tandil','Text')
comboLoc.current(0)  #set the selected item... por defecto localidad MDP
comboLoc.grid(column=1, row=2)


def eventoClick():
    aux =  messagebox.showinfo(title='Confirmación', message= "Confirma que vive en la localidad: " + comboLoc.get())
    if aux == 1:
        messagebox.showinfo(title="Confirmar",message='Almacenado correctamente')
    txt.focus()  #pasa el control o foco al objeto designado
    txt1.config(state= "disabled") #el Entry queda desabilitado para ingreso de datos 

def salirAplicación():
    aux =  messagebox.showinfo(title='Confirmación', message= "Confirma salir de la aplicación")
    if aux == 1:
        ventana.destroy()

btn = Button(ventana, text = "Confirmar", command = eventoClick)
btn.grid(column=0,row=6,padx=10,pady=10)

btSalir = Button(ventana, text = "Salir", command = salirAplicación)
btn.grid(column=1,row=6,padx=15,pady=15)

ventana.mainloop()