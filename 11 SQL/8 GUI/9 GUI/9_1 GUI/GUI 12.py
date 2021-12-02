from tkinter import *

calculadora = Tk()  
calculadora.title('Práctica com Label Frames')
calculadora.iconbitmap("Yo_Ahorc.ico")
calculadora.config(bd=20)  
calculadora.config(relief=GROOVE)
#calculadora.config(bg="yellow")
#---------------------primer LabelFrame-----------------------------------------------
miFrame=LabelFrame(calculadora,text = "Este es el encabezado de LabelFrame")  
miFrame.config(bg="purple")
miFrame.grid(column=0,row=0,padx=10,pady=10)
#---------------------segundo LabelFrame-----------------------------------------------
miFrame2=LabelFrame(calculadora,text = "Segundo Frame")  
miFrame2.config(bg="green")
miFrame2.grid(column=0,row=1,padx=10,pady=10)
#-----------------------------widget para frame 2----------------------------------------
cartelitoFrame2 = Label(miFrame2, text= "Pulse botón para finalizar aplicación")
cartelitoFrame2.grid(column=0,row=0)
cartelitoFrame2.config(bg="lightblue")

butSalir = Button(miFrame2, text= 'Finalizar Aplicación',width=26,height=2)
butSalir.grid(column=0,row=1)
butSalir.config(fg="brown")

#------------------------PANTALLA----------------------------------------------
pantalla = Entry(miFrame) 
pantalla.grid(column=2,row=1,padx=10,pady=10,columnspan=4)
pantalla.config(bg="black",fg="#03f943",justify='right')
#columnspan=4  es para que la caja de texto ocupe 4 columnas del grig
#----------------------PRIMERA FILA------------------------------------------------
boton7=Button(miFrame,text="7",width=3)
boton7.grid(row=2,column=1,padx=5,pady=5)
boton8=Button(miFrame,text="8",width=3)
boton8.grid(row=2,column=2,padx=5,pady=5)
boton9=Button(miFrame,text="9",width=3)
boton9.grid(row=2,column=3,padx=5,pady=5)
botonMult=Button(miFrame,text="x",width=3)
botonMult.grid(row=2,column=4,padx=5,pady=5)
#-----------------------SEGUNDA FILA-----------------------------------------------
boton4=Button(miFrame,text="4",width=3)
boton4.grid(row=3,column=1,padx=5,pady=5)
boton7=Button(miFrame,text="5",width=3)
boton7.grid(row=3,column=2,padx=5,pady=5)
boton7=Button(miFrame,text="6",width=3)
boton7.grid(row=3,column=3,padx=5,pady=5)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=3,column=4,padx=5,pady=5)
#-----------------------TERCERA FILA--------------------------------------
boton1=Button(miFrame,text="1",width=3)
boton1.grid(row=4,column=1,padx=5,pady=5)
boton2=Button(miFrame,text="2",width=3)
boton2.grid(row=4,column=2,padx=5,pady=5)
boton3=Button(miFrame,text="3",width=3)
boton3.grid(row=4,column=3,padx=5,pady=5)
botonRest=Button(miFrame,text="-",width=3)
botonRest.grid(row=4,column=4,padx=5,pady=5)
#----------------------CUARTA FILA-----------------------------------------
boton0=Button(miFrame,text="0",width=3)
boton0.grid(row=5,column=1,padx=5,pady=5)
botonIgual=Button(miFrame,text="=",width=3)
botonIgual.grid(row=5,column=2,padx=5,pady=5)
botonComa=Button(miFrame,text=",",width=3)
botonComa.grid(row=5,column=3,padx=5,pady=5)
botonSum=Button(miFrame,text="+",width=3)
botonSum.grid(row=5,column=4,padx=5,pady=5)


calculadora.mainloop()