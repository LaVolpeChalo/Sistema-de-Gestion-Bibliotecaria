import psycopg2
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Libro import Libro
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo


def load(titirilken):
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '1234',
            database = 'Test'

        )
        print("\nConexión Exitosa\n")


        cursor =   connection.cursor()


        cursor.execute('SELECT * FROM libros;')
        for row in cursor.fetchall():
            lib = Libro(*row)
            titirilken.agregar_libro(lib)

        cursor.execute('SELECT * FROM usuarios;')
        for row in cursor.fetchall():
            us = Usuario(*row)
            titirilken.registrar_usuario(us)

        cursor.execute('SELECT * FROM prestamos;')
        for row in cursor.fetchall():
            pres = Prestamo(*row)
            pres.idus =str(pres.idus)
            if(pres.fecha_devolución != None):
                titirilken.prestamos[str(pres.id)] = pres
            else:
                titirilken.prestar_libro(pres)
        
    
    except Exception as e:
        print(e)


def save(titirilken):
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = '1234',
            database = 'Test'

        )

        cursor = connection.cursor()

        print("\nConexión Exitosa\n")

        cursor.execute('DELETE FROM prestamos;')
        cursor.execute('DELETE FROM libros;')
        cursor.execute('DELETE FROM usuarios;')


        #Traspaso Libros a BD
        contenedor = titirilken.libros.values()

        data = [(l.isbn, l.titulo, l.autor, l.disponible) for l in contenedor]

        cursor.executemany("""INSERT INTO libros(ISBNLibro, Titulo, Autor, Disponible)
                           Values (%s, %s, %s, %s);""", data)

        #Traspaso Usuarios a BD
        contenedor = titirilken.usuarios.values()

        data = [(u.id_usuario, u.nombre) for u in contenedor]


        cursor.executemany("""INSERT INTO usuarios(idusuario, nombre)
                           Values (%s, %s);""", data)

        #Traspaso Prestamos a BD
        contenedor = titirilken.prestamos.values()

        data = [(p.id, p.idus, p.isbn, p.fecha_prestamo, p.fecha_devolución) for p in contenedor]

        cursor.executemany("""INSERT INTO prestamos(id, idusuario, isbnlibro, fechaprestamo, fechadevolución)
                           Values (%s, %s, %s, %s, %s)""", data)
        
        connection.commit()#Se hace commit de todo

    except Exception as e:
        print(e)