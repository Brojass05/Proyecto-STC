import speech_recognition as sr

index_device = 0  # Reemplaza con el índice de tu dispositivo

# Crear un objeto Recognizer
r = sr.Recognizer()

# Obtener audio del micrófono especificado
with sr.Microphone(device_index=index_device) as source:
    print(f"Usando el dispositivo de entrada: {index_device}")
    print("Di algo!")
    audio = r.listen(source)

# Reconocer el habla usando Sphinx
try:
    print("Dijiste: " + r.recognize_sphinx(audio, language="es-ES"))
except sr.UnknownValueError:
    print("No te pude entender")
except sr.RequestError as e:
    print("Error; {0}".format(e))