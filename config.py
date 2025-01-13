import os
import tkinter as tk
import configparser
from tkinter import ttk, messagebox,filedialog
from pathlib import Path

class Gui:
    def __init__(self):
        self.base = tk.Tk()
        self.var = tk.IntVar()  # IntVar para manejar el estado del Checkbutton
        self.fps = 0
        self.vid_length = 0
        self.indexFormat = 0
        self.base.title("Configuración Clips")
        
        self.config = configparser.ConfigParser()
        self.config_file = "config.ini"
        self.leer_ini()  # Leer configuraciones desde el archivo INI
        self.get_start_status()  # Establecer el estado inicial del Checkbutton
        self.crear_formulario()  # Crear el formulario de la GUI
        
        self.base.geometry("500x720")  # Definir tamaño de la ventana
        
        self.base.mainloop()  # Iniciar el bucle principal de la GUI
    
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
    
    def guardar_ini(self):
        # Guardar configuraciones en el archivo INI
        with open(self.config_file, "w") as archivo:
            self.config.write(archivo)
    
    def crear_formulario(self):
        # Crear Checkbutton
        ttk.Label(self.base,text="Vista previa").grid(column=0,row=1)
        chk = ttk.Checkbutton(self.base, variable=self.var)
        chk.grid(column=1, row=1,pady=10)
        
        # Crear Spinbox de ejemplo
        ttk.Label(self.base,text="FPS",justify="right").grid(column=0,row=2)
        self.spinFps = ttk.Spinbox(self.base, from_=0, to=60,justify="left",increment=5)
        self.spinFps.grid(column=1, row=2,pady=10)
        self.spinFps.set(self.fps)
        
        ttk.Label(self.base,text="Duracion",justify="right").grid(column=0,row=3,pady=10)
        self.length = ttk.Spinbox(self.base,from_=5,to=60,increment=5)
        self.length.grid(column=1,row=3)
        self.length.set(self.vid_length)
        
        ttk.Label(self.base,text="Formato de salida",justify="right").grid(column=0,row=4,pady=10)
        self.format = ttk.Combobox(self.base,values=["mp4","avi","mov","webm"],state="readonly")
        self.format.current(self.indexFormat)
        self.format.grid(column=1,row=4)
        
        ttk.Button(self.base,text="Abrir carpeta contenedora",command=self.abrir_carpeta).grid(column=0,row=6)
        ttk.Button(self.base,text="Guardar Configuracion",command=self.save_status).grid(column=0,row=7)
        
    def abrir_carpeta(self):
        try:
            vid_path = Path("videos").absolute()
            filedialog.askdirectory(title="Carpeta",initialdir=vid_path)
            
            
        except Exception as e:
            messagebox.showerror("Error al abrir la carpeta",f"Eror: {e}")
    
    def save_status(self):
        # Obtener el estado actual del Checkbutton
        estado = self.var.get()
        fps = self.spinFps.get()
        length = self.length.get()
        iFormat = self.format.current()
        # Guardar el nuevo estado en el archivo INI
        self.config["status"]["verGrabacion"] = str(estado)
        self.config["status"]["fps"] = str(fps)
        self.config["status"]["clipLength"] = str(length)
        self.config["status"]["indexFormat"] = str(iFormat)
        self.guardar_ini()
    
    def get_start_status(self):
        # Establecer el estado inicial del Checkbutton desde el archivo INI
        try:
            estado = self.config["status"].getint("verGrabacion")
            fps = self.config["status"].getint("fps")
            length = self.config["status"].getint("clipLength")
            indFormat = self.config["status"].getint("indexFormat")
        except (KeyError, ValueError):
            estado = 0  # Valor por defecto si no existe o es inválido
            fps=15
            length = 10
            indFormat = 0
        self.indexFormat = indFormat
        self.vid_length = length 
        self.fps = fps
        self.var.set(estado)  # 1 para activado, 0 para desactivado

if __name__ == "__main__":
    app = Gui()
