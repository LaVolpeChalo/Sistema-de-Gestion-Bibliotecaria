import datetime
from .O_Usuario import Usuario
from .O_Libro import Libro
from .O_Prestamo import Prestamo


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = {}

    def agregar_libro(self, libro):
        if any(libro.isbn == l.isbn for l in self.libros.values()): raise ValueError("El libro ya se encuentra registrado")
        self.libros[libro.isbn] = libro
        
    def eliminar_libro(self, isbn):
        if not any(l.isbn == isbn for l in self.libros.values()): raise ValueError("El libro no se encuentra en el registro")
        if any (p.isbn == isbn for p in self.prestamos.values()): raise ValueError("El libro posee historial de prestamos")
        trash = self.libros.pop(isbn)

    def registrar_usuario(self, usuario):
        if (self.usuarios.get(usuario.rut)): raise ValueError("Usuario Ya registrado")
        self.usuarios[usuario.rut] = usuario
        
    def eliminar_usuario(self, rut):
        if (self.usuarios.get(rut) is None): raise ValueError("El Usuario no se encuentra en el registro")
        if any (p.rut == rut for p in self.prestamos.values()): raise ValueError("El usuario posee historial de prestamos")
        self.usuarios.pop(id)
      
    def prestar_libro(self, prestamo):
        if prestamo.fecha_prestamo == None and prestamo.id == 'None':
            if (self.usuarios.get(prestamo.rut) is None or self.libros.get(prestamo.isbn) is None): raise ValueError ("Usuario o Libro inexistente")
            if not (self.libros[prestamo.isbn].disponible): raise ValueError ("Libro no Disponible")
            prestamo.fecha_prestamo = datetime.datetime.now()
            prestamo.id = len(self.prestamos)
        self.usuarios.get(prestamo.rut).libros_prestados.append(self.libros.get(prestamo.isbn))
        self.libros.get(prestamo.isbn)._disponible = False

        self.prestamos[prestamo.id] = prestamo

    def devolver_libro(self, isbn, rut):
        if (self.usuarios.get(rut) is None or self.libros.get(isbn) is None): raise ValueError ("Usuario o Libro inexistente")
        if not any (isbn == x.isbn for x in (self.usuarios.get(rut).libros_prestados)): raise ValueError ("Usuario no Posee Libro")
        for i in self.prestamos.values(): 
            if(i.isbn == isbn and i.rut == rut and i.fecha_devolución == None):
                self.prestamos[i.id].fecha_devolución = datetime.datetime.now()
                continue
        self.usuarios.get(rut).libros_prestados.remove(self.libros.get(isbn))
        self.libros.get(isbn).disponible = True

        
    

    def mostrar_libros_registrados(self):
        ret = []
        if(len(self.libros) == 0): return ['No hay libros disponibles']
        for libro in self.libros.values():
                ret.append(libro.__str__())
        
        return ret
    
    def mostrar_libros_arrendados(self):
        ret = []
        if not any (x.disponible == False for x in self.libros.values()):   return ["No hay libros arrendados de momento"]
        else:
            for libro in self.libros.values():
                if not(libro.disponible):
                    ret.append(libro.__str__())
        return ret

    def mostrar_usuarios(self):
        ret = []
        if(len(self.usuarios) == 0): ret.append("No hay usuarios registrados aún")
        else:
            for usuario in self.usuarios.values():
                ret.append(usuario.__str__())

        return ret

    def mostrar_prestamos(self):
        ret = []
        if(len(self.prestamos) == 0):   ret.append("No hay prestamos realizados aún")
        else:
            for prestamo in self.prestamos.values():
                ret.append(prestamo.__str__())

        return ret
        