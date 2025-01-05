import speech_recognition as sr
import pyttsx3
import wave

class ModuloVoz:
    def __init__(self):
        print("Inicializando módulo de voz...")
        self.device_index = 5  # Reemplaza con el índice de tu dispositivo
        # Crear un objeto Recognizer
        self.r = sr.Recognizer()
        # Configurar el umbral de energía
        self.r.energy_threshold = 50  # Valor fijo para el umbral de energía
        self.r.dynamic_energy_threshold = False  # Deshabilitar el umbral dinámico
        # Inicializar el motor de pyttsx3
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
    def obtener_voz(self):
        # Obtener audio del micrófono especificado
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=2)
            self.reproducir_audio("Jarvis is listening to you.")
            print("Say something!")
            self.audio = self.r.listen(source)
            text = self.r.recognize_google(self.audio, language="es-ES")
        return text
        
            
    def reproducir_audio(self,mensaje):
        # Reconocer el habla usando Google Speech Recognition
        try:
            # Convertir texto a voz usando pyttsx3
            self.engine.say(mensaje)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error: {e}")

            
    
    