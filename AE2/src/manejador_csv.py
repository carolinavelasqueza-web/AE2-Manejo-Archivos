import csv

class ManejadorCSV:
    def __init__(self, ruta_entrada, ruta_salida):
        self.ruta_entrada = ruta_entrada
        self.ruta_salida = ruta_salida
        self.encabezados = []
        self.datos = []

    def importar(self):
        """Importa el CSV usando csv.reader"""
        with open(self.ruta_entrada, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)  # Guardamos los encabezados
            self.datos = [fila for fila in lector]
        return self.encabezados, self.datos

    def modificar(self, columna_objetivo, valor_nuevo, fila=0):
        """Modifica un valor en una columna específica"""
        if not self.datos:
            raise ValueError("No hay datos para modificar. Primero importa el archivo.")
        
        if columna_objetivo not in self.encabezados:
            raise ValueError(f"La columna '{columna_objetivo}' no existe en el CSV.")
        
        indice_col = self.encabezados.index(columna_objetivo)
        valor_anterior = self.datos[fila][indice_col]
        self.datos[fila][indice_col] = valor_nuevo
        
        return valor_anterior, valor_nuevo

    def guardar(self):
        """Guarda el nuevo CSV usando csv.writer"""
        with open(self.ruta_salida, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)