class GeneradorResumenTXT:
    def __init__(self, url_csv, url_json):
        self.url_csv = url_csv
        self.url_json = url_json
        self.operaciones = []

    def registrar_operacion(self, formato, archivo_origen, archivo_salida, modificacion, registros):
        """Registra una operación realizada"""
        self.operaciones.append({
            "formato": formato,
            "origen": archivo_origen,
            "salida": archivo_salida,
            "modificacion": modificacion,
            "registros": registros
        })

    def generar_resumen(self, ruta_salida_txt):
        """Genera el archivo resumen.txt"""
        with open(ruta_salida_txt, mode='w', encoding='utf-8') as txt:
            txt.write("=== RESUMEN DE EJECUCIÓN - AE2 ===\n\n")
            txt.write("URLs de origen:\n")
            txt.write(f"- CSV: {self.url_csv}\n")
            txt.write(f"- JSON: {self.url_json}\n\n")
            
            txt.write("Clases y métodos utilizados:\n")
            txt.write("- ManejadorCSV: importar(), modificar(), guardar()\n")
            txt.write("- ManejadorJSON: importar(), modificar(), guardar()\n")
            txt.write("- GeneradorResumenTXT: registrar_operacion(), generar_resumen()\n\n")
            
            txt.write("=== DETALLE DE OPERACIONES ===\n")
            for i, op in enumerate(self.operaciones, 1):
                txt.write(f"\nOperación {i}:\n")
                txt.write(f"  Formato: {op['formato']}\n")
                txt.write(f"  Archivo importado: {op['origen']}\n")
                txt.write(f"  Modificación: {op['modificacion']}\n")
                txt.write(f"  Archivo guardado: {op['salida']}\n")
                txt.write(f"  Registros procesados: {op['registros']}\n")