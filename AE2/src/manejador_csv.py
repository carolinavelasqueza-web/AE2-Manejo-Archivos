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
            self.encabezados = next(lector)
            self.datos = [fila for fila in lector]
        return self.encabezados, self.datos

    def _validar_datos(self):
        if not self.datos:
            raise ValueError("No hay datos. Primero importa el archivo.")

    def _validar_fila(self, fila):
        if fila < 0 or fila >= len(self.datos):
            raise IndexError(
                f"Fila {fila} fuera de rango (hay {len(self.datos)} registros)."
            )

    def modificar(self, columna_objetivo, valor_nuevo, fila=0):
        """Actualiza un valor en una columna y fila específicas.
        Devuelve (valor_anterior, valor_nuevo)."""
        self._validar_datos()
        self._validar_fila(fila)
        if columna_objetivo not in self.encabezados:
            raise ValueError(f"La columna '{columna_objetivo}' no existe en el CSV.")

        indice_col = self.encabezados.index(columna_objetivo)
        valor_anterior = self.datos[fila][indice_col]
        self.datos[fila][indice_col] = valor_nuevo
        return valor_anterior, valor_nuevo

    def agregar_registro(self, nueva_fila):
        """Agrega una fila (lista de valores) al final.
        Devuelve el total de registros después de agregar."""
        self._validar_datos()
        if len(nueva_fila) != len(self.encabezados):
            raise ValueError(
                f"La fila tiene {len(nueva_fila)} valores y el CSV tiene "
                f"{len(self.encabezados)} columnas."
            )
        self.datos.append([str(valor) for valor in nueva_fila])
        return len(self.datos)

    def eliminar_registro(self, indice):
        """Elimina la fila en la posición indicada.
        Devuelve la fila eliminada."""
        self._validar_datos()
        self._validar_fila(indice)
        return self.datos.pop(indice)

    def guardar(self):
        """Guarda el nuevo CSV usando csv.writer, incluyendo encabezados"""
        with open(self.ruta_salida, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)