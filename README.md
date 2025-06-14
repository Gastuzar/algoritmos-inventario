## 👥 Integrantes - Comisión 5

Gaston Zarate - Gastonzarate25@gmail.com
Nahuel Romero - nahuelromero43@outlook.es

# Inventario con búsqueda y ordenamiento en Python

## 📌 Descripción
Este proyecto simula un **sistema de inventario de productos**, enfocado en aplicar algoritmos clásicos de **búsqueda** y **ordenamiento** sobre un conjunto de datos cargados desde un archivo `.csv`. El programa permite buscar productos por nombre, ordenar por precio o stock, y guardar los resultados ordenados.

Está pensado como un caso práctico para aplicar conocimientos de algoritmos, análisis de eficiencia y estructuras de datos en Python.

🔗Link de video
https://www.youtube.com/watch?v=BfF1tXyxVvA

## 🚀 Funcionalidades
- ✅ Carga de productos desde archivo `inventario_productos.csv`
- ✅ Búsqueda de productos por nombre con:
  - Búsqueda Lineal
  - Búsqueda Binaria
- ✅ Ordenamiento de productos por:
  - Precio (Bubble Sort)
  - Stock (Quick Sort)
- ✅ Medición del tiempo de ejecución de cada algoritmo
- ✅ Guardado de resultados ordenados en archivos CSV (`ordenado.csv`), sobreescribiendo el archivo dependiendo de la busqueda que se realice
- ✅ Interfaz por menú en consola para interacción clara
- ✅ Código modular, separado en archivos `main.py`, `ordenamiento.py`, y `busqueda.py` ademas de los archivos csv correspondientes

## 🐍 Tecnologías
- 🐍 **Python 3.13.0**
- 📄 **csv**: para lectura y escritura de archivos de productos
- ⏱️ **time.perf_counter()**: para medición precisa del rendimiento de los algoritmos
- 🧮 Algoritmos clásicos:
  - **Búsqueda lineal**: O(n)
  - **Búsqueda binaria**: O(log n)
  - **Bubble sort**: O(n²)
  - **Quick sort**: O(n log n)

## 🎓 Reflexión
- Este trabajo permitió aplicar la teoría de búsqueda y ordenamiento a un caso práctico, reforzando conceptos clave y evaluando la eficiencia de cada algoritmo en un entorno simulado.

## ▶️ Cómo ejecutar
1. Iniciar Vscode.
2. Colocá en la misma carpeta:
   - `main.py`
   - `busqueda.py`
   - `ordenamiento.py`
   - `inventario_productos.csv`
   - `ordenado.csv`
3. Abrí una terminal y ejecutá:

```bash
python main.py

