import speech_recognition as sr
import pyttsx3
import wave

device_index = 5 # Reemplaza con el índice de tu dispositivo

# Crear un objeto Recognizer
r = sr.Recognizer()

# Configurar el umbral de energía
r.energy_threshold = 50  # Valor fijo para el umbral de energía
r.dynamic_energy_threshold = False  # Deshabilitar el umbral dinámico

# Obtener audio del micrófono especificado
with sr.Microphone() as source:
    print(f"Usando el dispositivo de entrada: {device_index}")
    print("Ajustando el ruido ambiental...")
    r.adjust_for_ambient_noise(source, duration=2)
    print(f"Umbral de energía actual: {r.energy_threshold}")
    print("Di algo!")
    audio = r.listen(source)

# Guardar la pista de audio en un archivo WAV
with wave.open("output.wav", "wb") as f:
    f.setnchannels(1)
    f.setsampwidth(audio.sample_width)
    f.setframerate(audio.sample_rate)
    f.writeframes(audio.get_wav_data())

# Reconocer el habla usando Google Speech Recognition
try:
    print("Dijiste: " + r.recognize_google(audio, language="es-ES"))
except sr.UnknownValueError:
    print("No te pude entender")
except sr.RequestError as e:
    print(f"Error de solicitud; {e}")
except sr.WaitTimeoutError:
    print("Tiempo de espera agotado mientras se esperaba el audio")
except sr.AudioDataError:
    print("Error al procesar los datos de audio")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")