import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
from RW.dbload import *
import os
import sys
from Screens import W_Read, W_Write
from layouts.layouts_Pop_Ups import LayoutsPopUps
from layouts.layouts_Read import LayoutsRead
from layouts.layouts_View import LayoutsView
from layouts.layouts_main import LayoutsMain

def VLR (biblioteca):
    window = sg.Window(title='Libros Registrados', keep_on_top = True, modal = True, layout = LayoutsView.VLD(biblioteca), finalize = True)
    while True:
        event, values = window.read()

        if(event == sg.WIN_CLOSED or event == 'Cerrar'): 
            window.close()
            break

def VUR (biblioteca):
    window = sg.Window(title = 'Usuarios Registrados', keep_on_top = True, modal = True, layout = LayoutsView.VUR(biblioteca), finalize = True)
    while True:
        event, values = window.read()

        if(event == sg.WIN_CLOSED or event == 'Cerrar'): 
            window.close()
            break

def VLP (biblioteca):
    window = sg.Window(title = 'Libros Prestados', keep_on_top = True, modal = True, layout = LayoutsView.VPA(biblioteca), finalize = True)
    while True: 
        event, values = window.read()

        if(event == sg.WIN_CLOSED or event == 'Cerrar'):
            window.close()
            break

def VHP (biblioteca):
    window = sg.Window(title = 'Historial de Prestamos', keep_on_top = True, modal = True, layout = LayoutsView.VHP(biblioteca), finalize = True)
    while True:
        event, values = window.read()

        if(event == sg.WIN_CLOSED or event == 'Cerrar'):
            window.close()
            break

def CFU(biblioteca):
    window = sg.Window(size = (480,360),title = 'Consulta Ficha de Usuario', keep_on_top = True, modal = True, layout = LayoutsView.CFU(), finalize = True)
    while True:
        event, values = window.read()

        if(event == 'Buscar'):
            try:
                usuario = biblioteca.usuarios[values['Rut']]
                window['Datos_Usuario'].update(values = [usuario.__str__()])
                
            except Exception as e:  window['Datos_Usuario'].update(values = [f'Rut {e} Inexistente'])

        if(event == sg.WIN_CLOSED or event == 'Cerrar'):
            window.close()
            break
    