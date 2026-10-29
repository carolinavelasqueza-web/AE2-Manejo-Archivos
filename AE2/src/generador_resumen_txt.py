import os
from datetime import datetime


class GeneradorResumenTXT:
    """Genera resumen.txt a partir de los resultados reales de ManejadorCSV
    y ManejadorJSON. Nada del contenido está escrito a mano: todo lo que
    aparece en el TXT fue registrado durante la ejecución."""

    def __init__(self, url_csv, url_json):
        self.url_csv = url_csv
        self.url_json = url_json
        self.operaciones = []
        self._llamadas_propias = {"__init__": 1, "registrar_operacion": 0}

    def registrar_operacion(self, formato, clase, archivo_origen, archivo_salida,
                            metodos, modificaciones, registros_antes,
                            registros_despues):
        """Registra una operación realizada sobre un archivo.

        metodos: lista de nombres de métodos que se llamaron (list[str]).
        modificaciones: lista de descripciones de cambios reales (list[str]).
        """
        self._llamadas_propias["registrar_operacion"] += 1
        self.operaciones.append({
            "formato": formato,
            "clase": clase,
            "origen": archivo_origen,
            "salida": archivo_salida,
            "metodos": list(metodos),
            "modificaciones": list(modificaciones),
            "antes": registros_antes,
            "despues": registros_despues,
        })

    def generar_resumen(self, ruta_salida_txt):
        """Escribe el resumen.txt con los datos registrados."""
        total_procesados = sum(op["antes"] for op in self.operaciones)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ruta_salida_txt, mode='w', encoding='utf-8') as txt:
            txt.write("=== RESUMEN DE EJECUCIÓN - AE2 ===\n")
            txt.write(f"Fecha de ejecución: {fecha}\n\n")

            txt.write("URLs de origen:\n")
            txt.write(f"- CSV: {self.url_csv}\n")
            txt.write(f"- JSON: {self.url_json}\n\n")

            txt.write("=== DETALLE DE OPERACIONES ===\n")
            for i, op in enumerate(self.operaciones, 1):
                txt.write(f"\nOperación {i} ({op['formato']}):\n")
                txt.write(f"  Clase utilizada: {op['clase']}\n")
                txt.write(f"  Métodos llamados: {', '.join(m + '()' for m in op['metodos'])}\n")
                txt.write(f"  Archivo importado: {op['origen']}\n")
                txt.write("  Modificaciones realizadas:\n")
                for mod in op["modificaciones"]:
                    txt.write(f"    - {mod}\n")
                existe = "sí" if os.path.exists(op["salida"]) else "NO"
                txt.write(f"  Archivo guardado: {op['salida']} (existe: {existe})\n")
                txt.write(f"  Registros antes: {op['antes']} | después: {op['despues']}\n")

            txt.write("\n=== TOTALES ===\n")
            txt.write(f"Registros importados en total: {total_procesados}\n")
            txt.write(f"Operaciones registradas: {len(self.operaciones)}\n\n")

            self._llamadas_propias["generar_resumen"] = 1
            txt.write("Clases y métodos utilizados (según la ejecución):\n")
            for op in self.operaciones:
                txt.write(f"- {op['clase']}: {', '.join(m + '()' for m in op['metodos'])}\n")
            propios = ', '.join(f"{m}() x{n}" for m, n in self._llamadas_propias.items()
                                if m != "__init__")
            txt.write(f"- GeneradorResumenTXT: {propios}\n")