import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
from RW import dbload
from RW.dbload import *
import os
import sys
from Screens import W_Conf, W_Read, W_Write
from layouts.layouts_Pop_Ups import LayoutsPopUps
from layouts.layouts_Read import LayoutsRead
from layouts.layouts_View import LayoutsView
from layouts.layouts_main import LayoutsMain

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

icon_path = resource_path('src/Icon.ico')
sg.theme('Green Mono')
biblioteca = Biblioteca()
dbkey = {}
##load(biblioteca)

# Create the Window
window = sg.Window('Gestor Biblioteca', layout = LayoutsMain.Main(), icon=icon_path)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if(event == 'Ver Libros Registrados'):
       W_Read.VLR(biblioteca)

    if(event == 'Ver Usuarios Registrados'):
       W_Read.VUR(biblioteca)

    if(event == 'Ver Libros Prestados'):
        W_Read.VLP(biblioteca)

    if(event == 'Ver Historial de Prestamos'):
        W_Read.VLP(biblioteca)

    if(event == 'Consultar Ficha de Usuario'):
        W_Read.CFU(biblioteca)

    if(event == 'Registrar Usuario'):
        W_Write.RU(biblioteca)

    if(event == 'Registrar Libro'):
        W_Write.RL(biblioteca)
    
    if(event == 'Prestar Libro'):
        W_Write.PL(biblioteca)

    if(event == 'Eliminar Usuario'):
        W_Write.EU(biblioteca)
    
    if(event == 'Eliminar Libro'):
        W_Write.EL(biblioteca)

    if(event == 'Devolver Libro'):
        W_Write.DL(biblioteca)

    if(event == 'Conectarse a Base de Datos'):
        W_Conf.CBD(biblioteca, dbkey)
    
    if(event == 'Guardar Transacciones en Base de Datos'):
        W_Conf.GTBD(biblioteca, dbkey)

    if (event == sg.WIN_CLOSED or event == 'Cerrar'):
        LayoutsPopUps.CierrePrograma()
        break

window.close()