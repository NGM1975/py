import sqlite3
#crea o conecta con una base de datos existente
miConexión = sqlite3.connect("MiBD0")

miPuntero = miConexión.cursor()
##Instrucciones en lenguaje SQL
##Instrucción DDL para crear la estructura
miPuntero.execute("CREATE TABLE ARTÍCULOS (código integer, descripción varchar(40),precio double)")

##Instrucción DML para insertar dos astículos
miPuntero.execute('INSERT into ARTÍCULOS values (100,"PELOTA NRO 5", 123.50)')

##Instrucción para confirmar transacción
miConexión.commit()
miConexión.close()