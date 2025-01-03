from pyautogui import hotkey
# ejemplo
# pyautogui.hotkey('win', 'shift', 's', interval=0.5)
class teclas:
    def __init__(self):
        pass
    def sacar_clip(self):
        hotkey('ctrl', 'f3')
    