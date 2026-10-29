# AE2 - Manejo de Archivos CSV, JSON y TXT

## Descripción
Actividad de aprendizaje que implementa tres clases en Python para importar, modificar y guardar archivos CSV y JSON descargados de Hugging Face, coordinadas desde un Notebook de Jupyter, generando un resumen de ejecución en formato TXT.

## Estructura del Proyecto
- `src/`: Contiene las clases `manejador_csv.py`, `manejador_json.py` y `generador_resumen_txt.py`.
- `data/`: Contiene los archivos originales (`original.csv`, `original.json`), los modificados y el `resumen.txt`.
- `AE2_Notebook.ipynb`: Notebook que orquesta todo el flujo.

## URLs de Origen de los Datos
- **CSV:** https://huggingface.co/datasets/scikit-learn/iris/resolve/main/Iris.csv
- **JSON:** https://huggingface.co/datasets/datasets-examples/doc-formats-json-1/resolve/main/data.json

## Pasos de Ejecución
1. Clonar este repositorio.
2. Asegurarse de tener Python 3.x instalado.
3. Abrir `AE2_Notebook.ipynb` en Jupyter Notebook o VS Code.
4. Ejecutar todas las celdas en orden ("Run All").
5. Revisar la carpeta `data/` para verificar los archivos de salida y el `resumen.txt`.