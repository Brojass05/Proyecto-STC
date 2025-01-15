import moviepy as mp
import os
import configparser
from conexion_ini import connIni

class RecorteVideo:
    def __init__(self):
        self.conn = connIni()
        self.config = self.conn.leer_ini()
        self.recortar_video()
    
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
            os.system(f'attrib +h "{ruta_video}"')
            print(f"Archivo '{ruta_video}' eliminado con éxito.")
        else:
            print(f"El archivo '{ruta_video}' no existe.")        