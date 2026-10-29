import json

class ManejadorJSON:
    def __init__(self, ruta_entrada, ruta_salida):
        self.ruta_entrada = ruta_entrada
        self.ruta_salida = ruta_salida
        self.datos = None

    def importar(self):
        """Importa el JSON usando json.load"""
        with open(self.ruta_entrada, mode='r', encoding='utf-8') as archivo:
            self.datos = json.load(archivo)
        return self.datos

    def modificar(self, clave_nueva, valor_nuevo):
        """Agrega o modifica una clave en los datos"""
        if self.datos is None:
            raise ValueError("No hay datos para modificar. Primero importa el archivo.")
        
        if isinstance(self.datos, list):
            # Si es una lista de diccionarios
            for registro in self.datos:
                if isinstance(registro, dict):
                    registro[clave_nueva] = valor_nuevo
        elif isinstance(self.datos, dict):
            # Si es un solo diccionario
            self.datos[clave_nueva] = valor_nuevo
            
        return self.datos

    def guardar(self):
        """Guarda el nuevo JSON usando json.dump"""
        with open(self.ruta_salida, mode='w', encoding='utf-8') as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)