import sqlite3

miConexión = sqlite3.connect("MiBD3")

miPuntero = miConexión.cursor()

#miPuntero.execute('''
#    CREATE TABLE ARTÍCULOS (
#    código integer PRIMARY KEY,
#    descripción varchar(40),
#    precio double)
#    ''')

#miPuntero.executemany('INSERT into ARTÍCULOS values (?,?,?)',listaArtículos)

## PARA GENERAR UN AUTONUMÉRICO DDL
miPuntero.execute('''
    CREATE TABLE ARTÍCULOS (
    código integer PRIMARY KEY AUTOINCREMENT,
    descripción varchar(40),
    precio double)
    ''')

#Crear una lista de artículos
listaArtículos = [
    ("Camión azul volcador", 234.80),
    ("Jarrón de Porcelana", 584.00),
    ("Remera Superman", 400.80),
    ("Pantalones de jean tipo Superman", 600.80)
]
miPuntero.executemany('INSERT into ARTÍCULOS values (NULL,?,?)',listaArtículos)
miConexión.commit()
miConexión.close()