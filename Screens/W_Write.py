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

def RU(biblioteca):
    window = sg.Window(title = 'Registro Usuario Nuevo', keep_on_top = True, modal = True, layout = LayoutsRead.RU(), finalize = True)
    while True:
        event, values = window.read()

        if(event == 'Registrar'):
            try:
                biblioteca.registrar_usuario(Usuario(values['Rut'], values['Nombre']))
                LayoutsPopUps.ExitoRegistro()
                window.close()
                break
            except ValueError as e: LayoutsPopUps.ErrorRegistro(e)
        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            window.close()
            break 

def RL(biblioteca):
    window = sg.Window(title = 'Registro Libro Nuevo', keep_on_top = True, modal = True, layout = LayoutsRead.RL(), finalize = True)
    while True:
        event, values = window.read()

        if(event == 'Registrar'):
            try:
                biblioteca.agregar_libro(Libro(values['ISBN'],values['Titulo'],values['Autor'],True))
                LayoutsPopUps.ExitoRegistro()
                window.close()
                break
            except ValueError as e: LayoutsPopUps.ErrorRegistro(e)

        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            window.close()
            break

def PL(biblioteca):
    window = sg.Window(title = 'Prestamo de Libro', keep_on_top = True, modal = True, layout = LayoutsRead.PL(), finalize = True)
    while True:
        event, values = window.read()

        if(event == 'Registrar'):
            try:
                biblioteca.prestar_libro(Prestamo(None, values['Rut'], values['ISBN'], None, None))
                LayoutsPopUps.ExitoRegistro()
                window.close()
                break
            except ValueError as e:
                LayoutsPopUps.ErrorRegistro(e)

        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            window.close()
            break

def EU(biblioteca):
    window = sg.Window(title = 'Eliminación de Usuario', keep_on_top = True, modal = True, layout = LayoutsRead.EU(), finalize = True)
    while True:
        event, values =  window.read()

        if(event == 'Eliminar'):
            try:
                biblioteca.eliminar_usuario(values['Rut'])
                LayoutsPopUps.Exito()
                window.close()
                break
            except ValueError as e: LayoutsPopUps.ErrorEliminacion(e)

        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            window.close()
            break

def EL(biblioteca):
    window = sg.Window(title = 'Eliminación de Libro', keep_on_top = True, modal = True, layout = LayoutsRead.EL(), finalize = True)
    while True:
        event, values = window.read()

        if(event == 'Eliminar'):
            try:
                biblioteca.eliminar_libro(values['ISBN'])
                LayoutsPopUps.ExitoEliminacion()
                window.close()
                break
            except ValueError as e: LayoutsPopUps.ErrorEliminacion(e)
        
        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            window.close()
            break

def DL(biblioteca):
    window = sg.Window(title = 'Devolución de Libro', keep_on_top = True, modal = True, layout = LayoutsRead.DL(), finalize = True)
    while True:
        event, values = window.read()

        if(event == 'Devolver'):
            try:
                biblioteca.devolver_libro(values['ISBN'], values['Rut'])
                LayoutsPopUps.ExitoRegistro()
                window.close()
                break
            except ValueError as e: LayoutsPopUps.ErrorRegistro(e)

        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            window.close()
            break