import FreeSimpleGUI as sg

class LayoutsMain:
    
    Ver = lambda: [
            [sg.Button('Ver Libros Registrados')],
            [sg.Button('Ver Usuarios Registrados')],
            [sg.Button('Ver Libros Prestados')],
            [sg.Button('Ver Historial de Prestamos')],
            [sg.Button('Consultar Ficha de Usuario')]   ]

    Acciones = lambda: [
            [sg.Button("Registrar Usuario")],
            [sg.Button("Registrar Libro")],
            [sg.Button("Prestar Libro")],
            [sg.Button("Eliminar Usuario")],
            [sg.Button("Eliminar Libro")],
            [sg.Button("Devolver Libro")]
    ]
    
    Configuracion = lambda: [
        [sg.Button('Conectarse a Base de Datos')],
        [sg.Button('Guardar Transacciones en Base de Datos')]
    ]


    Main = lambda: [  
            [sg.Text('Bienvenido al Gestor de Biblioteca')],

            [sg.TabGroup([
                [sg.Tab('Ver', layout = LayoutsMain.Ver()), 
                 sg.Tab('Acciones', layout = LayoutsMain.Acciones()),
                 sg.Tab('Configuracion', layout = LayoutsMain.Configuracion())]])],
            
            [sg.Button('Cerrar')]   
            ]