class Libro:
    def __init__(self,isbn,tit,aut,disponible): #Se le añade disponible como parametro para evitar errores con bd
        
        self.titulo = tit
        self.autor = aut
        self.isbn = isbn
        self.disponible = disponible
    
    def __str__(self):
        
        ret = [f"{self.titulo}",f"{self.autor}",f"{self.isbn}"]
        if(self._disponible): ret.append("Disponible")
        else: ret.append("Arrendado")
        
        return ret
    
    @property
    def titulo(self):   return self._titulo
    @property
    def autor(self):    return self._autor
    @property
    def isbn(self): return self._isbn
    @property
    def disponible(self):   return self._disponible
    @titulo.setter
    def titulo(self, tit):
        if (len(tit) == 0): raise ValueError("El Titulo No puede estar vacío")
        #Tuve que borrar la comprobación de que fueran solo números debido a 1984 de Aldous Huxley
        self._titulo = tit
        
    @autor.setter    
    def autor(self, aut):
        if (len(aut) == 0): raise ValueError("El Autor No puede estar vacío")
        
        if(aut.isdigit()): raise TypeError("El Autor no puede ser solo numeros")
        
        self._autor = aut
        
    @isbn.setter
    def isbn(self,isbn): # Se Podría agregar conversor de isbn de 10 num a 13
        if (len(isbn) > 17 or len(isbn) < 17): raise ValueError("Solo aceptamos isbn en formato de 13 digitos")
        cont = isbn.split('-')
        if  (len(cont) != 5): raise TypeError("Formato Incorrecto")
        
        if not all( i.isdigit() for i in cont): raise TypeError("Solo puede poseer numeros y \'-\'")
        
        self._isbn = str(isbn)

    @disponible.setter
    def disponible(self, bool):
        self._disponible = bool
            