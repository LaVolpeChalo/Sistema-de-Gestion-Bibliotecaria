import FreeSimpleGUI as sg

class LayoutsPopUps:
    
    ExitoEliminacion = lambda : sg.popup(
        auto_close = 5,
        keep_on_top = True,
        modal = True,
        button_color = ('Black', 'Green'),
        custom_text = f'Eliminación Exitosa')
    
    ExitoRegistro = lambda : sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Green'), 
        custom_text = f'Registro Exitoso')
    
    ExitoConexion = lambda : sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Green'), 
        custom_text = f'Conexion Exitosa!!')
    
    ErrorEliminacion = lambda e : sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Red'), 
        custom_text = f'Falló eliminación: {e}') 
    
    ErrorRegistro = lambda e: sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Red'), 
        custom_text = f'Falló registro: {e}')
    
    ErrorConexion = lambda e: sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Red'), 
        custom_text = f'Falló Conexión: {e}')
    
    CierrePrograma = lambda: sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Green'), 
        custom_text = 'Hasta Luego')

    Nulldbkey = lambda: sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Red'), 
        custom_text = 'Error: dbkey nula')
    
    FalloGuardado = lambda e: sg.popup(
        auto_close = 5, 
        keep_on_top = True, 
        modal = True, 
        button_color = ('Black', 'Red'), 
        custom_text = 'Error: no se pudo establecer conexion')