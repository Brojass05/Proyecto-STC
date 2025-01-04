import speech_recognition as sr
import pyaudio

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Obtener la lista de micrófonos disponibles
mic_list = sr.Microphone.list_microphone_names()

# Imprimir la lista de micrófonos
print("Dispositivos de entrada disponibles:")
for i, mic in enumerate(mic_list):
    print(f"Microphone {i}: {mic}")

# Filtrar y seleccionar los micrófonos que funcionan
working_mics = []
for i, mic in enumerate(mic_list):
    try:
        with sr.Microphone(device_index=i) as source:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source, duration=1)
            print(f"Microphone {i} ({mic}) is working")
            working_mics.append(i)
    except Exception as e:
        print(f"Microphone {i} ({mic}) is not working: {e}")

if working_mics:
    print(f"Working Microphones: {working_mics}")
    selected_mic_index = working_mics[0]  # Seleccionar el primer micrófono que funciona
    print(f"Selected Microphone {selected_mic_index}: {mic_list[selected_mic_index]}")
else:
    print("No suitable microphone found")

# Limpiar PyAudio
p.terminate()