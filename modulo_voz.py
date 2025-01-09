import speech_recognition as sr


class ModuloVoz:
    def __init__(self):
        try:
            self.r = sr.Recognizer()
            self.r.energy_threshold = 50
            self.r.dynamic_energy_threshold = False
        except Exception as e:
            print(f"Error: {e}")

    def obtener_voz(self):
        with sr.Microphone() as source:
            #self.r.adjust_for_ambient_noise(source, duration=2)
            #self.reproducir_audio("Jarvis is listening to you.")
            print("Esperando entrada de voz...")
            audio = self.r.listen(source)
            text = self.r.recognize_google(audio, language="es-ES")
            print("Texto reconocido:", text)
            return text

    def reproducir_audio(self, mensaje):
        try:
            self.engine.say(mensaje)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error: {e}")