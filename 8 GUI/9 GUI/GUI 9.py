from tkinter import *
from tkinter.ttk import *  #para el combobox
from tkinter import messagebox

ventana = Tk()  
ventana.title('Bienvenidos a la práctica de Radio Buttons and Check Buttons')
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

lbl3 = Label(ventana, text="Estudios...")
lbl3.grid(column=0,row=3,sticky='e',padx=10,pady=10)

lbl2 = Label(ventana, text="Sexo...")
lbl2.grid(column=0,row=6,sticky='e',padx=10,pady=10)

comboLoc = Combobox(ventana)
comboLoc['values']=('Mar del Plata','Miramar','Necochea','Balcarce','Tandil','Text')
comboLoc.current(0)  #set the selected item... por defecto localidad MDP
comboLoc.grid(column=1, row=2)
#--------------------------------------------------------------------------
primaria = BooleanVar() #también puede ser variable entera idem C
primaria.set(True)   #set check state
check1 = Checkbutton(ventana,text='Primario', var= primaria)
check1.grid(column=1,row=3,sticky="w",padx=5,pady=5)

#--------------------------------------------------------------------------
secundaria = BooleanVar() 
secundaria.set(False)   #set check state
check1 = Checkbutton(ventana,text='Secundario', var= secundaria)
check1.grid(column=1,row=4,sticky="w",padx=5,pady=5)

#--------------------------------------------------------------------------
def superiores():
    global superior
    superior= not superior
    print('superior es...',superior)

superior = BooleanVar() 
superior.set(False)   #set check state
check1 = Checkbutton(ventana,text='Superior', command=superiores,var=superior)
check1.grid(column=1,row=5,sticky="w",padx=5,pady=5)

#------------------------------------------------------------------------------
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
#------------------------------radios-----------------------------------------------
def sexoSelectado():
    aux=sexo.get()
    if aux == 1:
        messagebox.showinfo(title='Sexo',message='Sexo seleccionado masculino')
    elif aux == 2:
        messagebox.showinfo(title='Sexo',message='Sexo seleccionado femenino')
    else:
        messagebox.showinfo(title='Sexo',message='Sexo seleccionado es otro')

sexo = IntVar()
sexo.set(1)
masculino = Radiobutton(ventana,text='Masculino', value=1, variable=sexo, command=sexoSelectado)
femenino = Radiobutton(ventana,text='Femenino', value=2, variable=sexo, command=sexoSelectado)
otro = Radiobutton(ventana,text='Otro', value=3, variable=sexo, command=sexoSelectado)
masculino.grid(column=1,row=6,sticky='w',padx=5,pady=5)
femenino.grid(column=1,row=7,sticky='w',padx=5,pady=5)
otro.grid(column=1,row=8,sticky='w',padx=5,pady=5)

#----------------------------------------------------------------------------------------

btn = Button(ventana, text = "Confirmar", command = eventoClick)
btn.grid(column=0,row=9,padx=10,pady=10)

btSalir = Button(ventana, text = "Salir", command = salirAplicación)
btn.grid(column=1,row=9,padx=15,pady=15)

ventana.mainloop()