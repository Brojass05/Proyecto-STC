import speech_recognition as sr

# Obtener la lista de micrófonos disponibles
mic_list = sr.Microphone.list_microphone_names()

# Imprimir la lista de micrófonos
for i, mic in enumerate(mic_list):
    print(f"Microphone {i}: {mic}")

# Probar con diferentes índices de dispositivos
for i in range(len(mic_list)):
    try:
        with sr.Microphone(device_index=i) as source:
            print(f"Microphone {i} is working")
    except OSError as e:
        print(f"Microphone {i} is not working: {e}")