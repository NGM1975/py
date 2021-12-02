from tkinter import *
#creación de ventanas a través  de Tkinter
ventana = Tk()   #objeto raíz contenedor de objetos
ventana.title("Bienvenido a mi primera ventana ")

ventana.geometry('300x400')
#el método geometry de la clase Tk una un parámetro tipo cadena que
#representa ancho y alto de la ventana
#ventana.geometry("800x550")  #establecer sus dimensiones

ventana.resizable(True,False)  #ancho y alto en False fija los valores

ventana.iconbitmap("Yo_ok.ico")  #png o ici o ico formatos de imágenes aceptadas
                                #para que aparezca como icono de la ventana
                                #la imágen debe estar en el directorio de trabajo

ventana.config(bg = "green")

ventana.mainloop()    #ciclo infinito de escucha... espera que ocurran eventos en el contexto