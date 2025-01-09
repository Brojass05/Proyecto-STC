import moviepy as mp
import os

class RecorteVideo:
    def __init__(self):
        self.recortar_video()
    def recortar_video(self):
        
        ruta_video = "videos/captura1.mp4"
        video=mp.VideoFileClip(ruta_video)
        #recortar los ultimos 10 segundos
        start_time=video.duration - 10
        video_recortado=video.subclipped(start_time, video.duration)
        video_recortado.write_videofile("videos/clip.mp4")
        self.borrar_video_original(ruta_video)
        
        
    def borrar_video_original(self,ruta_video):
        
        if os.path.exists(ruta_video):
            os.remove(ruta_video)
            print(f"Archivo '{ruta_video}' eliminado con éxito.")
        else:
            print(f"El archivo '{ruta_video}' no existe.")        