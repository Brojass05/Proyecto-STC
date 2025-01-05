import speech_recognition
import pyttsx3
import pyautogui

class Main:
    def __init__(self):
        print("Inicializando Main...")
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.flujo_principal()
        
        
    def flujo_principal(self):
        try:
            from modulo_voz import ModuloVoz
            
            self.hablar()
            self.voz = ModuloVoz()
            self.text = self.voz.obtener_voz()
            print("Dijiste: ", self.text)
            self.verificar_texto_voz()
            
        except Exception as e:
            print(f"Error const. Main: {e}")

        
    def hablar(self):
        try:
            self.engine.say("Jarvis is listening to you.")
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error main_hablar: {e}")    
            
    def verificar_texto_voz(self):
        from modulo_teclas import teclas
        teclas = teclas()
        self.text = self.text.lower()
        if self.text == "captura pantalla" or self.text == "capturar pantalla" or self.text == "captura de pantalla" or self.text == "saca captura" or self.text == "sacar captura":
            teclas.capturar_pantalla()
        if self.text == "out saca clip":
            self.voz.reproducir_audio("outplayed sacando clip")
            teclas.sacar_clip_outplayed()
        else:
            print("No se reconoció el comando.")

            

        