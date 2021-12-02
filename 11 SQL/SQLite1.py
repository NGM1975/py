import sqlite3

miConexión = sqlite3.connect("MiBD1")

miPuntero = miConexión.cursor()
##Instrucciones en lenguaje SQL
##Instrucción DDL para crear la estructura
miPuntero.execute("CREATE TABLE ARTÍCULOS (código integer, descripción varchar(40),precio double)")

##Instrucción DML para insertar dos artículos
miPuntero.execute('INSERT into ARTÍCULOS values (100,"PELOTA NRO 5", 123.50)')
miPuntero.execute('INSERT into ARTÍCULOS values (101,"SET DE PELOTAS DE TENIS", 540)')

##Instrucción DML que realiza una consulta en la BD
miPuntero.execute("SELECT * FROM ARTÍCULOS")

##Creo una lista con los datods que vienen de la consulta de la BD con fetchall()
#listaConsulta = miPuntero.fetchall()
##Esta conversión puede ser hecha con list()
listaConsulta = list(miPuntero)
##Muestro la lista por consola
print('-'*60)
print(listaConsulta)
print('-'*60)
##También se puede mostrar en un ciclo
print('-'*60)
for artículo in listaConsulta:
    print("Código: ", artículo[0],"Descrición: ", artículo[1], 'Precio: ',artículo[2])
    ##print(artículo)
print('-'*60)

##Instrucción para confirmar los cambios en la BD
miConexión.commit()
miConexión.close()