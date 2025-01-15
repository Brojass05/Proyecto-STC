import screeninfo as sc
import os
import tkinter as tk
import configparser
from tkinter import ttk, messagebox,filedialog
from pathlib import Path

class Gui:
    def __init__(self):
        from conexion_ini import connIni
        self.base = tk.Tk()
        self.vistaPrevia = tk.IntVar()  # IntVar para manejar el estado del Checkbutton
        self.fps = 0
        self.vid_length = 0
        self.indexFormat = 0
        self.monitores = []
        self.lang = ""
        self.grabarPantalla = tk.IntVar()
        self.guardarGrab = tk.IntVar()
        self.base.title("Configuración Clips")
        
        
        self.conn = connIni()
        self.config = self.conn.leer_ini()
        self.get_start_status()  # Establecer el estado inicial del Checkbutton
        
        
        self.crear_formulario()  # Crear el formulario de la GUI
        self.base.geometry("350x350")  # Definir tamaño de la ventana
        self.base.mainloop()  # Iniciar el bucle principal de la GUI
    

    
    def crear_formulario(self):
        # Crear Checkbutton
        ttk.Label(self.base,text="Vista previa").grid(column=0,row=1)
        chk = ttk.Checkbutton(self.base, variable=self.vistaPrevia)
        chk.grid(column=1, row=1,pady=10)
        
        
        ttk.Label(self.base,text="Grabar pantalla",justify="right").grid(column=0,row=2,pady=10)
        chkRec = ttk.Checkbutton(self.base,variable=self.grabarPantalla)
        chkRec.grid(column=1,row=2)
        
        ttk.Label(self.base,text="Guardar grabacion",justify="right").grid(column=0,row=3,pady=10)
        chkSave = ttk.Checkbutton(self.base,variable=self.guardarGrab)
        chkSave.grid(column=1,row=3)
        
        # Crear Spinbox de ejemplo
        ttk.Label(self.base,text="FPS",justify="right").grid(column=0,row=4,pady=10)
        self.spinFps = ttk.Spinbox(self.base, from_=0, to=60,justify="left",increment=5)
        self.spinFps.grid(column=1, row=4,pady=10)
        self.spinFps.set(self.fps)
        
        ttk.Label(self.base,text="Duración",justify="right").grid(column=0,row=5,pady=10)
        self.length = ttk.Spinbox(self.base,from_=5,to=60,increment=5)
        self.length.grid(column=1,row=5)
        self.length.set(self.vid_length)
        
        ttk.Label(self.base,text="Formato de salida",justify="right").grid(column=0,row=6,pady=10)
        self.format = ttk.Combobox(self.base,values=["mp4","avi","mov","webm"],state="readonly")
        self.format.current(self.indexFormat)
        self.format.grid(column=1,row=6)
        
        ttk.Label(self.base,text="Lenguaje de reconocimiento",justify="right").grid(column=0,row=7,pady=10)
        self.leng = ttk.Combobox(self.base, values=["es-ES","en-US","es-MX","fr-FR","de-DE","it-IT","pt-PT","zh-CN","ja-JP","ko-KR","ar-SA","ru-RU","hi-IN"],state="readonly")
        self.leng.set(self.lang)
        self.leng.grid(column=1,row=7) 
                  
        ttk.Button(self.base,text="Abrir carpeta contenedora",command=self.abrir_carpeta).grid(column=0,row=10)
        ttk.Button(self.base,text="Guardar Configuracion",command=self.save_status).grid(column=0,row=11)
        
    def abrir_carpeta(self):
        try:
            vid_path = Path("videos").absolute()
            filedialog.askdirectory(title="Carpeta",initialdir=vid_path)
            
            
        except Exception as e:
            messagebox.showerror("Error al abrir la carpeta",f"Eror: {e}")

    def save_status(self):
        # Obtener el estado actual del Checkbutton
        estado: str = self.vistaPrevia.get()
        fps: str = self.spinFps.get()
        length: str = self.length.get()
        iFormat: str = self.format.current()
        lang: str = self.leng.get()
        grabarPantalla: str = self.grabarPantalla.get()
        guardarGrabacion = self.guardarGrab.get()
        # Guardar el nuevo estado en el archivo INI
        self.config["status"]["verGrabacion"] = str(estado)
        self.config["status"]["fps"] = fps
        self.config["status"]["clipLength"] = length
        self.config["status"]["indexFormat"] = str(iFormat)
        self.config["status"]["languagerec"] = lang
        self.config["status"]["grabarPantalla"] = str(grabarPantalla)
        self.config["status"]["guardarGrabacion"] = str(guardarGrabacion)
        self.conn.guardar_ini()
    
    def get_start_status(self):
        # Establecer el estado inicial del Checkbutton desde el archivo INI
        try:
            estado = self.config["status"].getint("verGrabacion")
            fps = self.config["status"].getint("fps")
            length = self.config["status"].getint("clipLength")
            indFormat = self.config["status"].getint("indexFormat")
            lang = self.config["status"]["languagerec"]
            grabarPantalla = self.config["status"].getint("grabarPantalla")
            guardarGrabacion = self.config["status"].getint("guardarGrabacion")
        except (KeyError, ValueError):
            estado = 0  # Valor por defecto si no existe o es inválido
            fps=15
            length = 10
            indFormat = 0
            lang = "en-US"
            grabarPantalla = 1
            guardarGrabacion = 1
        self.guardarGrab.set(guardarGrabacion)
        self.grabarPantalla.set(grabarPantalla)
        self.lang = lang
        self.indexFormat = indFormat
        self.vid_length = length 
        self.fps = fps
        self.vistaPrevia.set(estado)  # 1 para activado, 0 para desactivado

if __name__ == "__main__":
    app = Gui()
