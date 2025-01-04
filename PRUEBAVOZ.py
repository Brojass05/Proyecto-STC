import pyaudio

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Listar todos los dispositivos de audio disponibles
print("Dispositivos de audio disponibles:")
for i in range(p.get_device_count()):
    try:
        device_info = p.get_device_info_by_index(i)
        print(f"Device {i}: {device_info['name']}")
        print(f"  Max Input Channels: {device_info['maxInputChannels']}")
        print(f"  Max Output Channels: {device_info['maxOutputChannels']}")
    except Exception as e:
        print(f"Error al obtener información del dispositivo {i}: {e}")

# Limpiar PyAudio
p.terminate()