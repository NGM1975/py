import sqlite3

miConexión = sqlite3.connect("MiBDCRUD")

miPuntero = miConexión.cursor()

#PARA GENERAR UN AUTOINCREMENTO
miPuntero.execute('''
    CREATE TABLE USUARIOS(
    id integer PRIMARY KEY AUTOINCREMENT,
    nombre varchar(40),
    apellido varchar(40),
    dirección varchar(40),
    passw varchar(40),
    obs text)
    ''')
#Si fuera varchar poner UNIQUE
#OJO DEBE SER INTEGER
listaUsuarios = [
    ("Juan","García",'Belgrano 3023','1234','ninguna'),
    ("Mirta","Legrand",'San Juan 2345','1234','ninguna'),
    ("Julieta","Bernal",'Moreno 1044','1234','ninguna'),
    ("Atilio","Gomez",'Larrea 2035','1234','ninguna')
]
##Una sola Instrucción insert para insertar todos los artículos de la lista
miPuntero.executemany('INSERT into USUARIOS values (NULL,?,?,?,?,?)',listaUsuarios)
miConexión.commit()
miConexión.close()