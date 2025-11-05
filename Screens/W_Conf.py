import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
from RW import dbload
from RW.dbload import *
import os
import sys
from Screens import W_Read, W_Write
from layouts.layouts_Pop_Ups import LayoutsPopUps
from layouts.layouts_Read import LayoutsRead
from layouts.layouts_View import LayoutsView
from layouts.layouts_conf import LayoutsConf
from layouts.layouts_main import LayoutsMain



def CBD (biblioteca, dbkey):
    window = sg.Window(title = 'Conexion a Base de Datos', keep_on_top = True, modal = True, layout = LayoutsConf.CBD(), finalize = True)
    while True:
            event, values = window.read()

            if(event == 'Conectar'):
                dbkey.update([('host' , values['Host']),
                            ('user' , values['User']),
                            ('password' , values['Password']),
                            ('database' , values['Database'])])
                dbload.load(biblioteca , dbkey)
                     

            if(event == sg.WIN_CLOSED or event == 'Cancelar'):
                window.close()
                break

def GTBD (biblioteca, dbkey):
     window = sg.Window(title = 'Confirmar Guardado', keep_on_top = True, modal = True, layout = LayoutsConf.GTBD(), finalize = True)
     while True:
            event, values = window.read()

            if(event == 'Si'):
               dbload.save(biblioteca, dbkey)

            if(event == sg.WIN_CLOSED or event == 'No'):
                 window.close()
                 break
            