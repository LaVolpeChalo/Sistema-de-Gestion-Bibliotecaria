import FreeSimpleGUI as sg
from Objects.O_Libro import Libro
from Objects.O_Biblioteca import Biblioteca
from Objects.O_Usuario import Usuario
from Objects.O_Prestamo import Prestamo
from RW.dbload import *
import FreeSimpleGUI as sg
import os
import sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)


icon_path = resource_path('src/Icon.ico')
sg.theme('Green Mono')
biblioteca = Biblioteca()
load(biblioteca)

# All the stuff inside your window.
tab_layout1 = [
            [sg.Button('Ver Libros Registrados')],
            [sg.Button('Ver Usuarios Registrados')],
            [sg.Button('Ver Libros Prestados')],
            [sg.Button('Ver Historial de Prestamos')],
            [sg.Button('Consultar Ficha de Usuario')]   ]

tab_layout2 = [
            [sg.Button("Registrar Usuario")],
            [sg.Button("Registrar Libro")],
            [sg.Button("Prestar Libro")],
            [sg.Button("Eliminar Usuario")],
            [sg.Button("Eliminar Libro")],
            [sg.Button("Devolver Libro")]
]

# Layouts de Funciones
VLD = lambda: [ #Ver Libros Disponibles
        [sg.Table(values=biblioteca.mostrar_libros_registrados() ,
                         

        headings = ['Titulo', 'Autor', 'ISBN', 'Estado'])],
        
        [sg.Button('Cerrar')]   ]

VUR = lambda: [ #Ver Usuarios Registrados
        [sg.Table(values=biblioteca.mostrar_usuarios() ,
                  
        headings = ['Rut Usuario', 'Nombre', 'Libros Arrendados'])],

        [sg.Button('Cerrar')]   ]

VPA = lambda: [ #Ver Prestamos Activos
        [sg.Table(values=biblioteca.mostrar_libros_arrendados(),

        headings = ['Titulo', 'Autor', 'ISBN', 'Estado'])],

        [sg.Button('Cerrar')]   ]

VHP = lambda: [#Historial de Prestamos
    [sg.Table(values=biblioteca.mostrar_prestamos(),

    headings = ['ID', 'Rut Usuario', 'ISBN Libro', 'Fecha Prestamo', 'Fecha Devolución'])],

    [sg.Button('Cerrar')]   ]

CFU = lambda: [#Consultar Ficha Usuario
    [sg.Text('Rut Usuario')],
    [sg.Input(default_text = 'Ej:12.345.678-9', key = 'Rut')],
    [sg.Button('Buscar')],
    [sg.Table(values = [], headings = ['ID Usuario', 'Nombre', 'Libros Arrendados'], key = 'Datos_Usuario')],
    [sg.Button('Cerrar')]   ]

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
    [sg.Input(default_text = '12.345.678-9', key = 'Rut')],
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

layout = [  
            [sg.Text('Bienvenido al Gestor de Biblioteca')],

            [sg.TabGroup([[sg.Tab('Ver', tab_layout1), sg.Tab('Acciones', tab_layout2)]])],

            [sg.Button('Cerrar')]   ]


# Create the Window
window = sg.Window('Gestor Biblioteca', layout, icon=icon_path)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if(event == 'Ver Libros Registrados'):
        window2 = sg.Window(title='Libros Registrados', keep_on_top = True, modal = True, layout = VLD(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'): 
                window2.close()
                break

    if(event == 'Ver Usuarios Registrados'):
        window2 = sg.Window(title = 'Usuarios Registrados', keep_on_top = True, modal = True, layout = VUR(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'): 
                window2.close()
                break

    if(event == 'Ver Libros Prestados'):
        window2 = sg.Window(title = 'Libros Prestados', keep_on_top = True, modal = True, layout = VPA(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'):
                window2.close()
                break

    if(event == 'Ver Historial de Prestamos'):
        window2 = sg.Window(title = 'Historial de Prestamos', keep_on_top = True, modal = True, layout = VHP(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'):
                window2.close()
                break

    if(event == 'Consultar Ficha de Usuario'):
        window2 = sg.Window(size = (480,360),title = 'Consulta Ficha de Usuario', keep_on_top = True, modal = True, layout = CFU(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Buscar'):
                try:
                    id_usuario = values2['Rut']
                
                    usuario = biblioteca.usuarios[id_usuario]

                    window2['Datos_Usuario'].update(values = [usuario.__str__()])

                except Exception as e:
                    window2['Datos_Usuario'].update(values = [f'Rut {e} Inexistente'])

            if(event2 == sg.WIN_CLOSED or event2 == 'Cerrar'):
                window2.close()
                break
    
    if(event == 'Registrar Usuario'):
        window2 = sg.Window(title = 'Registro Usuario Nuevo', keep_on_top = True, modal = True, layout = RU(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Registrar'):
                try:
                    us = Usuario(values2['Rut'], values2['Nombre'])
                    biblioteca.registrar_usuario(us)
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color =('Black','Green'), custom_text = f'Registro Exitoso')
                    window2.close()
                    break
                except ValueError as e:
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black','Red'), custom_text = f'Falló registro: {e}')    

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break 

    if(event == 'Registrar Libro'):
        window2 = sg.Window(title = 'Registro Libro Nuevo', keep_on_top = True, modal = True, layout = RL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Registrar'):
                try:
                    us = Libro(values2['ISBN'],values2['Titulo'],values2['Autor'],True)
                    biblioteca.agregar_libro(us)
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black','Green'), custom_text = f'Registro Exitoso')
                    window2.close()
                    break
                except ValueError as e:
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Red'), custom_text = f'Falló registro: {e}')

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break
    
    if(event == 'Prestar Libro'):
        window2 = sg.Window(title = 'Prestamo de Libro', keep_on_top = True, modal = True, layout = PL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Registrar'):
                try:
                    prestamo = Prestamo(None, values2['Rut'], values2['ISBN'], None, None)
                    biblioteca.prestar_libro(prestamo)
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Green'), custom_text = f'Registro Exitoso')
                    window2.close()
                    break
                except ValueError as e:
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Red'), custom_text = f'Falló registro: {e}')

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break

    if(event == 'Eliminar Usuario'):
        window2 = sg.Window(title = 'Eliminación de Usuario', keep_on_top = True, modal = True, layout = EU(), finalize = True)
        while True:
            event2, values2 =  window2.read()

            if(event2 == 'Eliminar'):
                try:
                    biblioteca.eliminar_usuario(values2['Rut'])
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Green'), custom_text = f'Eliminación Exitosa')
                    window2.close()
                    break
                except ValueError as e:
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Red'), custom_text = f'Falló eliminación: {e}')

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break
    
    if(event == 'Eliminar Libro'):
        window2 = sg.Window(title = 'Eliminación de Libro', keep_on_top = True, modal = True, layout = EL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Eliminar'):
                try:
                    biblioteca.eliminar_libro(values2['ISBN'])
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Green'), custom_text = f'Eliminación Exitosa')
                    window2.close()
                    break
                except ValueError as e:
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Red'), custom_text = f'Falló eliminación: {e}')
        

            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break

    if(event == 'Devolver Libro'):
        window2 = sg.Window(title = 'Devolución de Libro', keep_on_top = True, modal = True, layout = DL(), finalize = True)
        while True:
            event2, values2 = window2.read()

            if(event2 == 'Devolver'):
                try:
                    biblioteca.devolver_libro(values2['ISBN'], values2['Rut'])
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Green'), custom_text = f'Devolución Exitosa')
                    window2.close()
                    break
                except ValueError as e:
                    sg.popup(auto_close = 5, keep_on_top = True, modal = True, button_color = ('Black', 'Red'), custom_text = f'Falló eliminación: {e}')


            if(event2 == sg.WIN_CLOSED or event2 == 'Cancelar'):
                window2.close()
                break



    # if user closes window or clicks cancel
    if (event == sg.WIN_CLOSED or event == 'Cerrar'):
        save(biblioteca)
        print("¡Hasta luego!")
        break

    print('You entered ', values[0])

window.close()