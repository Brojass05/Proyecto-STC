import moviepy as mp
import os
import configparser

class RecorteVideo:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = "config.ini"
        self.leer_ini()
        self.recortar_video()
        
    def leer_ini(self):
        # Leer archivo INI o crear un archivo de configuración predeterminado si no existe
        try:
            self.config.read(self.config_file)
            if "status" not in self.config:
                self.config["status"] = {
                    "verGrabacion": "0",
                    "fps":"15",
                    "monitorIndex": "0",
                    "resolutionIndex": "0",
                    "noiseUmbral": "4",
                    "languageRec": "es-ES",
                    "clipLength": "10"
                    }  # Valores por defecto
                self.guardar_ini()
        except Exception as e:
            print(f"Error leyendo el archivo INI: {e}")
    
    
    def recortar_video(self):
        duracion_video = self.config["status"].getint("clipLength")
        otptIndex = self.config["status"].getint("indexFormat")
        ruta_video = "videos/captura1.mp4"
        video=mp.VideoFileClip(ruta_video)
        #recortar los ultimos 10 segundos
        start_time=video.duration - int(duracion_video)
        video_recortado=video.subclipped(start_time, video.duration)
        if otptIndex == 0:
            video_recortado.write_videofile("videos/clip.mp4", codec="libx264")
        elif otptIndex == 1:
            video_recortado.write_videofile("videos/clip.avi", codec="png")
        elif otptIndex == 2:
            video_recortado.write_videofile("output.mov", codec="libx264")  # Exportar a MOV
        elif otptIndex == 3:
            video_recortado.write_videofile("output.webm", codec="libvpx")  # Exportar a WebM
        
        
        self.borrar_video_original(ruta_video)
        
        
    def borrar_video_original(self,ruta_video):
        
        if os.path.exists(ruta_video):
            os.remove(ruta_video)
            print(f"Archivo '{ruta_video}' eliminado con éxito.")
        else:
            print(f"El archivo '{ruta_video}' no existe.")        