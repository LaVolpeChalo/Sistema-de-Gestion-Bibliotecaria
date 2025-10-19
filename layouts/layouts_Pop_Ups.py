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