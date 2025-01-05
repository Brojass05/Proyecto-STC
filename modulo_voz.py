import speech_recognition as sr
import pyttsx3
import wave

class ModuloVoz:
    def __init__(self):
        self.device_index = 5  # Reemplaza con el índice de tu dispositivo
        # Crear un objeto Recognizer
        self.r = sr.Recognizer()
        # Configurar el umbral de energía
        self.r.energy_threshold = 50  # Valor fijo para el umbral de energía
        self.r.dynamic_energy_threshold = False  # Deshabilitar el umbral dinámico
        # Inicializar el motor de pyttsx3
        self.engine = pyttsx3.init()
        
    def obtener_voz(self):
        # Obtener audio del micrófono especificado
        with sr.Microphone() as source:
            print(f"Usando el dispositivo de entrada: {self.device_index}")
            print("Ajustando el ruido ambiental...")
            self.r.adjust_for_ambient_noise(source, duration=2)
            print(f"Umbral de energía actual: {self.r.energy_threshold}")
            print("Di algo!")
            self.audio = self.r.listen(source)
            text = self.r.recognize_google(self.audio, language="es-ES")
        return text
        
            
    def reproducir_audio(self,text):
        # Reconocer el habla usando Google Speech Recognition
        try:
            # Convertir texto a voz usando pyttsx3
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error: {e}")

            
    
    