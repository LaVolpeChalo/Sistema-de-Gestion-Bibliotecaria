class Usuario:
    def __init__(self, rut, nom):
        
        self.rut = rut
        self.nombre = nom
        self._libros_prestados = []
        
    def __str__(self): #modificar str
        ret = [f"{self._rut}",f"{self._nombre}"]
        
        if(len(self._libros_prestados) == 0): ret.append("No posee")
        else:
            for i in range(0, len(self._libros_prestados)):
                ret.append(f"{self._libros_prestados[i].titulo}")
        
        return ret
    
    @property
    def libros_prestados(self): return self._libros_prestados
    @property
    def rut(self):   return self._rut
    @property
    def nombre(self):   return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if (len(nombre) == 0):  raise ValueError("El Nombre no puede estar vacío")
        
        if (nombre.isdigit()):    raise TypeError("El Nombre no puede ser solo numeros")
        
        self._nombre = nombre
    @rut.setter
    def rut(self, rut):  self._rut = str(rut)
    