import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
from RW.dbload import *
import FreeSimpleGUI as sg
import os
import sys
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
load(biblioteca)

# Create the Window
window = sg.Window('Gestor Biblioteca', layout = LayoutsMain.Main(), icon=icon_path)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if(event == 'Ver Libros Registrados'):
        window2 = sg.Window(title='Libros Registrados', keep_on_top = True, modal = True, layout = LayoutsView.VLD(biblioteca), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'): 
                window2.close()
                break

    if(event == 'Ver Usuarios Registrados'):
        window2 = sg.Window(title = 'Usuarios Registrados', keep_on_top = True, modal = True, layout = LayoutsView.VUR(biblioteca), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'): 
                window2.close()
                break

    if(event == 'Ver Libros Prestados'):
        window2 = sg.Window(title = 'Libros Prestados', keep_on_top = True, modal = True, layout = LayoutsView.VPA(biblioteca), finalize = True)
        while True: 
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'):
                window2.close()
                break

    if(event == 'Ver Historial de Prestamos'):
        window2 = sg.Window(title = 'Historial de Prestamos', keep_on_top = True, modal = True, layout = LayoutsView.VHP(biblioteca), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'):
                window2.close()
                break

    if(event == 'Consultar Ficha de Usuario'):
        window2 = sg.Window(size = (480,360),title = 'Consulta Ficha de Usuario', keep_on_top = True, modal = True, layout = LayoutsView.CFU(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Buscar'):
                try:
                    usuario = biblioteca.usuarios[values2['Rut']]
                    window2['Datos_Usuario'].update(values = [usuario.__str__()])
                except Exception as e:  window2['Datos_Usuario'].update(values = [f'Rut {e} Inexistente'])

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'):
                window2.close()
                break
    
    if(event == 'Registrar Usuario'):
        window2 = sg.Window(title = 'Registro Usuario Nuevo', keep_on_top = True, modal = True, layout = LayoutsRead.RU(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Registrar'):
                try:
                    biblioteca.registrar_usuario(Usuario(values2['Rut'], values2['Nombre']))
                    LayoutsPopUps.ExitoRegistro()
                    window2.close()
                    break
                except ValueError as e: LayoutsPopUps.ErrorRegistro(e)
            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break 

    if(event == 'Registrar Libro'):
        window2 = sg.Window(title = 'Registro Libro Nuevo', keep_on_top = True, modal = True, layout = LayoutsRead.RL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Registrar'):
                try:
                    biblioteca.agregar_libro(Libro(values2['ISBN'],values2['Titulo'],values2['Autor'],True))
                    LayoutsPopUps.ExitoRegistro()
                    window2.close()
                    break
                except ValueError as e: LayoutsPopUps.ErrorRegistro(e)

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break
    
    if(event == 'Prestar Libro'):
        window2 = sg.Window(title = 'Prestamo de Libro', keep_on_top = True, modal = True, layout = LayoutsRead.PL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Registrar'):
                try:
                    biblioteca.prestar_libro(Prestamo(None, values2['Rut'], values2['ISBN'], None, None))
                    LayoutsPopUps.ExitoRegistro()
                    window2.close()
                    break
                except ValueError as e:
                    LayoutsPopUps.ErrorRegistro(e)

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break

    if(event == 'Eliminar Usuario'):
        window2 = sg.Window(title = 'Eliminación de Usuario', keep_on_top = True, modal = True, layout = LayoutsRead.EU(), finalize = True)
        while True:
            event2, values2 =  window2.read()

            if(event2 == 'Eliminar'):
                try:
                    biblioteca.eliminar_usuario(values2['Rut'])
                    LayoutsPopUps.Exito()
                    window2.close()
                    break
                except ValueError as e: LayoutsPopUps.ErrorEliminacion(e)

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break
    
    if(event == 'Eliminar Libro'):
        window2 = sg.Window(title = 'Eliminación de Libro', keep_on_top = True, modal = True, layout = LayoutsRead.EL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Eliminar'):
                try:
                    biblioteca.eliminar_libro(values2['ISBN'])
                    LayoutsPopUps.ExitoEliminacion()
                    window2.close()
                    break
                except ValueError as e: LayoutsPopUps.ErrorEliminacion(e)
        
            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break

    if(event == 'Devolver Libro'):
        window2 = sg.Window(title = 'Devolución de Libro', keep_on_top = True, modal = True, layout = LayoutsRead.DL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Devolver'):
                try:
                    biblioteca.devolver_libro(values2['ISBN'], values2['Rut'])
                    LayoutsPopUps.ExitoRegistro()
                    window2.close()
                    break
                except ValueError as e: LayoutsPopUps.ErrorRegistro(e)

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break

    if (event == sg.WIN_CLOSED or event == 'Cerrar'):
        save(biblioteca)
        print("¡Hasta luego!")
        break
window.close()