# para trabajar con bases de datos debemos primero importar lo siquiente:
import sqlite3 as dbapi
# esto nos wervirá para trabajar con una base de datos SQLite (un archivo)

database = dbapi.connect('database.dat')# esto se conectara a nuestra DB si no esta creada la crea

# ahora debemos instanciar el cursor de la base de datos, para indicarle donde estamos
cursor = database.cursor()

try:
    #ahora creamos la tabla de la base de datos
    cursor.execute("""
    create table usuarios (
    dni text,
    nombre text,
    edad integer,
    genero text,
    trabajando boolean) 
    """)

except dbapi.DatabaseError as e:
    print("Error creando la tabla USUARIOS")

try:
    # una vez creada la tabla vamos a hacer unos inserts de diferentes dato s aguardar en la base de datos
    cursor.execute("""insert into usuarios values ('1234A',"Marcos Avendaño",23,"Hombre",True)""")
    cursor.execute("""insert into usuarios values ('1234B',"Manolo Lama",90,"Hombre",True)""")
    cursor.execute("""insert into usuarios values ('1234C',"Elon Musk",40,"Hombre",True)""")
    cursor.execute("""insert into usuarios values ('1234D',"Perro Sanchez",900,"Mujer",True)""")
    database.commit()

except dbapi.OperationalError as e:
    print("Error al insertar los datos en la base de datos")





