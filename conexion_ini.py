import configparser

class connIni:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_file = "config.ini"
        self.leer_ini()
        
    def leer_ini(self):
        # Leer archivo INI o crear un archivo de configuración predeterminado si no existe
        try:
            self.config.read(self.config_file)
            if "status" not in self.config:
                self.config["status"] = {
                    "grabarpantalla": "1",
                    "vergrabacion": "1",
                    "fps":"15",
                    "langindex": "0",
                    "languageRec": "es-ES",
                    "clipLength": "10",
                    "indexformat": "0",
                    "guardarGrabacion": "0"
                    }  # Valores por defecto
                self.guardar_ini()
            return self.config
        except Exception as e:
            print(f"Error leyendo el archivo INI: {e}")
        
    def guardar_ini(self):
        # Guardar configuraciones en el archivo INI
        with open(self.config_file, "w") as archivo:
            self.config.write(archivo)