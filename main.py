import speech_recognition
import pyttsx3
import pyautogui

class main:
    def __init__(self):
        try:
            from modulo_voz import ModuloVoz
            self.voz = ModuloVoz()
            self.text = self.voz.obtener_voz()
            print("Dijiste: ", self.text)
            self.verificar_texto_voz()
            
        except Exception as e:
            print(f"Error: {e}")
            
    def verificar_texto_voz(self):
        from modulo_teclas import teclas
        teclas = teclas()
        self.text = self.text.lower()
        if self.text == "captura pantalla":
            teclas.capturar_pantalla()
        if self.text == "out saca clip":
            self.voz.reproducir_audio("outplayed sacando clip")
            teclas.sacar_clip_outplayed()
        
if __name__ == "__main__":
    main()
    print("Presiona 0 para salir\nPresiona 1 para reintentar")
    valor = int(input("Opción: "))
    while valor != 0:
        main()
        print("Presiona 0 para salir\nPresiona 1 para reintentar")
        valor = int(input("Opción: "))
        