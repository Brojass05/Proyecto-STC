import speech_recognition as sr
import pyttsx3
import time
import sys
import logging

class ModuloVoz:
    def __init__(self):
        try:
            self.device_index = 5
            self.r = sr.Recognizer()
            self.engine = pyttsx3.init()
            self.mic = sr.Microphone(device_index=self.device_index)
            
            # Configure logging
            logging.basicConfig(filename='voice_module.log', level=logging.INFO)
            
            # Adjust for ambient noise once at startup
            with self.mic as source:
                print("Ajustando ruido ambiental...")
                self.r.adjust_for_ambient_noise(source, duration=2)
                print(f"Umbral: {self.r.energy_threshold}")
        except Exception as e:
            logging.error(f"Error en inicialización: {e}")
            sys.exit(1)

    def callback(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            logging.info(f"Audio detectado exitosamente: {text}")
            print(f"Detectado: {text}")
            
            # Add debug info for TTS
            logging.info("Intentando reproducir audio...")
            self.engine.say(text)
            self.engine.runAndWait()
            logging.info("Audio reproducido exitosamente")
            
        except sr.UnknownValueError:
            logging.warning("No se pudo entender el audio")
            print("No te pude entender")
        except sr.RequestError as e:
            logging.error(f"Error en la solicitud a Google: {e}")
            print(f"Error de solicitud: {e}")
        except Exception as e:
            logging.error(f"Error inesperado en callback: {str(e)}")
            print(f"Error: {e}")

    def start_listening(self):
        try:
            print("Iniciando escucha en segundo plano...")
            return self.r.listen_in_background(self.mic, self.callback)
        except Exception as e:
            logging.error(f"Error al iniciar escucha: {e}")
            return None

if __name__ == "__main__":
    try:
        voz = ModuloVoz()
        stop_function = voz.start_listening()
        
        if stop_function is None:
            print("Error al iniciar la escucha")
            sys.exit(1)
            
        print("Escuchando... Presiona Ctrl+C para detener")
        
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        if stop_function:
            stop_function(wait_for_stop=True)
        print("\nPrograma detenido")
    except Exception as e:
        logging.error(f"Error general: {e}")
        if stop_function:
            stop_function(wait_for_stop=True)
    finally:
        sys.exit(0)