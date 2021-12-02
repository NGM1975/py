import sqlite3

miConexión = sqlite3.connect("MiBD3")

miPuntero = miConexión.cursor()

#Tabla con  clase primaria
miPuntero.execute('''
    CREATE TABLE ESTUDIANTES(
    matrícula varchar(4) PRIMARY KEY,
    apellido varchar(40),
    nombres varchar(40),
    nota doble)
    ''')

listaEstudiantes = [
    ("A101","Amaya","Isaías", 4.80),
    ("B102","Cingolani","Osvaldo", 4.00),
    ("C103","Fernández", "Superman", 6.80),
    ("C104","Olmedo","Juana", 7.50)
]
##Una sola Instrucción insert para insertar todos los artículos de la lista
miPuntero.executemany('INSERT into ESTUDIANTES values (?,?,?,?)',listaEstudiantes)

##Realizamos consulta con select en la BD
miPuntero.execute("SELECT * FROM ESTUDIANTES")

##Creo una lista con los datods de la BD 
listaConsulta = miPuntero.fetchall()

print('-'*60)
print(listaConsulta)
print('-'*60)
##Muestro la lista por Consola en un ciclo
print('-'*60)
for estudiante in listaConsulta:
    print("Matrícula: ", estudiante[0]," Apellido: ", estudiante[1], ' Nombre: ',estudiante[2], ' Nota: ',estudiante[3])
    ##print(artículo)
print('-'*60)
print("\n")

##Instrucción para confirmar los cambios en la BD
miConexión.commit()
miConexión.close()