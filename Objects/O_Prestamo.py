class Prestamo:
    def __init__(self, id, idus, isbn, fecha_prestamo, fecha_devolución):
        self.id = id
        self.idus = idus
        self.isbn = isbn
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolución = fecha_devolución

    def __str__(self):
        return [f"{self.id}",f"{self.idus}",f"{self.isbn}",f"{self.fecha_prestamo}",f"{self.fecha_devolución}"]

    @property
    def id(self): return self._id
    @property
    def idus(self): return self._idus
    @property
    def isbn(self): return self._isbn
    @property
    def fecha_prestamo(self): return self._fecha_prestamo
    @property
    def fecha_devolución(self): return self._fecha_devolución
    @id.setter
    def id(self, id):   self._id = str(id)
    @idus.setter
    def idus(self, idus):   self._idus = str(idus)
    @isbn.setter
    def isbn(self, isbn):   self._isbn = str(isbn)
    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo):   self._fecha_prestamo = fecha_prestamo
    @fecha_devolución.setter
    def fecha_devolución(self, fecha_devolución):   self._fecha_devolución = fecha_devolución



