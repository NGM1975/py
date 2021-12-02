import sqlite3

miConexión = sqlite3.connect("MiBD2")

miPuntero = miConexión.cursor()

##Instrucción DDL para crear la estructura
miPuntero.execute("CREATE TABLE ARTÍCULOS (código integer,descripción varchar(40),precio double)")

#Crear una lista de artículos
listaArtículos = [
    (101,"Camión azul volcador", 234.80),
    (102,"Jarrón de Porcelana", 584.00),
    (103,"Remera Superman", 400.80)
]
##Una sola Instrucción insert para insertar todos los artículos de la lista
miPuntero.executemany('INSERT into ARTÍCULOS values (?,?,?)',listaArtículos)


##Realiza consulta con select en la BD
miPuntero.execute("SELECT * FROM ARTÍCULOS")

##Creo una lista con los datods de la BD 
listaConsulta = miPuntero.fetchall()

print('-'*60)
print(listaConsulta)
print('-'*60)
##Muestro la lista por Consola en un ciclo
print('-'*60)
for artículo in listaConsulta:
    print("Código: ", artículo[0]," Descrición: ", artículo[1], ' Precio: ',artículo[2])
    ##print(artículo)
print('-'*60)
print("\n")

##Instrucción para confirmar los cambios en la BD
miConexión.commit()
miConexión.close()