import speech_recognition as sr
import pyttsx3
import logging
from main import Main

class EscuchaPorDebajo:
    def __init__(self):
        self.recognized_text = None
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        # Ajustar el ruido ambiental
        with self.m as source:
            print("Ajustando ruido ambiental... por favor, espera.")
            self.r.adjust_for_ambient_noise(source, duration=2)
            print(f"Umbral ajustado a: {self.r.energy_threshold}")

    def callback(self, recognizer, audio):
        try:
            self.recognized_text = str(recognizer.recognize_google(audio, language="es-ES")).lower()
            print(f"\nDijiste: {self.recognized_text}")
            indice1 = self.recognized_text.find("jarvis")
            texto1 = self.recognized_text[indice1:]
            indice = texto1.find(" ")
            texto_jarvis = texto1[:indice]
            comando_jarvis = texto1[indice:].strip()
            
            if texto_jarvis in ["jarvis","yarbis","yarbiss","yarvis","yarviss","yarbis","yarbiss","yarviss"]:
                # Create new instance without background listening
                if hasattr(self, 'stop_listening'):
                    self.stop_listening(wait_for_stop=False)
                    delattr(self, 'stop_listening')
                
                # Execute main flow
                main = Main()
                main.verificar_texto_voz(comando_jarvis)
                
                # Start new background listening with fresh context
                self.m = sr.Microphone()
                self.iniciar_escucha()
                
        except sr.UnknownValueError:
            print(".", end="", flush=True)
        except sr.RequestError as e:
            print(f"\nError de conexión: {e}")
        except Exception as e:
            print(f"\nError: {e}")
    
    def iniciar_escucha(self):
        print("\nIniciando escucha en segundo plano...")
        self.stop_listening = self.r.listen_in_background(self.m, self.callback)

    def detener_escucha(self):
        if self.stop_listening:
            self.stop_listening(wait_for_stop=False)
            print("Escucha en segundo plano detenida.")
            
if __name__ == "__main__":
    try:
        escucha = EscuchaPorDebajo()
        escucha.iniciar_escucha()
        input("Presiona Enter para detener la escucha.\n")
        escucha.detener_escucha()
    except Exception as e:
        print(f"Error en el módulo principal: {e}")
            