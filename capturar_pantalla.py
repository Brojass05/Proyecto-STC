from time import sleep
import cv2
import configparser
from PIL import ImageGrab
import numpy as np
import screeninfo as sc
import os


# video enconding
class VideoEncoding:
    def __init__(self):
        self.crear_carpeta()
        self.runing = True
        self.config = configparser.ConfigParser()
        self.config_file = "config.ini"
        self.leer_ini()
        
    def leer_ini(self):
        # Leer archivo INI o crear un archivo de configuración predeterminado si no existe
        try:
            self.config.read(self.config_file)
            if "status" not in self.config:
                self.config["status"] = {"verGrabacion": "0"}  # Valor por defecto
                self.guardar_ini()
        except Exception as e:
            print(f"Error leyendo el archivo INI: {e}")
        
    def capturar_pantalla(self):
        monitor_principal = None
        ver_cuadro = self.config["status"].getint("verGrabacion")
        for m in sc.get_monitors():
            if m.x == 0 and m.y == 0:  # Monitor principal
                monitor_principal = m
                break
            
        if monitor_principal:
            fps = self.config["status"].getfloat("fps")
            bbox = (monitor_principal.x, monitor_principal.y, 
                    monitor_principal.x + monitor_principal.width, 
                    monitor_principal.y + monitor_principal.height)  
            fourccc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
            captura = cv2.VideoWriter("videos/captura1.mp4", fourccc, fps, (1920, 1080))

            while self.runing:
                img = ImageGrab.grab(bbox=bbox)
                np_img = np.array(img)
                cvt_image = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
                # mostrar una ventana con la captura de pantalla
                if ver_cuadro:
                    cv2.imshow("Captura de pantalla", cvt_image)
                captura.write(cvt_image)
                if cv2.waitKey(1) == 27:
                    break
            captura.release()
            cv2.destroyAllWindows()
    
    def  cerrar_captura(self):
        self.runing = False

    def crear_carpeta(self):
        try:
            ruta_carpeta = "videos"
            os.makedirs(ruta_carpeta)
        except FileExistsError:
            print(f"La carpeta '{ruta_carpeta}' ya existe.")
        except PermissionError:
            print("No tienes permisos para crear la carpeta.")
            
            
vid=VideoEncoding()
vid.capturar_pantalla()



    
