import logging
from modulo_voz import ModuloVoz
from modulo_teclas import teclas
from capturar_pantalla import VideoEncoding

class Main:
    def __init__(self):
        from escucha_por_debajo import EscuchaPorDebajo
        
        self.voz = ModuloVoz()  # Inicializar ModuloVoz correctamente
        escucha = EscuchaPorDebajo()
        
        

    def flujo_principal(self):
        try:
            self.text = self.voz.obtener_voz()
            print("Texto obtenido:", self.text)
            self.verificar_texto_voz()
        except Exception as e:
            print(f"Error en flujo_principal: {e}")
            raise  # Re-raise the exception for debugging

    def verificar_texto_voz(self,texto):
        try:
            teclas_instance = teclas()
            self.text = texto
            if self.text.lower() in ["captura pantalla", "capturar pantalla", "captura de pantalla", "saca captura", "sacar captura","captura la pantalla"]:
                teclas_instance.capturar_pantalla()
            elif self.text.lower() == "out saca clip":
                #self.voz.reproducir_audio("outplayed sacando clip")
                teclas_instance.sacar_clip_outplayed()
            elif self.text.lower() == "xbox":
                #self.voz.reproducir_audio("xbox sacando clip")
                teclas_instance.sacar_clip_xbox()
            elif self.text.lower() == "clip":
                from recortar_vid import RecorteVideo
                RecorteVideo()
            else:
                print("No se reconoció el comando.")
        except Exception as e:
            print(f"Error en verificar_texto_voz: {e}")

