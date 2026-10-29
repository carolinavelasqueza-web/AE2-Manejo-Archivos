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

    def _validar_lista(self):
        """Verifica que haya datos importados y que sean una lista de registros"""
        if self.datos is None:
            raise ValueError("No hay datos. Primero importa el archivo.")
        if not isinstance(self.datos, list):
            raise TypeError("Se esperaba una lista de registros en el JSON.")

    def modificar(self, clave_nueva, valor_nuevo):
        """Agrega o actualiza una clave en todos los registros.
        Devuelve la cantidad de registros modificados."""
        self._validar_lista()
        modificados = 0
        for registro in self.datos:
            if isinstance(registro, dict):
                registro[clave_nueva] = valor_nuevo
                modificados += 1
        return modificados

    def agregar_registro(self, registro):
        """Agrega un nuevo registro (diccionario) al final de la lista.
        Devuelve el total de registros después de agregar."""
        self._validar_lista()
        if not isinstance(registro, dict):
            raise TypeError("El registro debe ser un diccionario.")
        self.datos.append(registro)
        return len(self.datos)

    def eliminar_registro(self, indice):
        """Elimina el registro en la posición indicada.
        Devuelve el registro eliminado."""
        self._validar_lista()
        if indice < 0 or indice >= len(self.datos):
            raise IndexError(
                f"Índice {indice} fuera de rango (hay {len(self.datos)} registros)."
            )
        return self.datos.pop(indice)

    def guardar(self):
        """Guarda el nuevo JSON usando json.dump"""
        with open(self.ruta_salida, mode='w', encoding='utf-8') as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)