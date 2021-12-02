from tkinter import*
from tkinter import messagebox

raíz = Tk()
raíz.title("Trabajamos con barras de menús....")
#raíz.config()
raíz.iconbitmap("Yo_ok.ico") 
#--------------------------------Funcionees---------------------------------
def ventAcercaDe():
    band = messagebox.showinfo("Acerca de mi aplicación....", "Nombre Aplicación")

def ventLicencia():
    messagebox.showwarning('Acerca de la licencia del producto', 'Licencia BAJO dominio GNU!!')

def ventSalida():
    #band = messagebox.askquestion("Salida","¿Está seguro que desea salir?")
    band = messagebox.askokcancel("Salida","¿Está seguro que desea salir?")
    if (band == True):
        raíz.destroy()

def guardarDoc():
    band = messagebox.askretrycancel("Guardar","No es posible guardar el Documento")
#--------------------------------Barra de Menús--------------------------------------
barraMenu = Menu(raíz)
raíz.config(menu = barraMenu,width=800,height=350)  #ancho y alto de la ventana
raíz.geometry('600x400+200+200') #desplazamiento de ventana en 200 en X e Y
menuArchivo=Menu(barraMenu)#,tearoff=0) #tearoff=0 para que no salga una división tipo barra en
                           #la parte superior del menú desplegable

#-----------------------------Menú Archivo--------------------------------------------
menuArchivo.add_command(label="Nuevo") #crea el menu Archivo
menuArchivo.add_command(label="Guardar",command=guardarDoc)
menuArchivo.add_command(label="Guardar como....")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir",command=ventSalida)
#----------------------------Menú Edición---------------------------------------------- 
menuEdición = Menu(barraMenu) #crea el menu Edición
menuEdición.add_command(label="Cortar")
menuEdición.add_command(label="Copiar")
menuEdición.add_command(label="Pegar")
#---------------------------Menú Herramientas------------------------------------------
menuHerramientas = Menu(barraMenu) #crea el menu Herramientas
menuAyuda = Menu(barraMenu)
menuAyuda.add_command(label="Acerca de....",command=ventAcercaDe)
menuAyuda.add_command(label="Ayuda",command=ventLicencia)
#---------------------Agregar menus a la barra de menús-------------------------------
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)  #agraga el menú archivo a la barra de menús
barraMenu.add_cascade(label="Edición",menu=menuEdición)
barraMenu.add_cascade(label="Herramientas",menu=menuHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)


raíz.mainloop()