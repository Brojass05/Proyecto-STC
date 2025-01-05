from pyautogui import hotkey
# ejemplo
# pyautogui.hotkey('win', 'shift', 's', interval=0.5)
class teclas:
    def __init__(self):
        pass
    
    def sacar_clip_outplayed(self):
        hotkey('ctrl', 'f3')
        
    def capturar_pantalla(self):
        hotkey('win', 'shift', 's')