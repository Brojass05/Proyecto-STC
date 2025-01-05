import time
import speech_recognition as sr
import pyttsx3

class EscuchaPorDebajo:
    def __init__(self):
        print("Inicializando escucha por debajo...")
        self.recognized_text = None
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()


    def callback(self,recognizer, audio):
        from main import Main
        try:
            # Reconocer el audio usando Google Speech Recognition
            self.recognized_text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Dijiste: {self.recognized_text}")
            # Aquí podrías añadir lógica adicional, como comandos de voz específicos
            if self.recognized_text == "jarvis":
                Main()
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError as e:
            print(f"Error al conectarse con el servicio de reconocimiento: {e}")
        except Exception as e:
            print(f"Error: {e}")
        

    def hablar(self,mensaje):
        try:
            self.engine.say(mensaje)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error en el motor de texto a voz: {e}")


    def iniciar_escucha(self):
        # Configuración del reconocedor y micrófono
        
        # Ajustar el ruido ambiental
        with self.m as source:
            print("Ajustando ruido ambiental... por favor, espera.")
            self.r.adjust_for_ambient_noise(source, duration=2)
            self.hablar("Listo para escuchar. Di algo...")

        # Iniciar escucha en segundo plano
        stop_listening = self.r.listen_in_background(self.m, self.callback)

        print("Escuchando continuamente... Presiona Ctrl+C para detener.")

        try:
            # Mantener el programa corriendo hasta que se interrumpa manualmente
            while True:
                time.sleep(0.1)  # Mantener el hilo principal activo
        except KeyboardInterrupt:
            # Detener la escucha cuando se presiona Ctrl+C
            print("Deteniendo escucha...")
            stop_listening(wait_for_stop=False)
            print("Programa finalizado.")

