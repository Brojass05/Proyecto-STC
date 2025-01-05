from pyautogui import hotkey
import pyttsx3
# ejemplo
# pyautogui.hotkey('win', 'shift', 's', interval=0.5)
class teclas:
    def __init__(self):
        pass
        
    def hablar(self,mensaje):
        try:
            self.engine.say(mensaje)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error en el motor de texto a voz: {e}")
        
    def sacar_clip_outplayed(self):
        #self.hablar("Taking clip")
        try:
            hotkey('ctrl', 'f3',interval=0.1)
        except Exception as e:
            print(f"Error en la combinación de teclas: {e}")
            
    def sacar_clip_xbox(self):
        #self.hablar("Taking clip")
        try:
            hotkey('win', 'alt', 'g', interval=0.1)
            print("Xbox esta sacando clip")
        except Exception as e:
            print(f"Error en la combinación de teclas: {e}")
            
    def capturar_pantalla(self):
        #self.hablar("Taking screenshot")
        try:
            hotkey('win', 'shift', 's')
            print("Capturando pantalla")
        except Exception as e:
            print(f"Error en la combinación de teclas: {e}")
    
    