## Pasos de Ejecución

1. Clonar este repositorio.
2. Tener Python 3.x (solo se usan módulos estándar: `csv`, `json`, `os`, `datetime`; no se requiere instalar paquetes).
3. Abrir `AE2/AE2_Notebook.ipynb` en Jupyter o VS Code, **con la carpeta `AE2` como directorio de trabajo** (las rutas son relativas).
4. Ejecutar **Kernel → Restart & Run All**.
5. Revisar en `data/` los archivos de salida y `resumen.txt`.

## Modificaciones realizadas
- **CSV** (`ManejadorCSV`): se actualiza el valor de `Species` en la fila 0 y se agrega un registro nuevo (150 → 151 registros).
- **JSON** (`ManejadorJSON`): se agrega la clave `procesado_por` a todos los registros y se elimina el último (4 → 3 registros).
- El notebook relee `modificado.csv` y `modificado.json` desde disco para verificar los cambios.

## Origen de los datos
Descargados **manualmente** de Hugging Face; los archivos originales no se modifican.