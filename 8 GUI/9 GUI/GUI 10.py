from tkinter import *

calculadora = Tk()  
calculadora.title('Operaciones Aritméticas')
calculadora.iconbitmap("Yo_Serio.ico")
miFrame=Frame(calculadora)


#miFrame.pack(side="left")
miFrame.pack(side="right")
#miFrame.pack(side="left",anchor="n")
#miFrame.pack(fill='x')
#miFrame.pack(fill="both",expand= True)
miFrame.config(bd=20)  #borde
miFrame.config(relief=GROOVE)  #marco

#calculadora.config(bd=20)  
#calculadora.config(relief=GROOVE)

miFrame.config(bg="lightblue")

#calculadora.config(bg="yellow")

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