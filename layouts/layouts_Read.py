import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
import FreeSimpleGUI as sg

class LayoutsRead:
    
    RU = lambda: [#Registrar Usuario
        [sg.Text('Ingrese Nombre Usuario')],
        [sg.Input(default_text = 'Ej: Darth Vader', key = 'Nombre')],
        [sg.Text('Ingrese Rut Usuario')],
        [sg.Input(default_text = 'Ej: 12.345.678-9', key = 'Rut')],
        [sg.Button('Cancelar'), sg.Button('Registrar')] ]

    RL = lambda: [#Registrar Libro
        [sg.Text('ISBN')],
        [sg.Input(default_text = 'Ej: 123-45-67890-12-3', key = 'ISBN')],
        [sg.Text('Titulo')],
        [sg.Input(default_text = 'Ej: El Libro Troll', key = 'Titulo')],
        [sg.Text('Autor')],
        [sg.Input(default_text = 'Franz Kafka', key = 'Autor')],
        [sg.Button('Cancelar'), sg.Button('Registrar')] ]

    PL = lambda: [#Prestar Libro
        [sg.Text('Rut Usuario')],
        [sg.Input(default_text = 'Ej: 12.345.678-9', key = 'Rut')],
        [sg.Text('ISBN Libro')],
        [sg.Input(default_text = 'Ej: 123-45-67890-12-3', key = 'ISBN')],
        [sg.Button('Cancelar'), sg.Button('Registrar')] ]

    EU = lambda: [#Eliminar Usuario
        [sg.Text('Rut Usuario')],
        [sg.Input(default_text = 'Ej: 12.345.678-9', key = 'Rut')],
        [sg.Button('Cancelar'), sg.Button('Eliminar')]  ]

    EL = lambda: [#Eliminar Libro
        [sg.Text('ISBN')],
        [sg.Input(default_text = 'Ej: 123-45-67890-12-3', key = 'ISBN')],
        [sg.Button('Cancelar'), sg.Button('Eliminar')]  ]

    DL = lambda: [#Devolver Libro
        [sg.Text('ISBN')],
        [sg.Input(default_text = 'Ej: 123-45-67890-12-3', key = 'ISBN')],
        [sg.Text('Rut Usuario')],
        [sg.Input(default_text = 'Ej: 12.345.678-9', key = 'Rut')],
        [sg.Button('Cancelar'), sg.Button('Devolver')]  ]