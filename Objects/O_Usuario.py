class Usuario:
    def __init__(self, id_u, nom):
        
        self.id_usuario = id_u
        self.nombre = nom
        self._libros_prestados = []
        
    def __str__(self): #modificar str
        ret = [f"{self._id_usuario}",f"{self._nombre}"]
        
        if(len(self._libros_prestados) == 0): ret.append("No posee")
        else:
            for i in range(0, len(self._libros_prestados)):
                ret.append(f"{self._libros_prestados[i].titulo}")
        
        return ret
    
    @property
    def libros_prestados(self): return self._libros_prestados
    @property
    def id_usuario(self):   return self._id_usuario
    @property
    def nombre(self):   return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if (len(nombre) == 0):  raise ValueError("El Nombre no puede estar vacío")
        
        if (nombre.isdigit()):    raise TypeError("El Nombre no puede ser solo numeros")
        
        self._nombre = nombre
    @id_usuario.setter
    def id_usuario(self, id_u):  self._id_usuario = str(id_u)
    