import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
import FreeSimpleGUI as sg



class LayoutsConf:

    CBD = lambda: [ #Conectarse a Base de Datos
        [sg.Text('Host:')],
        [sg.Input(key = 'Host')],
        [sg.Text('Database:')],
        [sg.Input(key = 'Database')],
        [sg.Text('User:')],
        [sg.Input(key = 'User')],
        [sg.Text('Password:')],
        [sg.Input(key = 'Password')],
        [sg.Button('Cancelar'), sg.Button('Conectar')]
    ]

    GTBD = lambda: [ #Guardar Transacciones Base de Datos
        [sg.Text('Estás seguro de guardar las transacciones realizadas?')],
        [sg.Button('No'), sg.Button('Si')]
    ]