import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
import FreeSimpleGUI as sg

class LayoutsView:
    
    VLD = lambda biblioteca: [ #Ver Libros Disponibles
        [sg.Table(values = biblioteca.mostrar_libros_registrados() ,
                         

        headings = ['Titulo', 'Autor', 'ISBN', 'Estado'])],
        
        [sg.Button('Cerrar')]   ]

    VUR = lambda biblioteca: [ #Ver Usuarios Registrados
        [sg.Table(values = biblioteca.mostrar_usuarios() ,
                  
        headings = ['Rut Usuario', 'Nombre', 'Libros Arrendados'])],

        [sg.Button('Cerrar')]   ]

    VPA = lambda biblioteca: [ #Ver Prestamos Activos
        [sg.Table(values = biblioteca.mostrar_libros_arrendados(),

        headings = ['Titulo', 'Autor', 'ISBN', 'Estado'])],

        [sg.Button('Cerrar')]   ]

    VHP = lambda biblioteca: [#Historial de Prestamos
        [sg.Table(values = biblioteca.mostrar_prestamos(),

        headings = ['ID', 'Rut Usuario', 'ISBN Libro', 'Fecha Prestamo', 'Fecha Devolución'])],

        [sg.Button('Cerrar')]   ]

    CFU = lambda: [#Consultar Ficha Usuario
        [sg.Text('Rut Usuario')],
        [sg.Input(default_text = 'Ej:12.345.678-9', key = 'Rut')],
        [sg.Button('Buscar')],
        [sg.Table(values = [], headings = ['ID Usuario', 'Nombre', 'Libros Arrendados'], key = 'Datos_Usuario')],
        [sg.Button('Cerrar')]   ]
